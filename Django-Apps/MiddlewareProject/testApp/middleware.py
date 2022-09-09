
class LoginMiddleware(object) :
    def __init__(self,get_response):
       self.get_response=get_response

    def __call__(self,request):
        print("This line printead at pre processing")
        response=self.get_response(request)
        print("Post preprocessing")
        return response

from  django.http import HttpResponse
class AppMaintenanceMiddleware(object) :
    def __init__(self,get_reponse):
       self.get_reponse=get_reponse

    def __call__(self,request):
        return HttpResponse('<h1> Current Application is under Maintance Try After Few Days..</h1>')

class ErrorMessegeMiddleware(object) :
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        s='<h1>Currently we are facing some technical problems</h1><hr>'
        s1='<h1>Raised Exception:{}</h1>'.format(exception.__class__.__name__)
        s2='<h1>Exception Description:{}'.format(exception)
        return HttpResponse(s+s1+s2)