from django.contrib import admin

from blog.models import Author, Comment, Post, Tag


def get_day_suffix(day):
    """
    Return the suffix for a given day (e.g., 'st', 'nd', 'rd', or 'th').
    """
    if 11 <= day <= 13:  # Special case for teens
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "last_modified", "author", "created_at")
    prepopulated_fields = {"slug": ("title",)}

    def last_modified(self, obj):
        if obj.date:
            day = obj.date.day
            day_with_suffix = f"{day}{get_day_suffix(day)}"
            return obj.date.strftime(f"{day_with_suffix} %b %Y")
        return "-"
    last_modified.short_description = "Last modified"

class CommentAdmin(admin.ModelAdmin):
    list_filter = ("user_name", "user_email")
    list_display = ("user_name", "user_email", "post", "created_at")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
