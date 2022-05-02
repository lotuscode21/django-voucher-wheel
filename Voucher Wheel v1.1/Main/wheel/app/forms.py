from django import forms

from app.draw import is_code_valid
from app.models import Draw
from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


class DrawForm(forms.ModelForm):
    class Meta:
        model = Draw
        fields = ('email', 'code',)

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get("code")

        if is_code_valid(code) is not True:
            self.add_error('code', forms.ValidationError("Invalid or expired code!"))
