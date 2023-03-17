# Generated by Django 4.1.7 on 2023-03-17 05:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_name', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('image', models.ImageField(default=None, null=True, upload_to='Account/%Y/%m')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('refreshToken', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=45)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=45, unique=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='Category/%Y/%m')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('rate', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='evaluate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='List_Categoies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tikiapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_ship', models.CharField(max_length=100)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('status', models.CharField(max_length=40)),
                ('is_deleted', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_sku', models.CharField(max_length=45, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='Product/%Y/%m')),
                ('description', models.TextField(max_length=200, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=45, null=True)),
                ('categoryDetail', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product', to='tikiapp.list_categoies')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=200, null=True)),
                ('name', models.CharField(max_length=45, unique=True)),
                ('phone', models.CharField(max_length=20, null=True, unique=True)),
                ('address', models.CharField(max_length=45, null=True)),
                ('isOfficial', models.BooleanField(default=False)),
                ('isChecked', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.IntegerField()),
                ('salable_quantity', models.IntegerField()),
                ('image', models.ImageField(default=None, upload_to='Product/%Y/%m')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('account', models.ManyToManyField(related_name='product_detail', through='tikiapp.Evaluate', to=settings.AUTH_USER_MODEL)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product_detail', to='tikiapp.option')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product_detail', to='tikiapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product', to='tikiapp.seller'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=45)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('process', models.CharField(max_length=45, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tikiapp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='order_item', to='tikiapp.order')),
                ('productDetail', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='order_item', to='tikiapp.product_detail')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='productDetail',
            field=models.ManyToManyField(related_name='order', through='tikiapp.Order_item', to='tikiapp.product_detail'),
        ),
        migrations.AddField(
            model_name='option',
            name='option_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tikiapp.option_group'),
        ),
        migrations.AddField(
            model_name='option',
            name='products',
            field=models.ManyToManyField(related_name='option', through='tikiapp.Product_detail', to='tikiapp.product'),
        ),
        migrations.AddField(
            model_name='list_categoies',
            name='sellers',
            field=models.ManyToManyField(related_name='list_categories', through='tikiapp.Product', to='tikiapp.seller'),
        ),
        migrations.AddField(
            model_name='evaluate',
            name='productDetail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='evaluate', to='tikiapp.product_detail'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=80)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('DOB', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cart_item', to='tikiapp.cart')),
                ('productDetail', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cart_item', to='tikiapp.product_detail')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='productDetail',
            field=models.ManyToManyField(related_name='cart', through='tikiapp.Cart_item', to='tikiapp.product_detail'),
        ),
    ]
