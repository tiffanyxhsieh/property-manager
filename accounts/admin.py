from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Customer, Employee, User
from django.contrib.auth.forms import UserCreationForm

admin.site.unregister(User)


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name','password1','password2')


class MyUserAdmin(BaseUserAdmin):
    add_form = MyUserCreationForm

# don't forget to register your custom admin class
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)


