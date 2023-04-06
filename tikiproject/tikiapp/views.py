
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render
from rest_framework import viewsets, permissions , generics,parsers
from django.http import HttpResponse
from django.views import View
from rest_framework.parsers import MultiPartParser
from .models import Category,Account,Product
from rest_framework.decorators import action
from rest_framework.views import Response
from .serializers import CategorySerializer,AccountSerializer , ProductSerializer


# Create your views here.

class CategoryViewSet (viewsets.ModelViewSet, generics.UpdateAPIView, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    # permission_classes = [permissions.IsAuthenticated]

    # permission override
    def get_permissions(self):
        if self.action in['list']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    # list categories

    @action(methods=['get'], detail=True, url_path='products', url_name='products')
    def products(self, request, pk):
        cd = self.get_object()
        products = cd.category_set.all()
        return Response(ProductSerializer(products, context={'request': request}, many=True).data)

class ProductViewSet(viewsets.ViewSet , generics.ListAPIView , generics.UpdateAPIView , generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active = True)
    serializer_class = ProductSerializer
    def get_permissions(self):
        if self.action in['list']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class SellerViewSet (viewsets.ViewSet , generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = Account.objects.filter(is_seller = True)
    serializer_class = AccountSerializer
    pagination_class = None
    permission_classes =  permissions.IsAuthenticated

class BrandViewSet (viewsets.ModelViewSet , generics.ListAPIView):
    queryset = Account.objects.filter(is_seller = True , is_official = True)
    serializer_class = AccountSerializer
    pagination_class = None
class AccountViewSet(viewsets.ViewSet , generics.ListAPIView, generics.CreateAPIView , generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = None
    parser_classes = [MultiPartParser, ]
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['CurrentUser', 'update', 'partial_update']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail= False, url_path='your_user', url_name='your_user')
    def CurrentUser(self, request):
        return Response(AccountSerializer(request.account).data)



