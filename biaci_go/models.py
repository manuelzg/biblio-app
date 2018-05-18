from django.db import models

ESTADO_RECURSO = (
    ('P', 'Prestado'),
    ('B', 'Bloqueado'),
)

ESTADO_EJEMPLAR = (
    ('P', 'Prestado'),
    ('D', 'Disponible'),
)

SEXO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

ESTADO_USUARIO = (
    ('S', 'Suspendido'),
    ('B', 'Bloqueado'),
    ('I', 'Insolvente'),
)


# Create your models here.
class Recurso(models.Model):
    cota = models.CharField(max_length=15, primary_key=True)
    titulo = models.CharField(max_length=80)
    anio = models.IntegerField()
    idioma = models.CharField(max_length=15)
    lugar_publicacion = models.TextField()
    estado = models.CharField(max_length=1, choices=ESTADO_RECURSO)


class Biblioteca(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)
    estado = models.CharField(max_length=80)
    cuidad = models.CharField(max_length=80)
    avenida = models.CharField(max_length=80)
    calle = models.CharField(max_length=80)
    edificio = models.CharField(max_length=80)


class Ejemplar(models.Model):
    estado = models.CharField(max_length=1, choices=ESTADO_EJEMPLAR)
    cota_recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    codigo_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)


class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)


class Materia(models.Model):
    nombre = models.CharField(max_length=20)


class Revista(Recurso):
    numero = models.IntegerField()
    serie = models.CharField(max_length=10)


class Tesis(Recurso):
    autor = models.ManyToManyField(Autor)
    area = models.CharField(max_length=30)


class Libro(Recurso):
    autor = models.ManyToManyField(Autor)
    editorial = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)
    materia = models.ManyToManyField(Materia)


class Facultad(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)


class Escuela(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)
    codigo_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)


class Postgrado(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)
    codigo_escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)


class Doctorado(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)
    codigo_facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)


class Trabajador(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)


class Carrera(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=20)
    codigo_escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)


class Persona(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=SEXO)
    cod_area = models.IntegerField()
    num_telefono = models.IntegerField()
    correo = models.EmailField(max_length=70)
    direccion = models.TextField()
    postgrado = models.ManyToManyField(Postgrado)
    doctorado = models.ManyToManyField(Doctorado)
    trabajador = models.ManyToManyField(Trabajador)
    carrera = models.ManyToManyField(Carrera)


class Usuario(models.Model):
    usuario = models.CharField(max_length=20, primary_key=True)
    estado = models.CharField(max_length=1, choices=ESTADO_USUARIO)
    contrasenia = models.CharField(max_length=50)
    cedula_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)


class Consulta(models.Model):
    fecha = models.DateField()
    consulta_recurso = models.ManyToManyField(Recurso)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Prestamo(models.Model):
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    id_ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Reserva(models.Model):
    fecha_reserva = models.DateField()
    fecha_caducidad = models.DateField()
    id_ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)