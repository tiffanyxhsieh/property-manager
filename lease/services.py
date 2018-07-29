from .models import Lease
from housing_application.models import HousingApplication
import housing_application.services


def get_active_leases():
    return HousingApplication.objects.filter(application_status='APPROVED')
