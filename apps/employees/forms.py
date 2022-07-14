from django import forms

# App modules.
from .models import Empleado



class CreateEmpleadoForm(forms.ModelForm):
    # cargo = forms.ModelChoiceField(empty_label='› Seleccione un cargo', queryset=Cargo.objects.all())
    # inicio = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'])
    # activo = forms.BooleanField(required=True)
    class Meta:
        model = Empleado
        fields = '__all__'
        exclude = ('distrito', 'persona', 'escalafon', 'remuneracion')
        labels = {
            'documento_designacion': 'Documento de designación'
        }
        widgets = {
            'sede': forms.Select(
                attrs={
                    'class': 'form-control ',
                    'style': 'width: 100%',
                },
            ),
            'modulo': forms.Select(
                attrs={
                    'class': 'form-control ',
                    'style': 'width: 100%',
                    # 'data_modulos_url': reverse_lazy('empleado:ajax_cargar_modulos'),
                },
            ),
            'edificio': forms.Select(
                attrs={
                    'class': 'form-control ',
                    'style': 'width: 100%',
                    # 'data-live-search':"true",
                },
            ),
            'cargo': forms.Select(
                attrs={
                    'class': 'form-control ',
                    'style': 'width: 100%',
                    # 'data-live-search':"true",
                },
            ),
            'dependencia': forms.Select(            
                attrs={
                    'class': 'form-control ',
                    'style': 'width: 100%;',
                    # 'data-live-search':"true",
                },
            ),  
            'inicio': forms.DateInput(                
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Inicio del cargo',
                    'type': 'date',
                    # 'value':datetime.now().strftime('%d/%m/%Y'),
                    # 'id': 'inicio'
                },
            ), 
            'cese': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    # 'value': datetime.now().strftime('%d/%m/%Y'),
                    'placeholder':'Cese al cargo',
                    'type': 'date',
                },
            ),             
            'documento_designacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Memorando N° 001-2022-CSJPA-PJ'
                },
            ),  
            'observaciones': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'name': 'observaciones',
                    'rows': 4,
                }  
            ),
            'activo': forms.CheckboxInput(
                # attrs={
                #     'class': 'form-control',
                # }
            ),                                                                   
        }
    # def __init__(self, *args, **kwargs):
    #     print('>>>>>>>>>>>>>>>>')
       
    #     super().__init__(*args, **kwargs)
    #     self.fields['dependencia'].queryset = Dependencia.objects.none()


    #     if 'sede' in self.data:
    #         try:
    #             sede_id = int(self.data.get('sede'))
    #             self.fields['dependencia'].queryset = Dependencia.objects.filter(
    #                 sede_id = sede_id
    #             ).order_by('nombre')
    #         except (ValueError, TypeError):
    #             print(f'Errores ===>: {ValueError} {TypeError}')
    #     elif self.instance.id:
    #         self.fields['dependencia'].queryset = self.instance.sede.dependencia_set.order_by('nombre')
    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('inicio')
        cese = cleaned_data.get('cese')
        activo = cleaned_data.get('activo')
        if cese:
            if cese < inicio:
                raise forms.ValidationError(
                    'La fecha de cese del cargo no puede \
                    ser menor a la fecha de inicio de la designación.'
                )
            if cese and activo:
                raise forms.ValidationError(
                    'Una designación no puede estar activa \
                    si tiene fecha de cese al cargo.'
                )
        elif cese is None and activo is False:
            raise forms.ValidationError(
                'Una designación debe estar activa \
                si no tiene fecha de cese al cargo.'
            )
