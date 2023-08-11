from django.urls import path
from . import views

# Namespace for the 'polls' app URLs
app_name = 'polls'

urlpatterns = [
    # Maps the root URL of the 'polls' app to the 'index' view
    path('', views.index, name='index'),

    # Maps a URL path with an integer question ID to the 'detail' view
    path('<int:question_id>/', views.detail, name='detail'),

    # Maps a URL path with a question ID followed by '/results/' to the 'results' view
    path('<int:question_id>/results/', views.results, name='results'),

    # Maps a URL path with a question ID followed by '/vote/' to the 'vote' view
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
