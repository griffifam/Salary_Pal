from tastypie.resources import ModelResource
from api.models import Adie, Company, Offer
from tastypie.authorization import Authorization


class AdieResource(ModelResource):
    class Meta:
        queryset = Adie.objects.all()
        resource_name = 'adie'
        authorization = Authorization()

class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'
        authorization = Authorization()

class OfferResource(ModelResource):
    class Meta:
        queryset = Offer.objects.all()
        resource_name = 'offer'
        authorization = Authorization()
