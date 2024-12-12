from django.contrib import admin

# Register your models here.
from .models import User, Store, BusinessUser, ClientUser

admin.site.register(User)
admin.site.register(Store)
admin.site.register(BusinessUser)
admin.site.register(ClientUser)