from rest_framework.serializers import ModelSerializer
from UPService.models import AgencyType, Agency, Profile, Year, Mission, Choice, RmPlan, RiskRM


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


class ChoiceSerializer(ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class RmPlanSerializer(ModelSerializer):

    class Meta:
        model = RmPlan
        fields = '__all__'


class RiskRMSerializer(ModelSerializer):

    class Meta:
        model = RiskRM
        fields = '__all__'
