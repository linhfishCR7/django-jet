from django.db import models
from django.conf import settings
from django.utils import timezone
try:
    from django.utils.translation import ugettext_lazy as _
except ImportError: # Django 4 (tested with Django 4.0)
    from django.utils.translation import gettext_lazy as _

try:
    from django.utils.encoding import python_2_unicode_compatible
except ImportError:
    from six import python_2_unicode_compatible

@python_2_unicode_compatible
class Bookmark(models.Model):
    url = models.URLField(verbose_name=_('URL'))
    title = models.CharField(verbose_name=_('title'), max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE)
    date_add = models.DateTimeField(verbose_name=_('date created'), default=timezone.now)

    class Meta:
        verbose_name = _('bookmark')
        verbose_name_plural = _('bookmarks')
        ordering = ('date_add',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class PinnedApplication(models.Model):
    app_label = models.CharField(verbose_name=_('application name'), max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE)
    date_add = models.DateTimeField(verbose_name=_('date created'), default=timezone.now)

    class Meta:
        verbose_name = _('pinned application')
        verbose_name_plural = _('pinned applications')
        ordering = ('date_add',)

    def __str__(self):
        return self.app_label

