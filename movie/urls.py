# -*- coding = utf-8 -*-
# @Time : 2020/9/10 12:08
# @Author : hly
# @File : urls.py.py
# @Software : PyCharm
# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'movie'
urlpatterns = [
    # 目前还没有urls
    path('test/', views.test, name='test'),
    path('main_page/<int:page>',views.main_page_movie,name='main_page'),
    path('all_actor/<int:page>',views.all_actors_page,name = 'all_actors'),
    # path('actor/',views.actor_page(),name='actor'),
    path('actorpage/<str:name_>',views.index_,name ='actorpage'),
    path('moviepage/<str:name_>',views.movie_index,name='moviepage'),
    path('search_result/<str:nam>/<str:select_>/<int:page>',views.search_result,name='search_result' ),
    # path('search_result/',views.search_movies,name = 'search_result'),#搜索电影
    path('search_page/',views.search_page,name='search_page'),

]
