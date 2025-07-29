# **************************middleware************************
from django.shortcuts import render, HttpResponse
class FirstMiddelware(object):
    def __init__(self,response):
        self.response = response
    def __call__(self,request):
         print('this is first pre-processingfirst  middelware request')
         respons = self.response(request)
         print('this is first post-processing  first middelware request')
         return respons
class SecondMiddelware(object):
    def __init__(self,response):
        self.response = response
    def __call__(self, request):
        print('this is first pre-processing second  middelware  request')
        respons = self.response(request)
        print('this is  post-processing  second middelware request')
        return respons

class AppMaintenance(object):
    def __init__(self,response):
        self.response = response
    def __call__(self, request):
       return HttpResponse('<h1> Currently App under Maintenance....')


# # class error(object):
#     def __init__(self,response):
#         self.response = response
#     def __call__(self, request):
#        return self.response(request)
#     def exceptions(self,request,exception):
#         return HttpResponse('<h1> we are facing technical problems</h2>')