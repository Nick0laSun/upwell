from django import forms

class SourceForm(forms.Form):
    search_field = forms.CharField(
        label="Author/Title",
        label_suffix=": ",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Enter Author's name or Title"
            }
        )
    )