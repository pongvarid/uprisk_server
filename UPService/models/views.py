from rest_framework.viewsets import ModelViewSet
from UPService.serializers import AgencyTypeSerializer, AgencySerializer, ProfileSerializer, YearSerializer, MissionSerializer, StrategicSerializer, StrategySerializer, RmPlanSerializer
from UPService.models import AgencyType, Agency, Profile, Year, Mission, Strategic, Strategy, RmPlan


class AgencyTypeViewSet(ModelViewSet):
    queryset = AgencyType.objects.order_by('pk')
    serializer_class = AgencyTypeSerializer


class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.order_by('pk')
    serializer_class = AgencySerializer


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


class RmPlanViewSet(ModelViewSet):
    queryset = RmPlan.objects.order_by('pk')
    serializer_class = RmPlanSerializer
