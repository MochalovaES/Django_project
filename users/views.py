from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView
from users.models import User
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserForm
from django.core.mail import send_mail
from django.shortcuts import redirect
import random


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Подтверждение почты',
            message=f'Код {new_user.ver_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    request.user.set_password(new_password)
    request.user.save()

    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    return redirect(reverse('catalog:product_list'))
