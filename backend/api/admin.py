from django.contrib import admin
from .models import Page

admin.site.register(Page)

# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
    # list_display = ('title', 'created_at')
    # Uncomment line 8 if slugs starts to get integrated into the app
    # prepopulated_fields = {'slug': ('title',)}
