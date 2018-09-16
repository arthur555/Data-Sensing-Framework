from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question, KeyForm,Tweet
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import HomeForm

from . import callGetATweet as te
from . import kk 
class HomeView(TemplateView):
    template_name = 'polls/home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form })

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            te.call(text)
            objectss = []
            for i in range(7):
                objectss.append( Tweet.objects.filter(cluster = str(i+1))[1])

        args = {'form':form, 'text':text, 'cluster':cluster,'objects':objectss}
        return render(request, self.template_name, args)
            
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
            'latest_questions':latest_questions,
            }
    return render(request, 'polls/index.html',context)

def cluster(request, cluster):
    objects = Tweet.objects.filter(cluster = cluster)
    return render(request, 'polls/cluster.html',{'cluster':cluster,'objects':objects})

def detail(request,question_id):   
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):  
    response = "You'are looking for the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question%s." % question_id)




# Create your views here.
