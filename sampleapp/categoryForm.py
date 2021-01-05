
from django import forms
from .models import category, subcategory



class CategoryForm(forms.Form):

    categories = forms.ModelChoiceField(queryset=category.objects.all(), error_messages={'required': 'Role field is required.'},
                                 empty_label='Select categories', label='Categories',
                                 widget=forms.Select(attrs={'class': 'form-control', 'id': "categories_id"}))

    subcategory = forms.ModelChoiceField(queryset=subcategory.objects.all().exclude(isactive=1), empty_label='Select subcategory',
                                   error_messages={'required': 'Branch field is required.'},
                                   required=True, label='Subcategory',
                                   widget=forms.Select(attrs={'class': 'form-control', 'id': "subcategory_id"}))


