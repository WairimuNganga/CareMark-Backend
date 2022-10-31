from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models import User, ImageVerification



class UserSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating users"""

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = ("firstname", "lastname", "phonenumber", "email", "password")

    def create(self, validated_data, **kwargs):
        """
        Overriding the default create method of the Model serializer.
        """
        print(validated_data)
        user = User(
            email=validated_data["email"],
            firstname=validated_data["firstname"],
            lastname=validated_data["lastname"],
            phonenumber=validated_data["phonenumber"],
        )
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(LoginSerializer, self).validate(attrs)

        # Custom data included in the response
        data.update({"id": self.user.id})
        data.update({"email": self.user.email})
        data.update({"firstname": self.user.firstname})
        data.update({"lastname": self.user.lastname})
        data.update({"phonenumber": self.user.phonenumber})
        return data


class ImageVerificationSerializer(serializers.ModelSerializer):
  class Meta():
    model = ImageVerification
    fields = ('patient','blister_image_url','timestamp')     


