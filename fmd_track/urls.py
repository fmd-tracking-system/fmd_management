from django.conf.urls import url, include
from django.contrib import admin
from fmd import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'farm', views.FarmViewSet)
router.register(r'fmddata', views.FmdDataViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
