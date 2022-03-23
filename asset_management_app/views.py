import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
import asset_management_app
from asset_management_app.forms import LogMessageForm
from asset_management_app.models import LogMessage
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeListView(ListView):
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


class ProflieView(LoginRequiredMixin, TemplateView):
    template_name = "asset_management_app/accounts/profile.html"


def about(request):
    return render(request, "asset_management_app/about.html")


def contact(request):
    return render(request, "asset_management_app/contact.html")


def hello_there(request, name):
    return render(
        request,
        "asset_management_app/hello_there.html",
        {"name": name, "date": datetime.now()},
    )


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "asset_management_app/log_message.html", {"form": form})
