from django.contrib import admin
from wcAP1.models import *
	
class Admin(admin.ModelAdmin):
	list_display = ('msgID','msgContent','msgTimestamp',)
	ordering = ('-msgTimestamp',)
	search_fieds = ('msgContent',)
	app_label = 'My App'

class UserAdmin(admin.ModelAdmin):
	list_display=('name','fakeID','msgCount')
	
	
admin.site.register(WCMsg,Admin)
admin.site.register(WCUser,UserAdmin)