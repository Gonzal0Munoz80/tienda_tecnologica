from datetime import date

from django import forms

from .models import ventas


class VentasForm(forms.ModelForm):
    class Meta:
        model = ventas
        fields = ["nombre", "email", "fecha", "personas", "comentario"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data["fecha"]
        if fecha < date.today():
            raise forms.ValidationError("la fecha no puede estar en el pasado")
        return fecha