from rest_framework import serializers
from rest_framework.serializers import ModelSerializer , HyperlinkedModelSerializer,Serializer
from .models import Category, List_Categoies,Product, Account , Seller , Customer , Evaluate,Product_detail

class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()
        a = Account(**data)
        a.set_password(a.password)
        a.save()
        return a
    class Meta:
        model = Account
        fields = ['id' ,'username','password','image','created_date','updated_date','is_seller','is_customer']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class SellerSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = Seller
        fields = '__all__'
    def create(self, validated_data):
        user_data = validated_data.pop('account')
        user = Account.objects.create(**user_data)
        seller = Seller.objects.create(account= user , **validated_data)
        return seller

class CustomerSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = Customer
        fields = '__all__'
    def create(self, validated_data):
        user_data = validated_data.pop('account')
        user = Account.objects.create(**user_data)
        customer = Customer.objects.create(account= user , **validated_data)
        return customer

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

class ListCategorySerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = List_Categoies
        fields = ['id' , 'name' , 'category']

    def productDetails(self, request, pk):
        c = self.get_object()
        lessons = c.lesson_set.filter(active=True)

        kw = request.query_params.get('kw')
        if kw:
            lessons = lessons.filter(subject__icontains=kw)

        return Response(LessonSerializer(lessons, many=True).data)

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id' , 'name' , 'base_price','product_sku','image','description','created_date','updated_date','is_active']


class EvaluateSerializer (ModelSerializer):
    class Meta:
        model = Evaluate
        fields = ['id' , 'content' , 'rate' , 'created_date' , 'updated_date' , 'account']

class ProductDetailSerializer(ModelSerializer):

    evaluaties = EvaluateSerializer(many = True)
    class Meta:
        model = Product_detail
        fields = ['id' , 'name' , 'price','quantity','salable_quantity','image','created_date','updated_date','is_active','evaluaties']

