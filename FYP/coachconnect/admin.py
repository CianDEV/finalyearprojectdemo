from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Unregister Groups

admin.site.unregister(Group)

# Add profile info to user
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User

    # Only display username field
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister Initial User
admin.site.unregister(User)

# Re-Register User and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)
