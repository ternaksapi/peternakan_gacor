from django.forms import ModelForm, Textarea
from main.models import Items

class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'amount', 'description']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget = Textarea(attrs={'class': 'form-control'})