from django.contrib import admin
from django.utils.html import format_html

from .models import Application, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'job_type', 'posted_by', 'is_active', 'created_at']
    list_filter = ['job_type', 'is_active', 'location']
    search_fields = ['title', 'company', 'description']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'status', 'applied_at', 'resume_link']
    list_filter = ['status', 'applied_at']
    search_fields = ['applicant__username', 'job__title']
    list_editable = ['status']
    readonly_fields = ['applied_at']

    def resume_link(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank">View Resume</a>', obj.resume.url)
        return '-'

    resume_link.short_description = 'Resume'
