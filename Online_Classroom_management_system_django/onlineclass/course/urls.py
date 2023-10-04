from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/detail/', views.detail, name='detail'),
    path('<int:assignment_id>/upload_submission/', views.upload_submission, name='upload_submission'),
    path('<int:course_id>/view_assignments/', views.view_assignments, name='view_assignments'),
    path('<int:course_id>/view_resources/', views.view_resources, name='view_resources'),
]































# ## @brief urls for the course app.

# from django.conf.urls import url, include
# from django.contrib import admin
# from . import views

# ## @brief url patterns for the course app.
# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^(?P<course_id>[0-9]+)/detail/$', views.detail, name='detail'),
#     url(r'^index/$', views.index, name='index'),
#     url(r'^(?P<assignment_id>[0-9]+)/upload_submission/$', views.upload_submission, name='upload_submission'),
#     url(r'^(?P<course_id>[0-9]+)/view_assignments/$', views.view_assignments, name='view_assignments'),
#     url(r'^(?P<course_id>[0-9]+)/view_resources/$', views.view_resources, name='view_resources'),
# ]