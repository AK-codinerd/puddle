from django import forms
from .models import Item

class_input = "w-full py-4 px-6 rounded-xl border"


# this is the form for uploading a new item and model is also Item as we are taking the details of the item
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        # here you can do the same as core/forms or do like this too
        widgets = {
            "category": forms.Select(attrs={
                'class': class_input
            }),
            "name": forms.TextInput(attrs={
                'class': class_input
            }),
            "description": forms.Textarea(attrs={
                'class': class_input
            }),
            "price": forms.TextInput(attrs={
                'class': class_input
            }),
            "image": forms.FileInput(attrs={
                'class': class_input
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        # here you can do the same as core/forms or do like this too
        widgets = {
            "is_sold": forms.Select(attrs={
                'class': class_input
            }),
            "name": forms.TextInput(attrs={
                'class': class_input
            }),
            "description": forms.Textarea(attrs={
                'class': class_input
            }),
            "price": forms.TextInput(attrs={
                'class': class_input
            }),
            "image": forms.FileInput(attrs={
                'class': class_input
            })
        }


    