from clients.views import PageModelViewSet
from rest_framework.routers import DefaultRouter


app_name = "clients"
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r"", PageModelViewSet, basename="clients")
# URLs
urlpatterns = router.urls
