from django.contrib import admin

from .forms import GalleryItemInlineForm
from .models import Gallery, GalleryImage, Image


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    form = GalleryItemInlineForm
    extra = 0
    raw_id_fields = ('image',)


class GalleryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    inlines = [
        GalleryImageInline,
    ]
    list_display = ('pk', 'title', 'active')
    list_filter = ('active', 'created', 'modified')
    search_fields = ('title', )

    class Media:
        js = (
            'jquery-3.6.0.slim.min.js',
            'jquery-ui.min.js',
            'draggable_inlines.js',
        )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image)
