from django.contrib import admin
from .models.auxiliar import Auxiliar
from .models.clinicHistory import ClinicHistory
from .models.familiar import Familiar
from .models.medic import Medic
from .models.nurse import Nurse
from .models.patient import Patient
from .models.patientFamiliar import PatientFamiliar
from .models.user import User
from .models.suggestions import Suggestions
from .models.vitalSigns import VitalSigns

admin.site.register(Auxiliar)
admin.site.register(ClinicHistory)
admin.site.register(Familiar)
admin.site.register(Medic)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(PatientFamiliar)
admin.site.register(User)
admin.site.register(Suggestions)
admin.site.register(VitalSigns)
# Register your models here.
