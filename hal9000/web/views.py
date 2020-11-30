from django.shortcuts import render, redirect
from .forms import CertificateForm
from .models import Certificate
from django.http import HttpResponse


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


def destroy(request, id):
    certificate = Certificate.objects.get(id=id)
    certificate.delete()
    return redirect("/show")
