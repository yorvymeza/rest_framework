from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('__all__')
		# fields = ('id', 'title', 'description', 'technology', 'created_at')
		read_only_fields = ('created_at', ) # ('created_at', ) 
		# Se debe colocar una coma ya que si no lo lee como un string
		# Ya que esto debería ser una tupla

		# Me va permitir el campo created_at no se modifique
        
# Ahora vamos a crear un viewset 
# El viewSet nos va a decir que podra consultar esto

