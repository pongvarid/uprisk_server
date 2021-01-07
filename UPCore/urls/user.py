
from UPCore.api.user import general
from django.urls import include, path

urlpatterns = [
    path('check/rmplan/',  general.RMPlanRady.as_view()),
    path('check/strategy/', general.StrategyViewSet.as_view({'get': 'list'})),
]