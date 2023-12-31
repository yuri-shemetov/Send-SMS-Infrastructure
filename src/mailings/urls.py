from mailings.views import MailingViewSet
from rest_framework.routers import DefaultRouter


app_name = "mailings"
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r"", MailingViewSet, basename="mailings")
# URLs
urlpatterns = router.urls
