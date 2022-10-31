from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework_simplejwt.views import TokenObtainPairView
import json
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from api.serializers import LoginSerializer, UserSerializer,ImageVerificationSerializer
from api.models import ImageVerification
from rest_framework import generics


class UserRegistrationView(generics.CreateAPIView):
    """
    User registration view.
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Post request to register a user
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "User": UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(TokenObtainPairView):
    """
    Client login endpoint.
    """

    serializer_class = LoginSerializer


# class ImageVerificationView(generics.CreateAPIView):
#     queryset = ImageVerification.objects.all()
#     serializer_class = ImageVerificationSerializer


# class ImageViewSet(generics.ListAPIView):
#     queryset = UploadImageTest.objects.all()
#     serializer_class = ImageSerializer
     
#     parser_classes = [MultiPartParser, FormParser]
#     serializer_class = ImageSerializer

#     def post(self, request, *args, **kwargs):
#         file = request.FILES['image']
#         image = UploadImageTest.objects.create(image=file)
#         return HttpResponse(json.dumps({'message': "Uploaded"}), status=200

# class ImageVerificationView(APIView):
#   parser_classes = (MultiPartParser, FormParser)

#   def post(self, request):
#     image_verification_serializer = ImageVerificationSerializer(data=request.data)
#     if image_verification_serializer.is_valid():
#       image_verification_serializer.save()
#       return Response(image_verification_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(image_verification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageVerificationView(generics.ListAPIView):
  queryset = ImageVerification.objects.all()
  serializer_class = ImageVerificationSerializer

  def post(self, request):
    image_verification_serializer = ImageVerificationSerializer(data=request.data)
    if image_verification_serializer.is_valid():
      image_verification_serializer.save()
      return Response(image_verification_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(image_verification_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        

# class ImageVerificationView(generics.ListAPIView):
#     queryset =ImageVerification.objects.all()
#     serializer_class = ImageVerificationSerializer

#     def post(self, request, *args, **kwargs):
#       if 'file' in request.data:
#         file = request.data['file']
#       else:
#         file = False
#       blister_image_url = ImageVerification.objects.create(blister_image_url=file)
#       return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)    