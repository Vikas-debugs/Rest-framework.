import uuid

# *********************************CustomManager****************************
from django.db import models

from .managers import customManager


class students(models.Model):
    name = models.CharField(max_length=70)
    city = models.CharField()
    objects = customManager()


def home(request):
    st_data = student.objects.all()
    context = {'stu': st_data}
    return render(request, 'students.html', context)


class Basemodel(models.Model):
    uid = models.UUIDField(primary_key=True, max_length=100, editable=False, default=uuid.uuid4())
    created_at = models.DateField(auto_created=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Todo(Basemodel):
    todo_tittle = models.CharField(max_length=100)
    todo_des = models.TextField()
    is_done = models.BooleanField(default=False)


# Create your models here.

# ***************************************PROXY MODELS INHERITENCE***********************
class customManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=15000)


class customManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')


class customManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(eno__lt=15000)


class emp(models.Model):
    eno = models.IntegerField(max_length=40)
    ename = models.CharField()
    esal = models.FloatField()
    eaddr = models.CharField()
    objects = customManager1()


class proxy(emp):
    objects = customManager2()

    class meta:
        proxy = True


class proxy2(emp):
    objects = customManager3()

    class meta:
        proxy = True
