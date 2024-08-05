from app6.views import  helloList
from .import views
from django.urls import path
from .views import hellocreate
from .views import helloList
from .views import helloDetailView
from .views import helloUpdateView
from .views import helloDeleteView

urlpatterns=[
    path("",hellocreate.as_view()),
    path("list/",helloList.as_view()),
    path('<pk>/',helloDetailView.as_view()),
    path('<pk>/update',helloUpdateView.as_view()),
    path('<pk>/delete/',helloDeleteView.as_view()),

]