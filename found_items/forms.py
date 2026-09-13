from django import forms
from .models import ReportFoundItem

class ReportFoundItemForm(forms.ModelForm):
    class Meta:
        model = ReportFoundItem
        exclude = ["user"]

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter found item name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the found item...',
                'rows': 5,
            }),
            'date_found': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'location_found': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Where did you found it?',
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
            'item_name': 'Found Item Name',   
            'type': 'Item Type',
            'description': 'Description',
            'category': 'Category',
            'date_found': 'Date Found',
            'location_found': 'Location Found',
            'contact_info': 'Contact Information',
            'image': 'Image',
        }