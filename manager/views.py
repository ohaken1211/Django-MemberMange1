from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *

class PersonListView(TemplateView):
    template_name = "member_list.html"

    def get(self, request, *args, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        
        people= Person.objects.all() # データベースからオブジェクトを取得して
        context['people'] = people  # 入れ物に入れる

        return render(self.request, self.template_name, context)

            
from django.contrib.auth.views import login
from django.contrib.auth import authenticate

class CustomLoginView(TemplateView):
    template_name = "login.html"

    def get(self, _, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return login(self.request, *args, **kwargs)

    def post(self, _, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)  # 1
        if user is not None:
            login(self.request, user)
            return redirect(self.get_next_redirect_url())
        else:
            kwargs = {'template_name': 'login.html'}
            return login(self.request, *args, **kwargs)

    def get_next_redirect_url(self):
        redirect_url = self.request.GET.get('next')
        if not redirect_url or redirect_url == '/':
            redirect_url = '/member_list/'
        return redirect_url

def person_registration(request, *args, **kwargs):

    if request.POST:
        form_data = request.POST

        sex = User.MAN if form_data['sex'] == 'male' else User.WOMAN

        user = User(
            name=form_data['name'],
            sex=sex,
            email=form_data['email'],
        )

        user.set_password(form_data['password'])
        user.save()

        return render(request, "registration_done.html", {"email": form_data['email']})

