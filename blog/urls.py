from django.urls import path
from . import  views



urlpatterns = [
# path('',views.home),
path('students/', views.StudentListView.as_view(),name="student_list"),
path('student/<int:pk>/', views.StudentDetailView.as_view()),
path("",views.StudentCreateView.as_view()),
path("student/update/<int:pk>/",views.StudentUpdateView.as_view()),
path("student/delete/<int:pk>/",views.StudentDeleteView.as_view()),

]

