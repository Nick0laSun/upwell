from django import forms

options = [
    ('year', 'Статистика по годам'),
    ('season', 'Статистика по сезонам'),
    ('month', 'Статистика по месяцам')
]

class SourceForm(forms.Form):
    search_field = forms.CharField(
        label="Автор/Название",#"Author/Title",
        label_suffix=": ",
        widget=forms.TextInput(
            attrs={
                'placeholder': "Введите имя автора или название статьи" # "Enter Author's name or Title"
            }
        )
    )

class StatForm(forms.Form):
    stat = forms.ChoiceField(
        choices=options,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Виберете тип статистики'
    )