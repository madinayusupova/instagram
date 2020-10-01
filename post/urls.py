from django.urls import path
from post.views import *

app_name = 'post'
urlpatterns = [
    path('post_create/', PostCreateView.as_view()),
    path('post_all', PostListView.as_view()),
    path('post/detail/<int:pk>', PostDetailView.as_view()),
    # path('post/search/', PostSearchListView.as_view())
]