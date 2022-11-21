from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')


# You will need serializers to convert model instances to JSON so that the frontend can work with the received data.