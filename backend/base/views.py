from django.shortcuts  import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product 
from .serializers import ProductSerializer

from .products import products
    
@api_view(['GET'])
def getRoutes(request):

    return Response('Hello World')

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many = True)

    return Response(serializers.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializers = ProductSerializer(product, many = False)
    return Response(serializers.data)