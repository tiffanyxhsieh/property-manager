from housing_application.models import HousingApplication


def get_property_history(self):
    HousingApplication.objects.filter(property=self, application_status='APPROVED')