from django.contrib import admin


from .models import *


admin.site.register(Category)
admin.site.register(Genus)
admin.site.register(Exemplar)
admin.site.register(ThreatExemplar)
admin.site.register(ThreatExemplarImage)
admin.site.register(User)
admin.site.register(Protocol)
admin.site.register(ProtocolExemplarChoice)
admin.site.register(ProtocolExemplarFind)