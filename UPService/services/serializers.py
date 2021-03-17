from rest_framework.serializers import ModelSerializer,SerializerMethodField
from UPService.models import AgencyType, Agency, Profile, Year, Mission, Choice, RmPlan, RiskRM, RiskRMR6 , RiskRMR12


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

class RiskRM6Serializer(ModelSerializer):

    class Meta:
        model = RiskRMR6
        fields = '__all__'


class RiskRM12Serializer(ModelSerializer):

    class Meta:
        model = RiskRMR12
        fields = '__all__'

class RmPlanAllSerializer(ModelSerializer):
    risk = SerializerMethodField()
    mission = MissionSerializer()
    r6 =  SerializerMethodField()
    r12 = SerializerMethodField()
    class Meta:
        model = RmPlan
        fields = '__all__'

    def get_risk(self,obj):
        try:
            risk = RiskRM.objects.get(rm_plan=obj.id)
            risk = RiskRMSerializer(risk).data
            return risk 
        except: 
            return None
        
    
    def get_r6(self,obj):
        try:
            risk = RiskRMR6.objects.get(rm_plan=obj.id)
            risk = RiskRM6Serializer(risk).data
            return risk
        except:
            return None 
        

    def get_r12(self,obj):
        try: 
            risk = RiskRMR12.objects.get(rm_plan=obj.id)
            risk = RiskRM12Serializer(risk).data
            return risk
        except: 
            return None 
        