from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('list/', views.student_list),
    path('get_by_id/<int:req_id>/', views.get_student_by_id),
    path('get_by_name/<str:name>/', views.get_student_by_name),
    path('filter_by_grade/<int:grade>/', views.student_list_filter),

]
