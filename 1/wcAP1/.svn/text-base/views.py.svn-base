# Create your views here.
from contact import ContactForm
from django.shortcuts import render_to_response
from bae.api import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from wchooker import wcInfoHandler
from models import WCMsg
from bae.core import const

def contact(request):
	form = ContactForm()
	return render_to_response('contact.html', {'form':form})

def index(request):
	logging.info('info log')
	return contact(request)


def wcrequest(request):
	# validation
	query = request.GET.get('signature', '')
	echostr = request.GET.get('echostr', '')
	response = HttpResponse(echostr)
	return response

@csrf_exempt
def wcHook(request):
	#logging.info('Called')
	#return HttpResponse('wrong')
	if(request.method == 'POST'):
		handler = wcInfoHandler()
		rawStr = request.raw_post_data
		response = handler.respondMsg(rawStr)
		return HttpResponse(response)
	
def test(request):
	msg = WCMsg.objects.get(msgContent__iexact='test')
	return HttpResponse(msg.msgID)
