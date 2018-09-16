#include<iostream>
using namespace std;
class ArrayList{
	private:
		int length;
		int capacity;
		char[capacity] myArray;
	public:
		void init(int x = 5){
			length = 0;
			capacity = x;
			myArray = char[x];
		}

		int getLength(){
			return length;
		}

		void insert (char[] more, int moreLength)
		{
			if(length+moreLength >= capacity)
			{
				capacity *= 2;
				char[capacity] newArray;
				for (int i = 0; i < length; i ++)
					newArray[i] = myArray[i];
				myArray = newArray;
			}

			for (int i = 0; i < moreLength; i++)
			{
				myArray[length++] = more[i];
			}
		}





		
