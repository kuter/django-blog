from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from .models import Comment, Post


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    raw_id_fields = ('post',)


class PostAdmin(ImportExportModelAdmin):
    date_hierarchy = 'created'
    list_display = ('pk', 'title', 'active')
    list_filter = ('active', 'created', 'modified')
    search_fields = ('title', )
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.site_header = _('Django blog')
