from django import forms
from .models import SpottedMessage

class SpottedMessageForm(forms.ModelForm):
    class Meta:
        model = SpottedMessage
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Ektib eli fi belek...',
                'class': 'message-input'
            })
        }
