# Create your views here.
from contact import ContactForm
from django.shortcuts import render_to_response
def contact(request):
	form = ContactForm()
	return render_to_response('contact.html',{'form':form})

def index(request):
	return contact(request)