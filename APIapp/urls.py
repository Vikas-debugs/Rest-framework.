
from django.contrib import admin
from django.urls import path
from .views import *
# ********for viewset urls**********
from rest_framework.routers import DefaultRouter
router  = DefaultRouter()
router.register(r'todoviewset', todoviewset, basename ='todoviewset')
urlpatterns = [
    #**********FBViews******************
    path('', home,name ="home"),
    path('get_todo',get_todo,name='get_todo'),
    # **********CBViews******************
    path('todoView/',todoView.as_view(),name='todoView')
]
urlpatterns += router.urls