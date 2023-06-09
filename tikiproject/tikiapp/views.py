from django.db.models import Count
from django.db.models.signals import post_save
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, parsers, status
from django.http import HttpResponse, JsonResponse
from django.views import View
from .paginators import ProductPaginator, BrandPaginator,EvaluatePaginator
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Category,Account,Product,Evaluate,Order , Order_item , Cart_item , Cart
from rest_framework.decorators import action
from rest_framework.views import Response
from .serializers import CategorySerializer,AccountSerializer , ProductSerializer,EvaluateSerializer,OrderSerializer , OrderItemSerializer,CartSerializer,CartItemSerializer,BrandsSerializer,ProductReportSerializer




# Create your views here.

class CategoryViewSet (viewsets.ModelViewSet, generics.UpdateAPIView, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    # permission_classes = [permissions.IsAuthenticated]

    # permission override
    # def get_permissions(self):
    #     if self.action in['list']:
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
    # list categories


    @action(methods=['get'], detail=True, url_path='products', url_name='products')
    def products(self, request, pk):
        c = self.get_object()
        products = c.product_set.filter(is_active = True)

        return Response(ProductSerializer(products, many=True).data)

    @action(methods=['get'], detail=True, url_path='recommend-products', url_name='recommend-products')
    def recommend_product(self, request, pk):
        c = self.get_object()
        products = c.product_set.filter(is_active=True).order_by('?')[:6]
        return Response(ProductSerializer(products, many=True).data)
class CategoryRamdomViewSet(viewsets.ModelViewSet , generics.ListAPIView ,  generics.RetrieveAPIView):
    queryset = Category.objects.all().order_by('?')[:5]
    serializer_class = CategorySerializer
    pagination_class = None
class ProductViewSet(viewsets.ModelViewSet , generics.ListAPIView , generics.UpdateAPIView , generics.RetrieveAPIView):
    # parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = Product.objects.filter(is_active = True).order_by('-id')
    serializer_class = ProductSerializer
    pagination_class = ProductPaginator
    def filter_queryset(self, queryset):
        kw = self.request.query_params.get('kw')

        if self.action.__eq__('list') and kw:
            queryset = queryset.filter(name__icontains=kw)

        cate_id = self.request.query_params.get('category_id')
        if cate_id:
            queryset = queryset.filter(category_id=cate_id)

        # rate = self.request.query_params.get('rate')
        # if rate:
        #     queryset = queryset.filter(category_id=cate_id)

        priceFrom = self.request.query_params.get('priceFrom')
        priceTo = self.request.query_params.get('priceTo')
        # if priceTo is None:
        #     queryset = queryset.filter(base_price__gte=priceFrom)

        if priceFrom and priceTo:
            queryset = queryset.filter(base_price__gte=priceFrom,base_price__lt=priceTo)


        sortStatus = self.request.query_params.get('sortStatus')
        if sortStatus == 'ACS':
            queryset = queryset.order_by('base_price')
        else:
            queryset = queryset.order_by('-base_price')

        return queryset
    def get_permissions(self):
        if self.action in['list','retrieve','get_comments']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    @action(methods=['post'], detail=True, name='Hide this product', url_path='hide-product', url_name='hide-product')
    def hide_product(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            product.is_active = False
            product.save()
        except Product.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(product)
        return Response(serializer.data,
                        status=status.HTTP_200_OK)
    @action(methods=['post'], detail=True, name='post a comment' ,url_path='evaluates', url_name='evaluates')
    def comments(self, request, pk):
        product = self.get_object()
        e = Evaluate(content=request.data['content'], rate = request.data['rate'], product=product , seller = request.user)
        e.save()
        return Response(EvaluateSerializer(e).data, status=status.HTTP_201_CREATED)
    @action(methods=['get'], detail=True, url_path='evaluations', url_name='evaluations')
    def get_comments(self, request, pk):
        paginate_by = 2
        p = self.get_object()
        evaluates = p.evaluate.all()

        return Response(EvaluateSerializer(evaluates, many=True).data)


class BrandViewSet (viewsets.ModelViewSet , generics.ListAPIView):
    queryset = Account.objects.filter(is_seller = True , is_official = False)
    serializer_class = BrandsSerializer
    pagination_class = None
class CartViewSet(viewsets.ModelViewSet , generics.RetrieveAPIView , generics.CreateAPIView , generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = None

    @action(methods=['get'], detail=True, url_path='cart-items', url_name='cart-items')
    def cart_items(self, request, pk):
        c = self.get_object()
        cart_items = c.cart_item.all()

        return Response(CartItemSerializer(cart_items, many=True).data)

class OrderViewSet (viewsets.ModelViewSet , generics.RetrieveAPIView , generics.CreateAPIView , generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = None

    @action(methods=['get'], detail=True, url_path='order-items', url_name='order-items')
    def order_items(self, request, pk):
        o = self.get_object()
        order_items = o.order_item.all()

        return Response(OrderItemSerializer(order_items, many=True).data)
class OrderItemViewSet (viewsets.ModelViewSet , generics.ListAPIView , generics.CreateAPIView):
    queryset = Order_item.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = None

class SellerViewSet (viewsets.ViewSet , generics.ListAPIView ,generics.CreateAPIView, generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = Account.objects.filter(is_seller = True , is_customer = False)
    serializer_class = AccountSerializer
    pagination_class = None
    parser_classes = [parsers.MultiPartParser, ]

    @action(methods=['get'], detail=True, url_path='products', url_name='products')
    def get_comments(self, request, pk):
        s = self.get_object()
        products = s.product_seller_set.filter(is_active = True)

        return Response(ProductSerializer(products, many=True).data)
    def get_permissions(self):
        if self.action in ['CurrentSeller', 'update', 'partial_update']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]
    @action(methods=['get'], detail=False, url_path='current-user', url_name='current-user')
    def CurrentSeller(self, request):
        return Response(AccountSerializer(request.user).data)

    @action(methods=['get'], detail=True, url_path='products', url_name='products')
    def get_comments(self, request, pk):
        s = self.get_object()
        products = s.product_seller_set.filter(is_active = True)

        return Response(ProductSerializer(products, many=True).data)

    @action(methods=['get'], detail=True, url_path='report-product', url_name='report-product')
    def report_product(self, request, pk):
        s = self.get_object()
        products = s.product_seller_set.values('category__categoryname').annotate(Count('id'))

        return Response(products)
    @action(methods=['post'], detail=True, name='post a product', url_path='products', url_name='products')
    def products(self, request, pk):
        seller = self.get_object()
        p = Product(description=request.data['description'],name=request.data['name'],base_price=request.data['base_price'],
            product_sku= request.data['product_sku'],
            quantity= request.data['quantity'],
            salable_quantity= request.data['salable_quantity'],
            discount= request.data['discount'],
            image= request.data['image'],
            category= request.data['category'],
            seller = request.data['seller'])

        p.save()
        return Response(ProductSerializer(p, context={'request': request}).data, status=status.HTTP_201_CREATED)
class CustomerViewSet(viewsets.ViewSet ,generics.CreateAPIView, generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = Account.objects.filter(is_seller=False, is_customer=True)
    serializer_class = AccountSerializer
    pagination_class = None
    parser_classes = [parsers.MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current-user', url_name='current-user')
    def CurrentCustomer(self, request):
        return Response(AccountSerializer(request.user).data)

    @action(methods=['get'], detail=True, url_path='order-items', url_name='order-items')
    def order_items(self, request, pk):
        c = self.get_object()
        order_items = c.order.order_item.all()
        return Response(OrderItemSerializer(order_items, many=True).data)



class AccountViewSet(viewsets.ViewSet , generics.CreateAPIView , generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Account.objects.filter(is_customer = True,is_seller = False)
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
        account = self.get_object()
        if account.is_seller == True:
            return Response(AccountSerializer(request.seller).data)
        if account.is_customer == True:
            return Response(AccountSerializer(request.customer).data)
        return Response(AccountSerializer(request.account).data)


class ProductReportView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None

    def get_queryset(self):
        data = Product.objects.annotate(count=Count('id')).values()
        return data

