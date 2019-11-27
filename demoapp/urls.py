from django.urls import path

from . import views

app_name = "demoapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('exam/<int:question_no>',views.exam, name='exam'),
    path('results/',views.generate_results, name='results'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('results/',views.generate_results, name='generate_results'),
    path('exam/<int:question_no>/answer/', views.answer, name='answer'),

]
