from rest_framework import serializers
from .models import Todo
from django.template.defaultfilters import slugify
class TodoSerializer( serializers.ModelSerializer):
    # slug = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        fields= ['todo_tittle']

    def get_slug(self,objs):
         return "vikas yadav"

# '''def validate(self,validated_data):
            # if validated_data.get('todo_tittle'):
            #     todo_tittle = validated_data['todo_tittle']'''