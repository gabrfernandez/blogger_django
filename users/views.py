from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView
from posts.models import Post
from .forms import RegisterForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib import auth

# Create your views here.
class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        # save the new user first
        form.save()
        # get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect('/')


class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    template_name = 'users/login.html'

@method_decorator(login_required(login_url='/users/login'), name="dispatch")
class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = UserProfile
    template_name = 'users/profile-update.html'
    form_class = UserProfileForm
    success_message = "Your Profile has been updated"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('users:update_profile', kwargs={'slug': self.object.slug})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UserProfileUpdateView, self).get(request, *args, **kwargs)


@method_decorator(login_required(login_url='/users/login'), name="dispatch")
class UserProfileView(ListView):
    template_name = 'users/profile.html'
    model = Post
    context_object_name = 'userposts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['userprofile'] = UserProfile.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by("-id")


class UserPostView(ListView):
    template_name = 'users/user-post.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(user=self.kwargs['pk'])

class UserListView(ListView):
    template_name = 'users/user-list.html'
    model = UserProfile
    context_object_name = 'profiles'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return context