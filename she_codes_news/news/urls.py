from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('<int:pk>/edit', views.EditStoryView.as_view(), name='editStory'),
    path('all-stories/', views.All_stories_View.as_view(), name='allstories' ),
    path('authors/<int:pk>/stories', views.AuthorStories.as_view(), name= 'authorstories' ),
   path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory')
    ]

