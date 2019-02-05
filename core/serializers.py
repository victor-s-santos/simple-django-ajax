from rest_framework.serializers import ModelSerializer
from core.models import Perguntas

class PerguntasSerializer(ModelSerializer):
	class Meta:
		model = Perguntas
		fields = '__all__'