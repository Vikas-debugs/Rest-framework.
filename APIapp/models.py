from django.db import models
import uuid
class Basemodel(models.Model):
    uid = models.UUIDField(primary_key = True,max_length=100,editable=False,default=uuid.uuid4())
    created_at = models.DateField(auto_created = True)
    updated_at= models.DateField(auto_now_add=True)

    class Meta:
        abstract =True

class Todo(Basemodel):
    todo_tittle = models.CharField(max_length =100)
    todo_des = models.TextField()
    is_done =models.BooleanField(default = False)
# Create your models here.
