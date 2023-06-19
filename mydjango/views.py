
from django.http import HttpResponse
from django.shortcuts import render
# from django.shortcuts import HttpResponse
from random import randint


def test(request):
    context = {
        "page_title":"TEST PAGE TITLE",
        'items':[{
            'name':"SIMRAM",
            'age':16,
            'sex':"FEMALE"
        },{
            'name':"RAM",
            'age':24,
            'sex':"MALE"
        },{
            'name':"HARI",
            'age':45,
            'sex':"MALE"
        }]

    }
    return render(request,'blank.html',context)
def index(request):
    value = randint(99,999)
    display = True
    myhobbies = ['Volleyball','Singing','Dancing','Reading']
    context = {
        'page_title':"LEARNING DJANGO",
        'content':"We are learning Django",
        'random':value,
        'display_hobby':display,
        'hobbies':myhobbies

    }
    return render(request,'index.html',context)

    # return HttpResponse("THIS IS RESPONSE FORM DJANGO!")

'''
 this view function return my 
 name on calling localhost:8000/me/
 because it is mapped to path('me/',views.me_view,name='me')
'''

from random import randint

def me_view(request):
    value = randint(99,999)
    return HttpResponse("Its me Aaarv Poudel , The value is {}".format(value))

def dynamic_view(request,mypath):
    return HttpResponse("You have accesses {}".format(mypath))