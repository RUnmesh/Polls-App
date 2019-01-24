from django import forms
from .models import question , choice

class QuesForm(forms.ModelForm) :

    class Meta :
        model = question
        fields = ('text',)


class ChoiceForm(forms.ModelForm) :
    
    class Meta :
        model = choice
        fields = ('text' ,)