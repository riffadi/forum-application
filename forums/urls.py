from django.urls import path
from .views import ForumCreate, ForumList,ForumUserList,ForumDetail, ForumUpdate
urlpatterns = [
	path('add/', ForumCreate.as_view(), name='forum-add'),
	path('edit/<int:pk>', ForumUpdate.as_view(), name='forum-edit'),
	path('', ForumList.as_view(), name='forum-list'),
	path('<slug:slug>/', ForumDetail.as_view(), name='forum-detail'),
	path('by/<username>/', ForumUserList.as_view(), name='forum-by'),
]