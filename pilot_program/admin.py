from django.contrib import admin

from pilot_program.models import PilotProgram, Task

# Register your models here.
admin.site.register(PilotProgram)
admin.site.register(Task)
