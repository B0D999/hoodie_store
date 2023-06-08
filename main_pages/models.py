from django.db import models
import uuid


# default
class Color(models.Model):
    color_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    color_name = models.CharField(max_length=50, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        if self.color_name:
            return str(self.color_name)
        else:
            return ''


class DeliveryService(models.Model):
    delivery_service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    delivery_service_name = models.CharField(max_length=100, verbose_name='Служба доставки')

    class Meta:
        verbose_name = 'Служба доставки'
        verbose_name_plural = 'Службы доставки'

    def __str__(self):
        if self.delivery_service_name:
            return self.delivery_service_name
        else:
            return ''


class Vendor(models.Model):
    vendors_name = models.CharField(max_length=100, primary_key=True, verbose_name='Поставщик')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        if self.vendors_name:
            return self.vendors_name
        else:
            return ''


class Material(models.Model):
    material_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material_name = models.CharField(max_length=50, verbose_name='Название материала')

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        if self.material_name:
            return str(self.material_name)
        else:
            return ''


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100, verbose_name='Название товара')
    product_image = models.ImageField(verbose_name='Изображение товара')
    product_color = models.ForeignKey(to=Color, on_delete=models.CASCADE,
                                      verbose_name='Цвет')
    product_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    product_material = models.ForeignKey(to=Material, on_delete=models.CASCADE, verbose_name='Материал')
    description = models.TextField(default='Худи', verbose_name='Описание')
    date_of_manufacture = models.DateField(verbose_name='Дата изготовления')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        if self.product_name:
            return str(self.product_name)
        else:
            return ''


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    order_date = models.DateField(auto_now=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        if self.order_id:
            return str(self.order_id)
        else:
            return ''


class Client(models.Model):
    clients_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    clients_full_name = models.CharField(max_length=100, verbose_name='ФИО клиента')
    clients_email_address = models.EmailField(verbose_name='Адрес электронной почты')
    orders = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказы')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        if self.clients_full_name:
            return self.clients_full_name
        else:
            return ''


class JobTitle(models.Model):
    job_title_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.CharField(max_length=100, verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        if self.job_title_id:
            return self.job_title
        else:
            return ''


class Delivery(models.Model):
    delivery_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    delivery_service = models.ForeignKey(to=DeliveryService, on_delete=models.CASCADE, verbose_name='Служба доставки')
    clients = models.ManyToManyField(to=Client, verbose_name='Клиенты')
    order_date = models.DateField(auto_now=True, verbose_name='Дата доставки')
    delivery_review = models.TextField(verbose_name='Отзыв о доставке')

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        if self.delivery_id:
            return str(self.delivery_id)
        else:
            return ''


class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_full_name = models.CharField(max_length=100, verbose_name='ФИО сотрудника')
    job_title = models.ForeignKey(to=JobTitle, on_delete=models.CASCADE, verbose_name='Должность')
    employee_address = models.CharField(max_length=100, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        if self.employee_full_name:
            return self.employee_full_name
        else:
            return ''


class IncomingProduct(models.Model):
    delivery_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE, verbose_name='Поставщик')
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    date = models.DateField(auto_now=True, verbose_name='Дата поставки')

    class Meta:
        verbose_name = 'Поступление товара'
        verbose_name_plural = 'Поступления товара'

    def __str__(self):
        if self.delivery_number:
            return str(self.delivery_number)
        else:
            return ''


class Application(models.Model):
    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name='Клиент')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    delivery_date = models.DateField(auto_now=True, verbose_name='Дата доставки')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        if self.application_id:
            return str(self.application_id)
        else:
            return ''
