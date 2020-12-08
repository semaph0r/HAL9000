from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CertificateCreateForm, CertificateUpdateForm
from .models import Certificate
#from hal9000.monitoring.tls import ssl_expiry_datetime


def index(request):
    certificates = Certificate.objects.all()
    data = {'certificates': certificates}
    return render(request, "index.html", {'data': data})


class CertificatesListView(ListView):
    model = Certificate


def create_certificate_form(request):
    form = CertificateCreateForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, 'certificates/certificate_create_form.html', {'form': form})
    else:
        form = CertificateCreateForm()
        return render(request, 'certificates/certificate_create_form.html', {'form': form})


class CertificateUpdateView(UpdateView):
    model = Certificate
    fields = [
        'domain',
        'maintainer',
        'send_notification',
    ]
    template_name = "certificates/certificate_update_view.html"
    success_url = reverse_lazy('index')


class CertificateDeleteView(DeleteView):
    model = Certificate
    template_name = 'certificates/certificate_confirm_delete.html'
    context_object_name = 'certificate'
    success_url = reverse_lazy('index')