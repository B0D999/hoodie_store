from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название коллекции')

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name or ''


class Color(models.Model):
    color_id = models.CharField(primary_key=True, max_length=36)
    color_name = models.CharField(max_length=50, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.color_name or ''


class DeliveryService(models.Model):
    delivery_service_id = models.CharField(primary_key=True, max_length=36)
    delivery_service_name = models.CharField(max_length=100, verbose_name='Служба доставки')

    class Meta:
        verbose_name = 'Служба доставки'
        verbose_name_plural = 'Службы доставки'

    def __str__(self):
        return self.delivery_service_name or ''


class Vendor(models.Model):
    vendor_name = models.CharField(primary_key=True, max_length=100, verbose_name='Поставщик')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.vendor_name or ''


class Material(models.Model):
    material_id = models.CharField(primary_key=True, max_length=36)
    material_name = models.CharField(max_length=50, verbose_name='Название материала')

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.material_name or ''


class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=36)
    product_name = models.CharField(max_length=100, verbose_name='Название товара', db_index=True)
    product_image = models.ImageField(verbose_name='Изображение товара', upload_to='product_images/')
    product_color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет', related_name='products')
    product_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    product_material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал')
    description = models.TextField(default='Худи', verbose_name='Описание')
    date_of_manufacture = models.DateField(verbose_name='Дата изготовления')
    stock = models.IntegerField(verbose_name='Остаток на складе', default=10)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.product_name or ''


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=36)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    order_date = models.DateField(auto_now=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.order_id) or ''


class Client(models.Model):
    client_id = models.CharField(primary_key=True, max_length=36)
    client_full_name = models.CharField(max_length=100, verbose_name='ФИО клиента')
    client_email_address = models.EmailField(verbose_name='Адрес электронной почты')
    orders = models.ManyToManyField(Order, verbose_name='Заказы', related_name='clients')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.client_full_name or ''


class JobTitle(models.Model):
    job_title_id = models.CharField(primary_key=True, max_length=36)
    job_title = models.CharField(max_length=100, verbose_name='Должность')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.job_title or ''


class Delivery(models.Model):
    delivery_id = models.CharField(primary_key=True, max_length=36)
    delivery_service = models.ForeignKey(DeliveryService, on_delete=models.CASCADE, verbose_name='Служба доставки')
    clients = models.ManyToManyField(Client, verbose_name='Клиенты', related_name='deliveries')
    order_date = models.DateField(auto_now=True, verbose_name='Дата доставки')
    delivery_review = models.TextField(verbose_name='Отзыв о доставке')

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        return str(self.delivery_id) or ''


class Employee(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=36)
    employee_full_name = models.CharField(max_length=100, verbose_name='ФИО сотрудника')
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE, verbose_name='Должность')
    employee_address = models.CharField(max_length=100, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.employee_full_name or ''


class IncomingProduct(models.Model):
    delivery_number = models.CharField(primary_key=True, max_length=36)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='Поставщик')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    date = models.DateField(auto_now=True, verbose_name='Дата поставки')

    class Meta:
        verbose_name = 'Поступление товара'
        verbose_name_plural = 'Поступления товара'

    def __str__(self):
        return str(self.delivery_number) or ''


class Application(models.Model):
    application_id = models.CharField(primary_key=True, max_length=36)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    delivery_date = models.DateField(auto_now=True, verbose_name='Дата доставки')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return str(self.application_id) or ''


class Card(models.Model):
    card_id = models.CharField(primary_key=True, max_length=36)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name='Коллекция', related_name='cards')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='card')

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return str(self.card_id) or ''
