from .views import TestViewSet,PetsViewSet,UserDetails,GenericAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register('test', TestViewSet, basename='test')
router.register('petsdetails', PetsViewSet, basename='petsdetails')
router.register('pets', UserDetails, basename='pets')

urlpatterns =[
    path('', include(router.urls)),
    ]



#
# urlpatterns = [
#     path('',TestViewSet.as_view()),
#     path('<pk>',TestViewSet.as_view())
# ]