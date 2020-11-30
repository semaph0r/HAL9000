from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator


class Certificate(models.Model):
    INVALID = 'INVALID'
    VALID = 'VALID'
    EXPIRED = 'EXPIRED'
    ERROR = 'ERROR'
    NA = 'N/A'
    CertificateStatus = [
        (INVALID, 'Invalid'),
        (VALID, 'Valid'),
        (EXPIRED, 'Expired'),
        (ERROR, 'Error'),
        (NA, 'N/A')
    ]
    domain = models.TextField(validators=[URLValidator()], null=True)
    status = models.CharField(max_length=20,
                              choices=CertificateStatus,
                              default=NA)
    maintainer = models.ForeignKey(User, related_name='%(class)s_maintainer_created', on_delete=models.DO_NOTHING,
                                   blank=True, null=True)
    send_notification = models.BooleanField()
    notified_at = models.DateTimeField(blank=True, null=True)
    acknowledged_at = models.DateTimeField(blank=True, null=True)
    acknowledged_by = models.ForeignKey(User, related_name='%(class)s_acknowledge_created', on_delete=models.DO_NOTHING,
                                        blank=True, null=True)

    def __str__(self):
        return self.domain


class Software(models.Model):
    LATEST = 'LATEST'
    UPDATE = 'UPDATE'
    CRITICAL = 'CRITICAL'
    UNKNOWN = 'UNKNOWN'
    ERROR = 'ERROR'
    NA = 'N/A'
    SoftwareStatus = [
        (LATEST, 'Latest'),
        (UPDATE, 'Update'),
        (CRITICAL, 'Critical'),
        (UNKNOWN, 'Unknown'),
        (ERROR, 'Error'),
        (NA, 'N/A'),
    ]
    name = models.TextField()
    vendor = models.TextField()
    url = models.URLField(max_length=100)
    status = models.CharField(max_length=20,
                              choices=SoftwareStatus,
                              default=NA)
    maintainer = models.ForeignKey(User, related_name='%(class)s_maintainer_created', on_delete=models.DO_NOTHING,
                                   blank=True, null=True)
    send_notification = models.BooleanField()
    notified_at = models.DateTimeField(null=True)
    acknowledged_at = models.DateTimeField(null=True)
    acknowledged_by = models.ForeignKey(User, related_name='%(class)s_acknowledge_created', on_delete=models.DO_NOTHING,
                                        blank=True, null=True)

    def __str__(self):
        return self.name
