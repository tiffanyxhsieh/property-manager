from django.shortcuts import render
from accounts.models import Customer, Employee
# Create your views here.


def dashboard(request):

    if Customer.objects.filter(user_id=request.user.id).exists():
        return render(
            request,
            'dashboard_customer.html'
        )
    else:
        return render(
            request,
            'dashboard_leasing_employee.html'
        )


