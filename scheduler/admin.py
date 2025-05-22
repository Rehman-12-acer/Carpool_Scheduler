from django.contrib import admin
from .models import UserProfile, Schedule, Match

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'car_available', 'car_capacity')
    search_fields = ('user__username', 'phone_number')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'start_time', 'end_time', 'origin', 'destination')
    list_filter = ('day', 'user')
    search_fields = ('user__username', 'origin', 'destination')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('schedule1', 'schedule2', 'status', 'score', 'created_at')
    list_filter = ('status',)
    search_fields = ('schedule1__user__username', 'schedule2__user__username')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Match, MatchAdmin)