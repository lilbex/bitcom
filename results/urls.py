from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('punits/', views.PollingUnit.as_view(), name='punits'),
    path('postpolls/', views.PostPoll.as_view(), name='postpolls'),
]
