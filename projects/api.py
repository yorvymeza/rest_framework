from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

# Despues creamos una clase

class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	# queryset es la manera que nos va a decir que datos vas 
	# utilizar o que recurso vas a querer acceder de esta API
	 #Nos permite consultar todo los dato de una tabla
	permission_classes = [permissions.AllowAny]
	#AllowAny Cualquier aplicacion cliente va poder solitar datos a nuestro servidor
	#Pero afuturo se puede  cambiar con IsAuthenticated para las autentificaciones
	serializer_class = ProjectSerializer

	#Ahora debo crear una ruta para que los clientes puedan consultar 


# Crearemos un archivo de urls.py para  una ruta


# from projects.models import Project
# from rest_framework import viewsets, permissions
# from .serializers import ProjectSerializer

# class ProjectViewSet(viewsets.ModelViewSet):
#   queryset = Project.objects.all()
#   permission_classes = [permissions.AllowAny]
#   serializer_class = ProjectSerializer