from rest_framework.serializers import ModelSerializer
from UPService.models import AgencyType, Agency, Profile, Year, Mission, Strategic, Strategy, RmPlan


class AgencyTypeSerializer(ModelSerializer):

    class Meta:
        model = AgencyType
        fields = '__all__'


class AgencySerializer(ModelSerializer):

    class Meta:
        model = Agency
        fields = '__all__'


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class YearSerializer(ModelSerializer):

    class Meta:
        model = Year
        fields = '__all__'


class MissionSerializer(ModelSerializer):

    class Meta:
        model = Mission
        fields = '__all__'


class StrategicSerializer(ModelSerializer):

    class Meta:
        model = Strategic
        fields = '__all__'


class StrategySerializer(ModelSerializer):

    class Meta:
        model = Strategy
        fields = '__all__'


class RmPlanSerializer(ModelSerializer):

    class Meta:
        model = RmPlan
        fields = '__all__'
