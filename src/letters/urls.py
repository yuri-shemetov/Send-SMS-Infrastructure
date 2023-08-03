from letters.views import LetterModelViewSet
from rest_framework.routers import DefaultRouter


app_name = "letters"
# Create router and Registration ViewSet
router = DefaultRouter()
router.register(r"", LetterModelViewSet, basename="letters")
# URLs
urlpatterns = router.urls
