from django.shortcuts import render

# Create your views here.
def edu_view(request) :
    context = {'skill': 'active'}
    return render(request,'edu/skill.html',context=context)