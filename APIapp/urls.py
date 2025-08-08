from django.urls import path
from django.views.generic.base import TemplateView
from . import views
# ** ************************************************  ******for viewset urls**********
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'todoviewset', todoviewset, basename='todoviewset')
urlpatterns = [

    # *****************TemplateView****************
    path('template/', TemplateView.as_view(template_name="template.html"), name='template'),
    # **********FBViews******************
    path('', home, name="home"),

    path('result/', result, name="result"),
    path('pviews/', pviews, name="pviews"),
    path('filter/', filter, name="filter"),
    path('gfname/', gf, name="gfname"),
    path('age/', age, name="age"),
    path('count/', count, name='count'),
    path('get_cookie/', get_cookie, name='get_cookie'),
    path('del_cookie/', del_cookie, name='del_cookie'),
    path('set_cookie/', set_cookie, name='set_cookie'),
    path('middleware/', middleware, name='middleware'),
    path('set_session/', set_cookie, name='set_session'),
    path('get_session/', get_session, name='get_session'),
    path('del_session/', del_session, name='del_session'),
    path('flush_session/', flush_session, name='flush_session'),
    path('error/', error, name='error'),
    path('get_todo/', get_todo, name='get_todo'),
                                                       # **********CBViews******************
    path('todoView/', todoView.as_view(), name='todoView'),
# *****************************************************************************Captcha*********************************
    path('captcha/', views.captcha_page, name='captcha_page'),
    # URL for the success page
    path('success/', views.success_page, name='success_page'),
]
urlpatterns += router.urls
