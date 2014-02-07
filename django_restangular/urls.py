from apps.restangular.models import Item
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .routers import CustomRouter


# REST framework routes
class ItemViewSet(viewsets.ModelViewSet):
    model = Item

router = CustomRouter()
router.register(r'items', ItemViewSet)


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^', include(router.urls)),
)
