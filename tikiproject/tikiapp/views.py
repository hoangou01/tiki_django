from django.shortcuts import render
from rest_framework import viewsets, permissions , generics
from django.http import HttpResponse
from django.views import View
from rest_framework.parsers import MultiPartParser
from .models import Category,List_Categoies,Account,Seller ,Customer
from rest_framework.decorators import action
from rest_framework.views import Response
from .serializers import CategorySerializer, ListCategorySerializer ,AccountSerializer,SellerSerializer,CustomerSerializer


# Create your views here.

def index(request):
    return HttpResponse("hihi")
def welcome(request , year):
    return HttpResponse("hello" + str(year))

class TestView(View):
    def get(self , request):
        return HttpResponse("hihi")
    def post(self , request):
        pass

class CategoryViewSet (viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticated]

    # permission override
    # def get_permissions(self):
    #     if self.action in['list']:
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
    # list categories
    @action(methods=['get'], detail=True, url_path='listcategories',url_name='listcategories')
    def ListCategories(self,request , pk):
        c = self.get_object()
        ListCategories = c.category_set.all()
        return Response(ListCategorySerializer(ListCategories,context={'request':request}, many=True).data)

    @action(methods=['get'], detail=True, url_path='products', url_name='products')
    def products(self, request, pk):
        cd = self.get_object()
        products = cd.category_set.all()
        return Response(ListCategorySerializer(products, context={'request': request}, many=True).data)



class ListCategoryViewSet (viewsets.ModelViewSet):
    queryset = List_Categoies.objects.all()
    serializer_class = ListCategorySerializer
    pagination_class = None
    # permission_classes = [permissions.IsAuthenticated]
    @action(methods=['get'], detail=True, url_path='products', url_name='products')
    def products(self, request, pk):
        cd = self.get_object()
        products = cd.category_set.all()
        return Response(ListCategorySerializer(products, context={'request': request}, many=True).data)
class AccountViewSet(viewsets.ViewSet , generics.CreateAPIView , generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    pagination_class = None
    parser_classes = [MultiPartParser, ]
