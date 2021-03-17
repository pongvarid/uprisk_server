from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from UPService.services.serializers import AgencyTypeSerializer, AgencySerializer, ProfileSerializer, YearSerializer, \
    MissionSerializer, ChoiceSerializer, RmPlanSerializer, RiskRMSerializer, RmPlanAllSerializer, RiskRM6Serializer, RiskRM12Serializer
from UPService.models import AgencyType, Agency, Profile, Year, Mission, Choice, RmPlan, RiskRM, RiskRMR6 , RiskRMR12
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.response import Response


class AgencyTypeViewSet(ModelViewSet):
    queryset = AgencyType.objects.order_by('pk')
    serializer_class = AgencyTypeSerializer


class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.order_by('pk')
    serializer_class = AgencySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['agency_type', ]
    search_fields = ['name', ]


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.order_by('pk')
    serializer_class = ProfileSerializer


class YearViewSet(ModelViewSet):
    queryset = Year.objects.order_by('pk')
    serializer_class = YearSerializer


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.order_by('pk')
    serializer_class = MissionSerializer


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.order_by('pk')
    serializer_class = ChoiceSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['name', ]
    search_fields = ['value', ]


class RmPlanViewSet(ModelViewSet):
    queryset = RmPlan.objects.order_by('pk')
    serializer_class = RmPlanSerializer


class RiskRMViewSet(ModelViewSet):
    queryset = RiskRM.objects.order_by('pk')
    serializer_class = RiskRMSerializer

class RmPlanAllViewSet(ModelViewSet):
    queryset = RmPlan.objects.order_by('pk')
    serializer_class = RmPlanAllSerializer

class RiskRM6ViewSet(ModelViewSet):
    queryset = RiskRMR6.objects.order_by('pk')
    serializer_class = RiskRM6Serializer

class RiskRM12ViewSet(ModelViewSet):
    queryset = RiskRMR12.objects.order_by('pk')
    serializer_class = RiskRM12Serializer