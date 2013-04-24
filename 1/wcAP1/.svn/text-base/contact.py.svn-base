from django import forms

TOPIC_CHOICES = (
	('general','General Enquiry'),
	('bug','Bug Report')
)

class ContactForm(forms.Form):
	topic = forms.ChoiceField(choices=TOPIC_CHOICES)
	message = forms.CharField()
	other = forms.CharField(required=False)
