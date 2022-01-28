from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,PrivateData
from rest_framework import viewsets
from .serializers import UserSerializer,PrivateDataSerializer
# Create your views here.
from .utils import *

# class GetData(APIView):
#     def post(self,request):
#         if request.data.__contains__("data") and request.data.__contains__("signature"):
#             signature=bytes(request.data["signature"],'utf-8')
#             data=request.data["data"]
#             user = get_user(signature)
#             if user is None:
#                 return Response("Not Verified")
#         return Response("signatue or data not passed")



class VerifyingUser(APIView):
    def get(self,request):
        print(request.session)
        return Response("Get Not Allowed")
    
    def post(self,request):
        if request.data.__contains__("signature"):
            signature=bytes(request.data["signature"],'utf-8')
            user = get_user(signature)
            if user is None:
                return Response("Not Verified")
            request.session["public_key"]=user.public_key
            return Response("Verified")

        return Response("signatue not passed")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]

class DataCreateViewSet(viewsets.ModelViewSet):
    queryset=PrivateData.objects.all()
    serializer_class = PrivateDataSerializer

    def create(self,request):
        if request.session.__contains__("public_key"):
            data=request.data["data"]
            public_key=request.session["public_key"]
            user=User.objects.get(public_key)
            # apend add data to user data object
            return Response("Data added")
            
