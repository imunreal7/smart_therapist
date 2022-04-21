from django.contrib import admin
from .models import Admin
from .models import User
from .models import User_data


# Register your models here.





admin.site.register(Admin)
admin.site.register(User)
admin.site.register(User_data)