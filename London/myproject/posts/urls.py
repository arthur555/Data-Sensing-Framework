from django.urls import path
from . import views
from .views import HomeView

app_name = 'posts'
urlpatterns = [
        #path('', views.index, name = 'index'),
        #path('<int:question_id>/', views.detail, name = 'detail'),
        #path('<int:question_id>/results/', views.results, name = 'results'),
        #path('<int:question_id>/vote/', views.vote, name = 'vote'),
        path('form/', HomeView.as_view() , name = 'form'),
        ]


