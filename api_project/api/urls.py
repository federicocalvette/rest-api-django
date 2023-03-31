from django.urls import path
from .views import CourseView


urlpatterns=[
    path('courses/', CourseView.as_view(), name='courses_list'),
    path('courses/<int:id>', CourseView.as_view(), name='courses_process')
]