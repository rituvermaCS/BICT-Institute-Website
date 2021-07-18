from django.contrib import admin
from .models import Contact
from .models import Registration
from .models import Details

# Register your models here.

admin.site.register(Contact)
admin.site.register(Registration)
admin.site.register(Details)