from django import forms

# App modules.
from .models import Categoria, Marca, Modelo, Equipo, EquipoAsignado


class CreateEquipmentForm(forms.ModelForm):
    class Meta: 
        model = Equipo
        fields = '__all__'
        widgets = {
            'componente_de': forms.Select(
                attrs={
                    'class': 'form-control',
                }                
            ),            
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'marca': forms.Select(
                attrs={
                    'class': 'form-control',
                }                
            ),            
            'modelo': forms.Select(
                attrs={
                    'class': 'form-control',
                }                
            ),
            'serie': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }                
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                }                
            ),
            'condicion': forms.Select(
                attrs={
                    'class': 'form-control',
                }                
            ),
            'ip': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }                
            ),
            'mac': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }                
            ),            
            'cod_patrimonial': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }                
            ),
            'orden_compra': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }                
            ),

            'observaciones': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }                
            ),
        }

'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)    
        self.fields['modelo'].queryset = Modelo.objects.none()

        
        if 'marca' in self.data:
            print('================>')
            print(f'SELF.DATA: {self.data}')
            print(f'MARCA:' + 'marca')
            try:
                marca_id = int(self.data.get('marca'))
                self.fields['modelo'].queryset = Modelo.objects.filter(
                    marca_id = marca_id
                )
                print(f'MARCA_ID: {marca_id}')
            except (ValueError, TypeError):
                pass
        elif self.instance.id:
            print(f'self.instance.id: {self.instance.id}')
            self.fields['modelo'].queryset = self.instance.marca.modelo_set.order_by('nombre')
'''