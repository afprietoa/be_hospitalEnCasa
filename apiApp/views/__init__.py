from .userView import UserListView, UserRetrieveUpdateDeleteView
from .patientView import PatientListCreateView, PatientRetrieveUpdateView
from .familiarView import FamiliarListCreateView, FamiliarRetrieveUpdateView
from .medicView import MedicListCreateView, MedicRetrieveUpdateView
from .nurseView import NurseListCreateView, NurseRetrieveUpdateView
from .auxiliarView import AuxiliarListCreateView, AuxiliarRetrieveUpdateView

from .medicPatientView import createMedicPatient , detailMedicPatient
from .patientFamiliarView import createPatientFamiliar , detailPatientFamiliar
from .clinicHistoryView import ClinicHistoryCreateView , ClinicHistoryRetrieveUpdateDestroyView
# from .vitalSignsView import createVitalSigns , detailVitalSigns
# from .suggestionsView import createSuggestions , detailSuggestions