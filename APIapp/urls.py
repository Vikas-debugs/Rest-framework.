
from django.contrib import admin
from django.urls import path
from .views import *
# ********for viewset urls**********
from rest_framework.routers import DefaultRouter
router  = DefaultRouter()
router.register(r'todoviewset', todoviewset, basename ='todoviewset')
urlpatterns = [
    #**********FBViews******************

    path('', home, name="home"),
    path('result', result,name ="result"),
    path('gfname', gf, name="gfname"),
    path('age', age, name="age"),
    path('count/', count,name= 'count'),
    path('get_todo',get_todo,name='get_todo'),
    # **********CBViews******************
    path('todoView/',todoView.as_view(),name='todoView')
]
urlpatterns += router.urls