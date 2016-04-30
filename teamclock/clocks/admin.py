from django.contrib import admin
from .models import Clock, TeamMember



@admin.register(Clock)
class ClockAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    pass
