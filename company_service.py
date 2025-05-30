from esgapp.models import Company

class CompanyService:
    @staticmethod
    def create_company(data):
        # Add any custom validation here if needed
        return Company.objects.create(**data)

    @staticmethod
    def get_all_companies():
        return Company.objects.all()
