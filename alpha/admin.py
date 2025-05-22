from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import*

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Replies)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(News)
admin.site.register(NewsComment)
admin.site.register(PaymentSwitch)
admin.site.register(PaymentMethod)
admin.site.register(SubmitPayment)
admin.site.register(SavedQuestion)





# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'status')  # Exclude username
    list_filter = ('is_staff', 'status')  # Exclude username
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'profile_pic', 'department','status')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')  # Exclude username
    ordering = ('email',)  # Exclude username

admin.site.register(CustomUser, CustomUserAdmin)
