from django import forms
from.models import Team
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name','logo','description']
        widgets = {'name':forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':' Team name',
        }),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'rows': 4,
                'placeholder':' Description',
            }),
            'logo':forms.Textarea(attrs={
                'class':'form-control',
            }),
        }