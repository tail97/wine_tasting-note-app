
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Tastingnote


class TastingForm(forms.ModelForm):
    class Meta:
        model= Tastingnote
        fields = ['title', 'author', 'content', 'head_image']
        widgets = {
            'content': SummernoteWidget(attrs={
                'summernote': {
                    'width': '100%',
                    'height': '400px',
                    'iframe': False,
                    'lang': 'ko-KR',
                    'codemirror': {'mode': 'htmlmixed'},
                }
            })
        }
