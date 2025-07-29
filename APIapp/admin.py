from django.contrib import admin

from .models import Todo
from .models import emp, proxy, proxy2

admin.site.register(Todo)


# Register your models here.

class empAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']


class proxyA(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']


class proxy2A(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'eaddr']


admin.site.register(emp, empAdmin)
admin.site.register(proxy, proxyA)
admin.site.register(proxy2, proxy2A)
