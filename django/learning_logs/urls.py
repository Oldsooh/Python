from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path(r'', views.index, name='index'),

    path(r'topics', views.topics, name='topics'),

    path(r'topics/<int:id>/', views.topic, name='topic')

    path(r'topics/new', view.new_topic, name='new_topic')
]