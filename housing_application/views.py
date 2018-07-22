from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.


@login_required
@permission_required('housing_application.can_set_housing_application_status')
def approve_housing_application(self):
    self.lease.get().is_approved = True
    self.application_status = self.APPLICATION_STATUS_OPTIONS[2]


@login_required
@permission_required('housing_application.can_set_housing_application_status')
def deny_housing_application(self):
    self.lease.get().is_approved = False
    self.application_status = self.APPLICATION_STATUS_OPTIONS[3]