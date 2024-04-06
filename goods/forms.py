from django import forms
from .models import Supply, Size, Color, Category

class SupplyAddForm(forms.ModelForm):

    class Meta:
        model = Supply
        fields = ['id', 'image', 'category', 'title', 'color_to_str', 'size_to_str', 'status', 'count', 'description']

        
class CategoryAddForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['id', 'parent', 'title', 'status']

class ColorAddForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ['name']

class SizeAddForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ['name']

