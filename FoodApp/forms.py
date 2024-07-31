from django import forms
from .models import Items
# models means database in django
class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']