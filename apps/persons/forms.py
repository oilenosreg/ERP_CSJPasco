from datetime import date, datetime
from django import forms

# Project modules.
from apps.main.modules.dates import calcular_edad, menor_edad
from apps.main.modules.strings import caracteres_alfabeticos, caracteres_numericos

# App modules.
from .models import Persona


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = 'persona/imageField.html'

class CreatePersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'dni', 'nombres', 'apellido_paterno',
            'apellido_materno', 'fecha_nacimiento',
            'genero', 'estado_civil', 
            'observaciones', 'foto',
            'correo_institucional', 'correo_personal', 
            'telefono_principal', 'telefono_secundario',
            'anexo_institucional',          
            'direccion', 'activo',
        ]
        labels = {
            'dni': 'DNI',
            'nombres': 'Nombres',
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'genero': 'Género',
            'estado_civil': 'Estado civil',
            'observaciones': 'Observaciones',
            'foto': 'Fotografía',
            'correo_institucional': 'Correo institucional',
            'correo_personal': 'Correo personal',
            'telefono_principal': 'Teléfono principal',
            'telefono_secundario': 'Teléfono secundario',
            'anexo_institucional': 'Anexo telefónico',
            'direccion': 'Dirección'            
        }
        help_texts = {
            'estado_civil': 'Estado civil.'
        }
        widgets = {
            'dni': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de DNI',
                    'name':'dni',
                    # 'id': 'dni',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombres',
                    'name': 'nombres',
                }
            ),
            'apellido_paterno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido Paterno',
                    'name': 'apellido_paterno',
                }
            ),
            'apellido_materno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido Materno',
                    'name': 'apellido_materno',
                }
            ),

            # TODO: El campo debería se con DateInput, evaluar y probar con otros
            # plugins de datepicker.

            'fecha_nacimiento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de nacimiento',                
                    'id': 'fecha_nacimiento',                    
                    'type': 'date',
                    # 'value': datetime.now().strftime('%d / %m / %Y'),
                }
            ),
            'genero': forms.Select(
                attrs={
                    'class': 'form-control',
                    'name': 'genero',
                }
            ),
            'estado_civil': forms.Select(
                attrs={
                    'class': 'form-control',
                    'name': 'estado_civil',                    
                }
            ),
            'observaciones': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'name': 'observaciones',
                    'rows': 3,
                }
            ),
            'correo_institucional': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'correo_institucional',
                    'placeholder': 'alguien@pj.gob.pe'
                }
            ),
            'correo_personal': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'correo_personal',
                    'placeholder': 'alguien@gmail.com'
                }                
            ),
            'telefono_principal': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'telefono_principal',
                    'placeholder': '063597100'
                }                  
            ),
            'telefono_secundario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'telefono_secundario',
                    'placeholder': '987654321'
                }                  
            ),
            'anexo_institucional': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'anexo_institucional',
                    'placeholder': '47001'
                }                  
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'direccion',
                    'placeholder': 'Jr. 28 de julio S/N - San Juan - Yanacancha - Pasco'
                }                  
            ),
        }

    def __init__(self, *args, **kwargs):
        super(CreatePersonaForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.dni:
            self.fields['dni'].widget.attrs['readonly'] = True

    # Validaciones.
    def clean_dni(self):
        '''
        Valida que el número de DNI tenga ocho (8) dígitos.
        '''
        dni = self.cleaned_data['dni']
        # instance = getattr(self, 'instance', None)
        # if instance and instance.dni:            
        #     raise forms.ValidationError(
        #         '''
        #         No se puede modificar el DNI en este punto, usted está tratando
        #         de alterar el sistema.
        #         Se registrarán sus datos de acceso para ser auditados.
        #         ''')
        #     # return instance.dni
        # else:
        #     dni = self.cleaned_data['dni']
        #     print('=========================')

        if dni is not None and not caracteres_numericos(dni):
            raise forms.ValidationError(
                '''
                El número de DNI solo debe contener caracteres numéricos.
                ''')
        elif len(dni) > 8 or len(dni) < 8:
            raise forms.ValidationError(
                '''
                El número de DNI debe tener ocho (8) dígitos.
                ''')
        return dni

    def clean_nombres(self):
        nombres = self.cleaned_data['nombres']
        if not caracteres_alfabeticos(nombres):
            raise forms.ValidationError(
                '''
                Los nombres solo deben contener caracteres alfabéticos 
                (A-Z/a-z).
                ''')
        return nombres

    def clean_apellido_paterno(self):
        ap_pat = self.cleaned_data['apellido_paterno']
        if not caracteres_alfabeticos(ap_pat):
            raise forms.ValidationError(
                '''
                El apellido paterno solo deben contener caracteres 
                alfabéticos (A-Z/a-z).
                ''')
        return ap_pat

    def clean_apellido_materno(self):
        ap_mat = self.cleaned_data['apellido_materno']
        if not caracteres_alfabeticos(ap_mat):
            raise forms.ValidationError(
                '''
                El apellido materno solo deben contener caracteres 
                alfabéticos (A-Z/a-z).
                ''')
        return ap_mat

    def clean_fecha_nacimiento(self):
        '''
        Valida que la edad de la persona sea mayor a 18 años.
        '''        
        fn = self.cleaned_data['fecha_nacimiento']
        hoy = date.today()

        if fn is not None and fn >= hoy:
            raise forms.ValidationError('La fecha de nacimiento no puede ser igual o mayor a la fecha de hoy.')
        elif fn is not None:
            edad = calcular_edad(fn)
            if menor_edad(edad):
                raise forms.ValidationError('La persona es menor de edad, no podrá ser registrada.')
        return fn

    def clean_telefono_principal(self):
        telefono = self.cleaned_data['telefono_principal']
        if telefono is not None and not caracteres_numericos(telefono):
            raise forms.ValidationError('El número telefónico debe contener caracteres numéricos (0-9).')
        elif telefono is not None and len(telefono) < 9:
            raise forms.ValidationError('El número telefónico debe tener más de ocho (8) dígitos.')            
        return telefono

    def clean_telefono_secundario(self):
        telefono = self.cleaned_data['telefono_secundario']
        if telefono is not None and not caracteres_numericos(telefono):
            raise forms.ValidationError('El número telefónico debe contener caracteres numéricos (0-9).')
        elif telefono is not None and len(telefono) < 9:
            raise forms.ValidationError('El número telefónico debe tener más de ocho (8) dígitos.')            
        return telefono

    def clean_anexo_institucional(self):
        anexo = self.cleaned_data['anexo_institucional']
        if anexo is not None and not caracteres_numericos(anexo):
            raise forms.ValidationError('El número de anexo debe contener caracteres numéricos (0-9).')
        return anexo        