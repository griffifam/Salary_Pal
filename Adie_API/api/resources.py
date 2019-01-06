from tastypie.resources import ModelResource
from api.models import Adie, Company, Offer


class AdieResource(ModelResource):
    class Meta:
        queryset = Adie.objects.all()
        resource_name = 'adie'

class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'

class OfferResource(ModelResource):
    class Meta:
        queryset = Offer.objects.all()
        resource_name = 'offer'
