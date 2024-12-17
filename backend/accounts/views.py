from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .serializers import UserSerializer, StoreSerializer, BusinessUserSerializer, ClientUserSerializer


def get_user(request):
    return HttpResponse("Hello, world.")

@api_view(["POST"])
def create_user(request):
    data = request.data
    print("hiiiiiiiiiiiiii")
    serializer = UserSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
