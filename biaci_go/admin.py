from django.contrib import admin

from .models import Recurso
from .models import Biblioteca
from .models import Ejemplar
from .models import Autor
from .models import Materia
from .models import Revista
from .models import Tesis
from .models import Libro
from .models import Facultad
from .models import Escuela
from .models import Postgrado
from .models import Doctorado
from .models import Trabajador
from .models import Carrera
from .models import Persona
from .models import Usuario
from .models import Consulta
from .models import Prestamo
from .models import Reserva


admin.site.register(Recurso)
admin.site.register(Biblioteca)
admin.site.register(Ejemplar)
admin.site.register(Autor)
admin.site.register(Materia)
admin.site.register(Revista)
admin.site.register(Tesis)
admin.site.register(Libro)
admin.site.register(Facultad)
admin.site.register(Escuela)
admin.site.register(Postgrado)
admin.site.register(Doctorado)
admin.site.register(Trabajador)
admin.site.register(Carrera)
admin.site.register(Persona)
admin.site.register(Usuario)
admin.site.register(Consulta)
admin.site.register(Prestamo)
admin.site.register(Reserva)
