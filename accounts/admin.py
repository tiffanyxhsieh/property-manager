from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Customer, Employee, User
from django.contrib.auth.forms import UserCreationForm

admin.site.unregister(User)


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        pass


class MyUserAdmin(BaseUserAdmin):
    add_form = MyUserCreationForm


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('ss_number',)

# don't forget to register your custom admin class
admin.site.register(User)



