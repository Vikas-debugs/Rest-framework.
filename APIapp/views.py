from django.shortcuts import render
from .serializer import TodoSerializer
from  rest_framework.decorators import api_view
from  rest_framework import  viewsets
from  rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Todo
@api_view(['GET', 'POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response(
            {
                "status": 200,
                "msg" :"welcome"
            }
        )
    elif request.method == "PATCH":
        return Response(
            {
                "status": 200,
                "msg": "welcome TO patch Method"
            }
        )
    else:
        return Response(
            {
                "status": 400,
                "msg": "envalid request method"
            }
        )


@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs , many =True)
    return Response({
        "status":True,
        'msg': 'todo',
        'data': serializer.data


    })

@api_view(['POST'])
def post_todo(request):
    try :
        data =  request.data
        serializer = TodoSerializer (data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": 'sucessfull',
                    "msg": "post-todo",
                    'data': serializer.data
                }
            )
        return Response(
            {
                "status": 'false',
                "msg": "post-todo"
            }
        )
    except Exception as a:
        print(a)
    return Response(
        {
            "status": 'sucessfull',
            "msg": "post-todo"
        }
    )

# @api_view(['PATCH'])
# def patch_todo(request):
#     try:
#         data = request.data
#         if not dada.get('uid'):
#             return Response({
#                 'status': False,
#                 'msg': 'worng',
#                 'data':{}
#             })
#      obj = Todo.objects.get(uid =data.get('uid'))
#      serializer = TodoSerializer(obj, data = data, partial= True  )
#      if  serializer.is.valid():
#         serializer.save()
#         return Response(
#             {
#                 "status": 'sucessfull',
#                 "msg": "post-todo",
#                 'data': serializer.data
#             }
#         )
#
#     return Response(
#         {
#             "status": False,
#             "msg": "post-todo",
#             'data': serializer.errors
#         }
#     )
#     except Exception as e:
#       print(e)
#     return Response(
#         {
#             "status": False,
#             "msg": "invalid uid",
#             'data': {}
#         }
#     )
# # Create your views here.

#********* CBV************************
class todoView(APIView):
    def get(self,request):
        todo_objs =Todo.objects.all()
        serializer = TodoSerializer(todo_objs, many =True)
        return Response({
            'status': 200,
            'msg': 'yes get is working',
            'method': 'GET method',
            'data': serializer.data

        })
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'msg': 'yes post is working',
                    'method': 'POST method'
                })
        except Exception as a:
            print(a)

# *********ViewSets*******************************

class todoviewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class =TodoSerializer


# def count(request):
#     if "count" in request.COOKIES:
#         newc =int(request.COOKIES['count'])+1
#     else:
#         newc= 1;
#     response =render(request,'count.html',{'count':newc})
#     response.set_cookie('count',newc)
#     return response

# **************************session management using SESSION API ******************************
def count(request):
        count = request.session.get('count',0)
        nc =count+1
        request.session['count'] = nc
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        return render(request,'count.html',{'count':nc})
# *********session management by using Cookies************************************

def  name(request):
    return render(request,'name.html')
def age(request):
    name= request.GET['name']
    response = render(request,'age.html',{'name':name})
    response.set_cookie('name',name)
    return response
def gf(request):
    age = request.GET['age']
    name = request.COOKIES['name']
    response = render(request, 'gf.html', {'name': name})
    response.set_cookie('age', age)
    return response
def result (request):
    name = request.COOKIES['name']
    age =request.COOKIES['age']
    gfname= request.GET['gfname']
    response = render(request, 'gf.html', {'name': name, 'age': age, 'gfname':gfname})
    response.set_cookie('gfname', gfname)
    return response