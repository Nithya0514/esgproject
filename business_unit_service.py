from esgapp.models import BusinessUnit

class BusinessUnitService:
    @staticmethod
    def create_unit(data):
        return BusinessUnit.objects.create(**data)

    @staticmethod
    def list_units_by_company(company_id):
        return BusinessUnit.objects.filter(company_id=company_id)
