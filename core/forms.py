from django import forms
from .models import Familia, TipoAyuda, Voluntario, Entrega, Seguimiento

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'

class TipoAyudaForm(forms.ModelForm):
    class Meta:
        model = TipoAyuda
        fields = '__all__'

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = '__all__'

class EntregaForm(forms.ModelForm):
    fecha_entrega = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Entrega
        fields = '__all__'

class SeguimientoForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Seguimiento
        fields = '__all__'
