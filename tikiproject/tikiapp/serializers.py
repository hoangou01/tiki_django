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
        fields = ['id' ,'first_name','last_name','username','phone','DOB','gender','password','image','is_seller','is_customer']
        extra_kwargs = {
            'password': {'write_only': True}
        }


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
class BrandsSerializer (serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id' ,'first_name','last_name','username','image','is_seller','is_official']
class EvaluateSerializer (serializers.ModelSerializer):
    account = AccountSerializer(many=False)
    class Meta:
        model = Evaluate
        fields = ['id' , 'content' , 'rate' , 'created_date' , 'updated_date','account']
class ProductSerializer(serializers.ModelSerializer):
    # evaluate = EvaluateSerializer(many=True)
    seller = AccountSerializer(many=False)

    image = serializers.SerializerMethodField(source='image')
    def get_image(self , obj):
        # request = self.context['request']
        if obj.image.name.startswith('static/'):
            path = "/%s" % obj.image.name
        else:
            path = 'static/%s' % obj.image.name
        return path
    class Meta:
        model = Product
        fields = ['id' , 'name' , 'base_price','quantity','salable_quantity','discount','product_sku','image','description','is_global', 'category','seller']

class ProductReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

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



class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    def get_image(self , obj):
        # request = self.context['request']
        if obj.image.name.startswith('static/'):
            path = "/%s" % obj.image.name
        else:
            path = 'static/%s' % obj.image.name
        return path
    class Meta:
        model = Category
        fields = ['id' , 'categoryname' , 'image']





