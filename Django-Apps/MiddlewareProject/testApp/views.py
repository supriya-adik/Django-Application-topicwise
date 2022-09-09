from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_word_view(request) :
    user=request.user
    print(user)
    print(10/0)
    s='''
          <html>
             <body>
               <h1>Hello This Is First Line Of Response....</h1>
                <h1>Hello This Is First Line Of Response....</h1>

             </body>
          </html>
       '''
    return HttpResponse(s)