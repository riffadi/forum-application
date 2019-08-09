from django.urls import path
from .views import (ForumCreate,ForumList,ForumUserList,
					ForumDetail, ForumUpdate, ForumDelete,
					CommentCreate, CommentUpdate, CommentDelete)


urlpatterns = [
	path('add/', ForumCreate.as_view(), name='forum-add'),
	path('edit/<int:pk>', ForumUpdate.as_view(), name='forum-edit'),
	path('delete/<int:pk>', ForumDelete.as_view(), name='forum-delete'),
	path('', ForumList.as_view(), name='forum-list'),
	path('<slug:slug>/', ForumDetail.as_view(), name='forum-detail'),
	path('by/<username>/', ForumUserList.as_view(), name='forum-by'),
	
	path('comment/add/<int:pk>', CommentCreate.as_view(), name='comment-add'),
	path('comment/edit/<int:pk>', CommentUpdate.as_view(), name='comment-edit'),
	path('comment/delete/<int:pk>', CommentDelete.as_view(), name='comment-delete'),

]