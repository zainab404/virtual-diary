from django import forms
from diary_app.models import DiaryEntry
from django.contrib.auth.models import User

class NewEntryForm(forms.ModelForm):
    class Meta():
        model = DiaryEntry
        fields = ('title','text',)
        widgets = {
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password')