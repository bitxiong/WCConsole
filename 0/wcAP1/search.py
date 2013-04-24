from django.db.models import Q
from django.shortcuts import render_to_response
from models import WCMsg

def search(request):
	query = request.GET.get('q','')
	if query:
		qset = (
			Q(msgID__icontains=query)|
			Q(msgContent__icontains=query)
		)
		results = WCMsg.objects.filter(qset).distinct()
	else:
		results=[]
	return render_to_response("search.html",{
		"results":results,
		"query":query
	})