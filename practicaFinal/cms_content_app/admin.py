from django.contrib import admin

# Register your models here.

from models import Contenidos
from models import Usuario
from models import FechaActualizacion
from models import Membership

admin.site.register(Contenidos)
admin.site.register(Usuario)
admin.site.register(FechaActualizacion)
admin.site.register(Membership)

