from django.urls import path
from . import views

urlpatterns=[
    path("getPlayer/<str:pk>/", views.player, name="get_player"),
    # path("add/", views.addplayer, name="form"),
    # path('usertm/', views.rtm_used, name="rtm")
]