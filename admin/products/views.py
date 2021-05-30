from django.shortcuts import render, get_object_or_404
from .models import Product, User
from .serializers import ProductSerializers

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
import random


class ProductViewSets(viewsets.ViewSet):

    def list(self,request):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        # product = Product.objects.get(pk)
        products = Product.objects.all()
        product = get_object_or_404(products,pk=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def update(self,request,pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializers(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):

    def get(self,request):
        users = User.objects.all()
        user = random.choice(users);
        return Response({
            'id' : user.id
        });

    # def post(self, request):
    #     serializer = ArticleSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)