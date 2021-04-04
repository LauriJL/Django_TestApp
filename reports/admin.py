from django.contrib import admin
from .models import Report, Comment

#class CommentInline(admin.StackedInline):
 #   model = Comment

class CommentInline(admin.TabularInline):
    model = Comment

class ReportAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]

admin.site.register(Report,ReportAdmin)
admin.site.register(Comment)
