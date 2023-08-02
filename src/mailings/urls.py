from mailings.views import CreateMailingViewSet
from rest_framework.routers import DefaultRouter


app_name = "mailings"
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r"", CreateMailingViewSet, basename="mailings")
# URLs
urlpatterns = router.urls
