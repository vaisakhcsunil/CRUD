from django import forms
from.models import person
class geekform (forms.Modelform):
    class meta:
        model=person
        fields=[
            "title",
            "description",
        ]