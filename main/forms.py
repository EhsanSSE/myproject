from django.forms import ModelForm
from main.models import Contact, Newslaters

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewslatersForm(ModelForm):
    class Meta:
        model = Newslaters
        fields = '__all__'
