
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from UPService.services.default_serializers import AgencyTypeSerializer, AgencySerializer, ProfileSerializer, YearSerializer, MissionSerializer, StrategicSerializer, StrategySerializer, RmPlanSerializer, SOFCEGSerializer, EffectOfRiskSerializer, RiskRMSerializer
from UPService.models import AgencyType, Agency, Profile, Year, Mission, Strategic, Strategy, RmPlan, SOFCEG, EffectOfRisk, RiskRM


class AgencyTypeViewSet(ModelViewSet):
    queryset = AgencyType.objects.order_by('pk')
    serializer_class = AgencyTypeSerializer


class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.order_by('pk')
    serializer_class = AgencySerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filterset_fields = ['agency_type',]
    search_fields = ['name',]

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.order_by('pk')
    serializer_class = ProfileSerializer


class YearViewSet(ModelViewSet):
    queryset = Year.objects.order_by('pk')
    serializer_class = YearSerializer


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.order_by('pk')
    serializer_class = MissionSerializer


class StrategicViewSet(ModelViewSet):
    queryset = Strategic.objects.order_by('pk')
    serializer_class = StrategicSerializer


class StrategyViewSet(ModelViewSet):
    queryset = Strategy.objects.order_by('pk')
    serializer_class = StrategySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency','agency', ]

class RmPlanViewSet(ModelViewSet):
    queryset = RmPlan.objects.order_by('pk')
    serializer_class = RmPlanSerializer


class SOFCEGViewSet(ModelViewSet):
    queryset = SOFCEG.objects.order_by('pk')
    serializer_class = SOFCEGSerializer


class EffectOfRiskViewSet(ModelViewSet):
    queryset = EffectOfRisk.objects.order_by('pk')
    serializer_class = EffectOfRiskSerializer


class RiskRMViewSet(ModelViewSet):
    queryset = RiskRM.objects.order_by('pk')
    serializer_class = RiskRMSerializer
