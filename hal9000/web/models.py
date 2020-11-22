from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from enum import Enum


class CommonInfo(models.Model):
    maintainer = models.OneToOneField(User, related_name='maintainer', on_delete=models.DO_NOTHING, null=True)
    send_notification = models.BooleanField()
    notified_at = models.DateTimeField()
    acknowledged_at = models.DateTimeField()
    acknowledged_by = models.ForeignKey(User, related_name='acknowledged', on_delete=models.DO_NOTHING, null=True)


class CertificateStatus(Enum):
    INV = 'Invalid'
    VAL = 'Valid'
    EXP = 'Expired'


class SoftwareStatus(Enum):
    LATEST = 'Latest'
    UPDATE = 'Update'
    CRITICAL = 'Critical update'
    UNKNOWN = 'Unknown'
    ERROR = 'Error'


class Certificate(CommonInfo):
    domain = models.TextField(validators=[URLValidator()])
    status = models.TextField(CertificateStatus)


class Software(CommonInfo):
    name = models.TextField()
    vendor = models.TextField()
    url = models.URLField(max_length=200)
