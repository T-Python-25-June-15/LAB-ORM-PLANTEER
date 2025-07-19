from django.contrib import admin
from .models import Contact
from plants.models import Plants,Comment
# Register your models here.

class ContactAdmin(admin.ModelAdmin):

    list_display = ("first_name", "last_name", "email", "message", "created_at")

class PlantsAdmin(admin.ModelAdmin):

    list_display = ("name", "about", "user_for", "image", "category", "is_edible", "created_at")
    list_filter = ("category",)

class CommentAdmin(admin.ModelAdmin):

    list_display = ("full_name", "content", "created_at")

admin.site.register(Contact, ContactAdmin)
admin.site.register(Plants, PlantsAdmin)
admin.site.register(Comment, CommentAdmin)