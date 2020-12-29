from django import forms
from diary_app.models import DiaryEntry

class NewEntryForm(forms.ModelForm):
    class Meta():
        model = DiaryEntry
        fields = ('text',)
        widgets = {
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
    