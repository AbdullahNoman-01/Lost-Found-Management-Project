from django import forms
from .models import ReportLostItem

class ReportLostItemForm(forms.ModelForm):
    class Meta:
        model = ReportLostItem
        fields = ['item_name','type', 'description', 'category', 'date_lost', 'location_lost', 'contact_info', 'image']

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter lost item name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the lost item...',
                'rows': 5,
            }),
            'date_lost': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'location_lost': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Where did you lose it?',
            }),
            'contact_info': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone or email',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'item_name': 'Lost Item Name',   
            'type': 'Item Type',
            'description': 'Description',
            'category': 'Category',
            'date_lost': 'Date Lost',
            'location_lost': 'Location Lost',
            'contact_info': 'Contact Information',
            'image': 'Image',
        }