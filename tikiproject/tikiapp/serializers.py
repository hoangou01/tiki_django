from requests import Response
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer , HyperlinkedModelSerializer,Serializer
from .models import Category,Product, Account , Evaluate

class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()
        a = Account(**data)
        a.set_password(a.password)
        a.save()
        return a
    class Meta:
        model = Account
        fields = ['id' ,'username','password','image','is_seller','is_customer']
        extra_kwargs = {
            'password': {'write_only': True}
        }

# class SellerSerializer(serializers.ModelSerializer):
#     account = AccountSerializer()
#     class Meta:
#         model = Seller
#         fields = '__all__'
#     def create(self, validated_data):
#         user_data = validated_data.pop('account')
#         user = Account.objects.create(**user_data)
#         seller = Seller.objects.create(account= user , **validated_data)
#         return seller

# class CustomerSerializer(serializers.ModelSerializer):
#     account = AccountSerializer()
#     class Meta:
#         model = Customer
#         fields = '__all__'
#     def create(self, validated_data):
#         user_data = validated_data.pop('account')
#         user = Account.objects.create(**user_data)
#         customer = Customer.objects.create(account= user , **validated_data)
#         return customer
class EvaluateSerializer (serializers.ModelSerializer):
    account = AccountSerializer(many=False)
    class Meta:
        model = Evaluate
        fields = ['id' , 'content' , 'rate' , 'created_date' , 'updated_date','account']
class ProductSerializer(EvaluateSerializer):
    evaluate = EvaluateSerializer(many=True)

    # image = serializers.SerializerMethodField(source='image')
    # def get_image(self , obj):
    #     request = self.context['request']
    #     if obj.image.name.startswith('static/'):
    #         path = "/%s" % obj.image.name
    #     else:
    #         path = 'static/%s' % obj.image.name
    #     return request.build_absolute_uri(path)
    class Meta:
        model = Product
        fields = ['id' , 'name' , 'base_price','quantity','salable_quantity','discount','product_sku','image','description','created_date','updated_date','is_active','evaluate']
class OrderSerializer (serializers.ModelSerializer):

    class Meta:
        model = Evaluate
        fields = ['id' , 'content' , 'rate' , 'created_date' , 'updated_date']

class OrderItemSerializer (serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    order = OrderSerializer(many = False)
    class Meta:
        model = Evaluate
        fields = ['id' , 'quantity' , 'product','order']

class CartItemSerializer (serializers.ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = Evaluate
        fields = ['id' , 'quantity' , 'product']
class CartSerializer (serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    class Meta:
        model = Evaluate
        fields = ['id' , 'total' ,'cart_items']



class CategorySerializer(HyperlinkedModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    def get_image(self , obj):
        request = self.context['request']
        if obj.image.name.startswith('static/'):
            path = "/%s" % obj.image.name
        else:
            path = 'static/%s' % obj.image.name
        return request.build_absolute_uri(path)
    class Meta:
        model = Category
        fields = ['id' , 'categoryname' , 'image']

    def products(self, request, pk):
        c = self.get_object()
        products = c.product_set.filter(active=True)

        kw = request.query_params.get('kw')
        if kw:
            products = products.filter(name__icontains=kw)

        return Response(ProductSerializer(Product, many=True).data)



