from django.contrib import admin
from wcAP1.models import *
	
class Admin(admin.ModelAdmin):
	list_display = ('msgID','msgFrom','msgContent','msgTimestamp',)
	list_filter = ('msgFrom',)
	ordering = ('-msgTimestamp',)
	search_fieds = ('msgContent',)
	app_label = 'My App'

class UserAdmin(admin.ModelAdmin):
	list_display=('name','fakeID','msgCount')
	
	
admin.site.register(WCMsg,Admin)
admin.site.register(WCUser,UserAdmin)