from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import Filter, FilterSet

from rest_framework.viewsets import ModelViewSet
from UPService.services.default_serializers import AgencyTypeSerializer, AgencySerializer, ProfileSerializer, YearSerializer, MissionSerializer, StrategicSerializer, StrategySerializer, RmPlanSerializer, SOFCEGSerializer, EffectOfRiskSerializer, RiskRMSerializer
from UPService.models import AgencyType, Agency, Profile, Year, Mission, Strategic, Strategy, RmPlan, SOFCEG, EffectOfRisk, RiskRM


def getData(request:any,params:str):
    try:
        return request.GET.get(params)
    except:
        return ""


class RMPlanRady(APIView):
    def get(self, request, format=None):
        rmPlan = RmPlan.objects.filter(year=getData(request,'year'),agency=getData(request, 'agency'))
        return Response({"rmplan_exists": rmPlan.exists()})


class ListFilter(Filter):
    def filter(self, qs, value):
        if not value:
            return qs

        # For django-filter versions < 0.13, use lookup_type instead of lookup_expr
        self.lookup_expr = 'in'
        values = value.split(',')
        return super(ListFilter, self).filter(qs, values)



class AccommodationFilter(FilterSet):
    ids = ListFilter(name='id')

    class Meta:
        model = Strategy
        fields = ['ids',]

class StrategyViewSet(ModelViewSet):
    queryset = Strategy.objects.order_by('pk')
    serializer_class = StrategySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AccommodationFilter