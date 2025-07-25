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

