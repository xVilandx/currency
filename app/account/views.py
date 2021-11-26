from account.forms import UserSignUpForm
from account.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView


class UserSignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = UserSignUpForm


class UserActivateView(RedirectView):
    pattern_name = 'login'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = User.objects.filter(username=username).only('id').first()
        if user:
            user.is_active = True
            user.save(update_fields=['is_active'])
        url = super().get_redirect_url(*args, **kwargs)
        return url


class ProfileView(LoginRequiredMixin, UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
        'avatar',
    )

    def get_object(self, queryset=None):
        return self.request.user
