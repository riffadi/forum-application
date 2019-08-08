from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, ListView
from .models import Forum
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ForumListView(ListView):
	model = Forum
	#context_object_name = 'forums'

class ForumUserListView(ListView):
	def get_queryset(self):
		self.user = get_object_or_404(User, username=self.kwargs['username'])
		return Forum.objects.filter(user = self.user)

@method_decorator(login_required, name='dispatch')

class ForumCreate(CreateView):
	model = Forum
	fields = ['title', 'desc']


	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)