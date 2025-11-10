from rest_framework import serializers
from .models import Familia, TipoAyuda, Voluntario, Entrega, Seguimiento

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = '__all__'

class TipoAyudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAyuda
        fields = '__all__'

class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntario
        fields = '__all__'

class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = '__all__'

class SeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = '__all__'
