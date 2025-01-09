from django import forms
from fbvCRUDAssignmentApp import models

class COurseForm(forms.ModelForm):
    class Meta:
        model= models.Course
        fields='__all__'