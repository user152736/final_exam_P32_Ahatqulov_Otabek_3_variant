from django.forms import ModelForm
from .models import SpendingesModel

class CustomSpendingForm(ModelForm):
    class Meta:
        model = SpendingesModel
        fields = "__all__"
        exclude = ('author',)
