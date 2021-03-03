from rest_framework.routers import SimpleRouter
from UPService.services import views


router = SimpleRouter()

router.register(r'agencytype', views.AgencyTypeViewSet)
router.register(r'agency', views.AgencyViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'year', views.YearViewSet)
router.register(r'mission', views.MissionViewSet)
router.register(r'choice', views.ChoiceViewSet)
router.register(r'rmplan', views.RmPlanViewSet)
router.register(r'riskrm', views.RiskRMViewSet)
router.register(r'plan/all', views.RmPlanAllViewSet)
urlpatterns = router.urls
