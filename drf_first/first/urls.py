from django.urls import path

from first import views

urlpatterns = [
    path('user/', views.user),
    path('user_view/', views.UserView.as_view()),
    path('teacher/<str:id>/', views.TeacherAPIView.as_view()),
    path('teacher/', views.TeacherAPIView.as_view()),

]