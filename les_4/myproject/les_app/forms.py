from django import forms

class RandForm(forms.Form):
    kind = forms.ChoiceField(label='Что бросаем?', choices=[('coin', 'Бросок монеты'), ('cube', 'Бросок кубика'), ('number', 'Случайное число')])
    count_tries = forms.IntegerField(label='Сколько раз?', min_value=1, max_value=64)