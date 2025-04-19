from django.core.management import BaseCommand

from shopapp.models import Product, Order

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        order = Order.objects.first()
        if not order:
            self.stdout.write(self.style.ERROR('no order found'))
            return 
        
        products = Product.objects.all()

        for product in products:
            order.products.add(product)
        
        order.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Succesfully added products {order.products.all()} to order {order}'
            )
        )