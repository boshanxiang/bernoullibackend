from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'naturalpersons', views.NaturalPersonViewSet)
router.register(r'legalentities', views.LegalEntityViewSet)
router.register(r'equityclasses', views.EquityClassViewSet)
router.register(r'equitytokens', views.EquityTokenViewSet)
router.register(r'employmentrelations', views.EmploymentRelationViewSet)
router.register(r'officerrelations', views.OfficerRelationViewSet)
router.register(r'directorrelations', views.DirectorRelationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]