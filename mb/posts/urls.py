from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), # "name" tags are used for the anchor tags
    path('list', PostListView.as_view(), name='list'),
    path('<int:pk>', PostDetailView.as_view(), name='detail'),
    path('new/', PostCreateView.as_view(), name='new'),
] 