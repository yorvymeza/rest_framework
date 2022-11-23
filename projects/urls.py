from rest_framework import routers
from .api import ProjectViewSet
# Este ProjectViewSet lo pasamos como parametro en
# en la ruta
router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls


#Despues debemos registrar esa ruta en mi
# archivo urls.py que se encuentra en el otro project 

