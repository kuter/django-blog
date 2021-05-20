from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Post


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('pk', 'title', 'active')
    list_filter = ('active', 'created', 'modified')
    search_fields = ('title', )


admin.site.register(Post, PostAdmin)
admin.site.site_header = _('Django blog')
