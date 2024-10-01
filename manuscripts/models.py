from django.db import models
from django.utils.translation import gettext_lazy as _lazy

from simple_api import settings


class ManuscriptCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


MANUSCRIPT_STATUS = (
    ('WP', _lazy('Waiting for automatic parsing')),
    ('W', _lazy('Waiting for admin review')),
    ('D', _lazy('Declined')),
    ('A', _lazy('Accepted'), )
)


class Manuscript(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ManuscriptCategory, related_name='category', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manuscripts')
    file = models.FileField(upload_to='manuscripts')
    status = models.CharField(max_length=2, choices=MANUSCRIPT_STATUS, default='WP')
    # The field is for admin notes.
    notes = models.TextField(null=True, blank=True)
    # todo add additional data with celery queue.
