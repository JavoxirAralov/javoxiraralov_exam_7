from django.contrib import admin


from apps.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass