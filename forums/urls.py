from django.urls import path
from .views import ForumCreate, ForumList,ForumUserList,ForumDetail
urlpatterns = [
	path('add/', ForumCreate.as_view(), name='forum-add'),
	path('', ForumList.as_view(), name='forum-list'),
	path('<slug:slug>/', ForumDetail.as_view(), name='forum-detail'),
	path('by/<username>/', ForumUserList.as_view(), name='forum-by'),
]