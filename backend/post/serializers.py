from rest_framework import serializers
from .models import Products, Comment,User
from django.contrib.auth.password_validation import validate_password

class PostSerializer(serializers.ModelSerializer):


    class Meta:
        fields = '__all__'
        model = Products
        
class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'product', 'body', 'created']





class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
        )

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
