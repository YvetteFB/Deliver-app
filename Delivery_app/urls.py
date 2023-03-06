from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stores import views as stores_views
from wishlists import views as wishlists_views
from home import views as home_views

# Create a router and register viewsets with it
router = DefaultRouter()
router.register(r'stores', stores_views.StoreView, basename='stores')
router.register(r'wishlists', wishlists_views.WishlistView, basename='wishlists')
router.register(r'home', home_views.HomePage, basename='home')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
