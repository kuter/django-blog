from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel


class Post(TimeStampedModel, models.Model):
    active = models.BooleanField(_('active'), default=True)
    title = models.CharField(_('title'), max_length=50)
    slug = AutoSlugField(populate_from='title')
    body = models.TextField(_('body'))

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk, ))
