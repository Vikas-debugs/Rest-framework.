from django.urls import path
# ********for viewset urls**********
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'todoviewset', todoviewset, basename='todoviewset')
urlpatterns = [
    # **********FBViews******************

    path('', home, name="home"),
    path('result/', result, name="result"),
    path('pviews/', pviews, name="pviews"),
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
    path('todoView/', todoView.as_view(), name='todoView')
]
urlpatterns += router.urls
