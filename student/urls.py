from django.urls import path

from . import views

urlpatterns = [
  path('student', views.students),
  # path('teacher', views.teachBanv),
  # path('teacher/<int:pk>', views.teachBanv),
  path('student/<int:pk>/', views.students),
  path('student/update/<str:pk>/', views.updateStudent),
  path('studentName/<str:name>/', views.studentName),
  # path('student/<int:id>/', views.student),
#   path('student/', views.student),
]