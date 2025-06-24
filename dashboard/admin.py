from django.contrib import admin

# Register your models here.
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_role', 'github_link', 'linkedin_link')
    search_fields = ('member_name', 'member_role')