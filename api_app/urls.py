from django.urls import path
from . import views 

urlpatterns= [
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentDestroy.as_view()),
    
    # These are for combinagtion url path
    path('studentapi/',views.StudentListCreate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieveDestroy.as_view()),
    path('studentapi/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),
]