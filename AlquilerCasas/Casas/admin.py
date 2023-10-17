from django.contrib import admin
from .models import Casas
from .models import Personas
from .models import Alquiler
# Register your models here.
admin.site.register(Casas)
admin.site.register(Personas)
admin.site.register(Alquiler)