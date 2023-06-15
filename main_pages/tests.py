from django.test import TestCase
from decimal import Decimal
from .models import Color, DeliveryService, Vendor, Material, Product, Order, Client, JobTitle, Delivery, Employee, IncomingProduct, Application
from datetime import date


class ModelTestCase(TestCase):
    def setUp(self):
        self.color = Color.objects.create(color_id='1', color_name='Red')
        self.delivery_service = DeliveryService.objects.create(delivery_service_id='1', delivery_service_name='FedEx')
        self.vendor = Vendor.objects.create(vendors_name='Vendor1', address='Address1')
        self.material = Material.objects.create(material_id='1', material_name='Cotton')
        self.product = Product.objects.create(
            product_id='1',
            product_name='T-Shirt',
            product_image='tshirt.jpg',
            product_color=self.color,
            product_price=Decimal('19.99'),
            product_material=self.material,
            description='Comfortable t-shirt',
            date_of_manufacture=date(2023, 6, 13)
        )
        self.order = Order.objects.create(order_id='1', product=self.product, order_date=date(2023, 6, 13))
        self.client = Client.objects.create(
            clients_id='1',
            clients_full_name='John Doe',
            clients_email_address='john.doe@example.com',
            orders=self.order
        )
        self.job_title = JobTitle.objects.create(job_title_id='1', job_title='Manager')
        self.delivery = Delivery.objects.create(
            delivery_id='1',
            delivery_service=self.delivery_service,
            order_date=date(2023, 6, 13),
            delivery_review='Good service'
        )
        self.employee = Employee.objects.create(
            employee_id='1',
            employee_full_name='John Smith',
            job_title=self.job_title,
            employee_address='123 Main St'
        )
        self.incoming_product = IncomingProduct.objects.create(
            delivery_number='1',
            vendor=self.vendor,
            employee=self.employee,
            date=date(2023, 6, 13)
        )
        self.application = Application.objects.create(
            application_id='1',
            client=self.client,
            product=self.product,
            delivery_date=date(2023, 6, 13)
        )

    def test_color_model(self):
        # Тест 1: Проверка модели "Color"
        color = Color.objects.get(color_id='1')
        self.assertEqual(color.color_name, 'Red')

    def test_delivery_service_model(self):
        # Тест 2: Проверка модели "DeliveryService"
        delivery_service = DeliveryService.objects.get(delivery_service_id='1')
        self.assertEqual(delivery_service.delivery_service_name, 'FedEx')

    def test_vendor_model(self):
        # Тест 3: Проверка модели "Vendor"
        vendor = Vendor.objects.get(vendors_name='Vendor1')
        self.assertEqual(vendor.address, 'Address1')

    def test_material_model(self):
        # Тест 4: Проверка модели "Material"
        material = Material.objects.get(material_id='1')
        self.assertEqual(material.material_name, 'Cotton')

    def test_product_model(self):
        # Тест 5: Проверка модели "Product"
        product = Product.objects.get(product_id='1')
        self.assertEqual(product.product_name, 'T-Shirt')
        self.assertEqual(product.product_color, self.color)
        self.assertEqual(product.product_price, Decimal('19.99'))
        self.assertEqual(product.product_material, self.material)
        self.assertEqual(product.description, 'Comfortable t-shirt')
        self.assertEqual(product.date_of_manufacture, date(2023, 6, 13))
