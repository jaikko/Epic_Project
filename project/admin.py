from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, Contract, Event, Staff, Status

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = Staff
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'phone', 'mobile', 'team', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'phone', 'mobile', 'team', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')})
    ),
    search_fields = ('email',)
    ordering = ('email',)


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email', 'first_name', 'last_name',)


class StatusAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('status',)
    search_fields = ('status',)
    ordering = ('status',)


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('client', 'attendees', 'event_date',)
    ordering = ('client', 'attendees', 'event_date',)


class ContractAdmin(admin.ModelAdmin):
    model = Contract
    list_display = ('client', 'status', 'amount', 'payment_due',)
    ordering = ('client', 'status', 'amount', 'payment_due',)

admin.site.register(Staff, CustomUserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Contract, ContractAdmin)
