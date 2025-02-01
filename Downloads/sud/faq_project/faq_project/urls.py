from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faqs.views import FAQViewSet, home

router = DefaultRouter()
router.register(r'faqs', FAQViewSet)

urlpatterns = [
    path('', home, name='home'),  # Add this line for the home page
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]