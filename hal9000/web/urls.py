from django.urls import path

from . import views

urlpatterns = [
    path('', views.show, name='index'),
    path('certificates', views.CertificatesListView.as_view(), name='show-certificate'),
    path('certificate/create', views.CertificateCreateView.as_view(), name='create-certificate'),
    path('certificate/<int:pk>/update', views.CertificateUpdateView.as_view(), name='update-certificate'),
    path('certificate/<int:pk>/delete', views.CertificateDeleteView.as_view(), name='delete-certificate'),
]