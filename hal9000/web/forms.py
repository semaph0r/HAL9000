from django import forms
from .models import Certificate


class CertificateCreateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = [
            'domain',
            'maintainer',
            'send_notification'
        ]


class CertificateUpdateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = [
            'domain',
            'maintainer',
            'send_notification'
        ]
