from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from UPService.services.default_serializers import AgencyTypeSerializer, AgencySerializer, ProfileSerializer, YearSerializer, MissionSerializer, StrategicSerializer, StrategySerializer, RmPlanSerializer, SOFCEGSerializer, EffectOfRiskSerializer, RiskRMSerializer
from UPService.models import AgencyType, Agency, Profile, Year, Mission, Strategic, Strategy, RmPlan, SOFCEG, EffectOfRisk, RiskRM


class AgencyTypeAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = AgencyType.objects.get(pk=id)
            serializer = AgencyTypeSerializer(item)
            return Response(serializer.data)
        except AgencyType.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = AgencyType.objects.get(pk=id)
        except AgencyType.DoesNotExist:
            return Response(status=404)
        serializer = AgencyTypeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = AgencyType.objects.get(pk=id)
        except AgencyType.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AgencyTypeAPIListView(APIView):

    def get(self, request, format=None):
        items = AgencyType.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AgencyTypeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AgencyTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AgencyAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Agency.objects.get(pk=id)
            serializer = AgencySerializer(item)
            return Response(serializer.data)
        except Agency.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Agency.objects.get(pk=id)
        except Agency.DoesNotExist:
            return Response(status=404)
        serializer = AgencySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Agency.objects.get(pk=id)
        except Agency.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AgencyAPIListView(APIView):

    def get(self, request, format=None):
        items = Agency.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AgencySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AgencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProfileAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
            serializer = ProfileSerializer(item)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response(status=404)
        serializer = ProfileSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Profile.objects.get(pk=id)
        except Profile.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProfileAPIListView(APIView):

    def get(self, request, format=None):
        items = Profile.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class YearAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Year.objects.get(pk=id)
            serializer = YearSerializer(item)
            return Response(serializer.data)
        except Year.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Year.objects.get(pk=id)
        except Year.DoesNotExist:
            return Response(status=404)
        serializer = YearSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Year.objects.get(pk=id)
        except Year.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class YearAPIListView(APIView):

    def get(self, request, format=None):
        items = Year.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = YearSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = YearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MissionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Mission.objects.get(pk=id)
            serializer = MissionSerializer(item)
            return Response(serializer.data)
        except Mission.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Mission.objects.get(pk=id)
        except Mission.DoesNotExist:
            return Response(status=404)
        serializer = MissionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Mission.objects.get(pk=id)
        except Mission.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class MissionAPIListView(APIView):

    def get(self, request, format=None):
        items = Mission.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = MissionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = MissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StrategicAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Strategic.objects.get(pk=id)
            serializer = StrategicSerializer(item)
            return Response(serializer.data)
        except Strategic.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Strategic.objects.get(pk=id)
        except Strategic.DoesNotExist:
            return Response(status=404)
        serializer = StrategicSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Strategic.objects.get(pk=id)
        except Strategic.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class StrategicAPIListView(APIView):

    def get(self, request, format=None):
        items = Strategic.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = StrategicSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = StrategicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StrategyAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Strategy.objects.get(pk=id)
            serializer = StrategySerializer(item)
            return Response(serializer.data)
        except Strategy.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Strategy.objects.get(pk=id)
        except Strategy.DoesNotExist:
            return Response(status=404)
        serializer = StrategySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Strategy.objects.get(pk=id)
        except Strategy.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class StrategyAPIListView(APIView):

    def get(self, request, format=None):
        items = Strategy.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = StrategySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = StrategySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RmPlanAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = RmPlan.objects.get(pk=id)
            serializer = RmPlanSerializer(item)
            return Response(serializer.data)
        except RmPlan.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = RmPlan.objects.get(pk=id)
        except RmPlan.DoesNotExist:
            return Response(status=404)
        serializer = RmPlanSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = RmPlan.objects.get(pk=id)
        except RmPlan.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RmPlanAPIListView(APIView):

    def get(self, request, format=None):
        items = RmPlan.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RmPlanSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RmPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SOFCEGAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = SOFCEG.objects.get(pk=id)
            serializer = SOFCEGSerializer(item)
            return Response(serializer.data)
        except SOFCEG.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = SOFCEG.objects.get(pk=id)
        except SOFCEG.DoesNotExist:
            return Response(status=404)
        serializer = SOFCEGSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = SOFCEG.objects.get(pk=id)
        except SOFCEG.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SOFCEGAPIListView(APIView):

    def get(self, request, format=None):
        items = SOFCEG.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = SOFCEGSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SOFCEGSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EffectOfRiskAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = EffectOfRisk.objects.get(pk=id)
            serializer = EffectOfRiskSerializer(item)
            return Response(serializer.data)
        except EffectOfRisk.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = EffectOfRisk.objects.get(pk=id)
        except EffectOfRisk.DoesNotExist:
            return Response(status=404)
        serializer = EffectOfRiskSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = EffectOfRisk.objects.get(pk=id)
        except EffectOfRisk.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class EffectOfRiskAPIListView(APIView):

    def get(self, request, format=None):
        items = EffectOfRisk.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = EffectOfRiskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = EffectOfRiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class RiskRMAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = RiskRM.objects.get(pk=id)
            serializer = RiskRMSerializer(item)
            return Response(serializer.data)
        except RiskRM.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = RiskRM.objects.get(pk=id)
        except RiskRM.DoesNotExist:
            return Response(status=404)
        serializer = RiskRMSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = RiskRM.objects.get(pk=id)
        except RiskRM.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class RiskRMAPIListView(APIView):

    def get(self, request, format=None):
        items = RiskRM.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = RiskRMSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RiskRMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
