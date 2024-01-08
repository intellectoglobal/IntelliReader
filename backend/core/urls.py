from .views import DocPost
from rest_framework.routers import DefaultRouter

app_name = "core"

router = DefaultRouter()
router.register('', DocPost, basename = 'document')
urlpatterns = router.urls