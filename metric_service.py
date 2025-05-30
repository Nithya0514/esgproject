from esgapp.models import Metric

class MetricService:
    @staticmethod
    def create_metric(data):
        # Could add duplicate check here if needed
        return Metric.objects.create(**data)

    @staticmethod
    def get_metrics_by_business_unit(unit_id):
        return Metric.objects.filter(business_unit_id=unit_id)
