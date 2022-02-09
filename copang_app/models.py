from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LargeCategories(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    icon_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'large_categories'


class MainLink(models.Model):
    index = models.IntegerField()
    main_url = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'main_link'


class OrderItemOption(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    order_item = models.ForeignKey('OrderItems', models.DO_NOTHING)
    option = models.ForeignKey('ProductOptions', models.DO_NOTHING)
    value = models.ForeignKey('ProductOptionsValues', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_item_option'


class OrderItems(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    merchant_uid = models.CharField(max_length=50)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    product_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_items'


class Orders(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    receiver_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    number_zip = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=100)
    request_message = models.CharField(max_length=50)
    payment_uid = models.CharField(max_length=50)
    payment_money = models.IntegerField()
    merchant_uid = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders'


class Points(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    point = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'points'


class ProductDetailImages(models.Model):
    index = models.IntegerField()
    product = models.ForeignKey('Products', models.DO_NOTHING)
    image_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_detail_images'


class ProductInfos(models.Model):
    product = models.ForeignKey('Products', models.DO_NOTHING)
    description = models.CharField(max_length=50)
    description_content = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'product_infos'


class ProductMainImages(models.Model):
    index = models.IntegerField()
    product = models.ForeignKey('Products', models.DO_NOTHING)
    image_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_main_images'


class ProductOptionTemplateValues(models.Model):
    option_template = models.ForeignKey('ProductOptionTemplates', models.DO_NOTHING)
    values = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_option_template_values'


class ProductOptionTemplates(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_option_templates'


class ProductOptions(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey('Products', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_options'


class ProductOptionsValues(models.Model):
    option = models.ForeignKey(ProductOptions, models.DO_NOTHING)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product_options_values'


class ProductWithOptionTemplates(models.Model):
    product = models.ForeignKey('Products', models.DO_NOTHING)
    template = models.ForeignKey(ProductOptionTemplates, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_with_option_templates'


class Products(models.Model):
    small_category = models.ForeignKey('SmallCategories', models.DO_NOTHING)
    name = models.CharField(max_length=50)
    original_price = models.IntegerField()
    sale_price = models.IntegerField()
    option_template = models.ForeignKey(ProductOptionTemplates, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'


class QuestionReplies(models.Model):
    question = models.ForeignKey('UserProductQuestions', models.DO_NOTHING)
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'question_replies'


class ReviewImages(models.Model):
    review = models.ForeignKey('Reviews', models.DO_NOTHING)
    review_image_url = models.CharField(max_length=200, blank=True, null=True)
    review_image_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'review_images'


class ReviewRecommends(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    review = models.ForeignKey('Reviews', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review_recommends'


class Reviews(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    order_item = models.ForeignKey(OrderItems, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    review_title = models.CharField(max_length=50)
    review_content = models.CharField(max_length=300)
    score = models.FloatField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reviews'


class ShipmentInfos(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    is_basic_address = models.IntegerField()
    memo = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shipment_infos'


class ShipmentItems(models.Model):
    order_item_id = models.IntegerField()
    shipment = models.ForeignKey('Shipments', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shipment_items'


class Shipments(models.Model):
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    unique_code = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    invoice_number = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    arrival_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipments'


class SmallCategories(models.Model):
    name = models.CharField(max_length=50)
    large_category = models.ForeignKey(LargeCategories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'small_categories'


class UserCart(models.Model):
    product = models.ForeignKey(Products, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_cart'


class UserCartOptions(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    cart = models.ForeignKey(UserCart, models.DO_NOTHING)
    option = models.ForeignKey(ProductOptions, models.DO_NOTHING, blank=True, null=True)
    value = models.ForeignKey(ProductOptionsValues, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_cart_options'


class UserProductLike(models.Model):
    product = models.ForeignKey(Products, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_product_like'


class UserProductQuestions(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_product_questions'


class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password_hashed = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_admin = models.IntegerField()
    image_url = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    retired_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'