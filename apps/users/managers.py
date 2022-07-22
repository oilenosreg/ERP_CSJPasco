from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    '''
    Manejador de usuarios personalizados.
    El número de DNI es el identificador único, en lugar del nombre de usuario.
    '''

    def create_user(self, dni, password, **extra_fields):
        '''
        Crea y guarda un usuario con su número de DNI.
        '''
        if not dni:
            raise ValueError('El número de DNI es obligatorio para registrar a un usuario')

        user = self.model(dni = dni, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, dni, password, **extra_fields):
        '''
        Crea y guarda un super usuario en base a su número de DNI y clave.
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe pertenecer al grupo de administradores.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe estar habilitado en el sistema.')
        return self.create_user(dni, password, **extra_fields)
