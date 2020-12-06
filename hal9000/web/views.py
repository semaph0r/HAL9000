from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CertificateForm
from .models import Certificate
from django.http import HttpResponse


class CertificatesListView(ListView):
    model = Certificate


class CertificateCreateView(CreateView):
    model = Certificate
    fields = [
        'domain',
        'maintainer',
        'send_notification',
    ]
    success_url = reverse_lazy('index')


class CertificateUpdateView(UpdateView):
    model = Certificate
    fields = [
        'domain',
        'maintainer',
        'send_notification',
    ]
    success_url = reverse_lazy('index')


class CertificateDeleteView(DeleteView):
    model = Certificate
    success_url = reverse_lazy('index')


def show(request):
    certificates = Certificate.objects.all()
    data = {'certificates': certificates}
    return render(request, "show.html", {'data': data})


def edit(request, id):
    certificate = Certificate.objects.get(id=id)
    return render(request, 'edit.html', {'certificate': certificate})


def update(request, id):
    certificate = Certificate.objects.get(id=id)
    form = CertificateForm(request.POST, instance = certificate)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'certificate': certificate})
