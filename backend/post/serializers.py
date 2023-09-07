from rest_framework import serializers
from .models import Products, Comment


class PostSerializer(serializers.ModelSerializer):


    class Meta:
        fields = '__all__'
        model = Products
        
class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'product', 'body', 'created']


