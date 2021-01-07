from rest_framework.routers import SimpleRouter
from UPService.services import default_views as views


router = SimpleRouter()

router.register(r'agencytype', views.AgencyTypeViewSet)
router.register(r'agency', views.AgencyViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'year', views.YearViewSet)
router.register(r'mission', views.MissionViewSet)
router.register(r'strategic', views.StrategicViewSet)
router.register(r'strategy', views.StrategyViewSet)
router.register(r'rmplan', views.RmPlanViewSet)
router.register(r'sofceg', views.SOFCEGViewSet)
router.register(r'effectofrisk', views.EffectOfRiskViewSet)
router.register(r'riskrm', views.RiskRMViewSet)

urlpatterns = router.urls
