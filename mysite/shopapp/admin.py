from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet

from shopapp.models import Product, Order, ProductImage
from shopapp.admin_mixins import ExportAsCSVMixin

class OrderInline(admin.TabularInline):
    model = Product.orders.through


class ProductInline(admin.StackedInline):
    model = ProductImage


@admin.action(description='Archive products')
def mark_archive(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archive=True)

@admin.action(description='Unarchive products')
def mark_unarchive(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archive=False)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archive,
        mark_unarchive,
        'export_csv',
    ]
    inlines = (
        OrderInline,
        ProductInline,
    )
    list_display = ('pk', 'name', 'description_short', 'price', 'discount', 'archive')
    list_display_links = ('pk', 'name')
    ordering = ('-name', 'pk')
    search_fields = ('name', 'description')
    fieldsets = [
        (None, {
            'fields': ('name', 'description'),
        }),
        ('Price options',{
            'fields': ('price', 'discount'),
            'classes': ('wide', 'collapse'),
        }),
        ('Images',{
            'fields': ('preview',),
        }),
        ('Extra options',{
            'fields': ('archive',),
            'classes': ('collapse',),
            'description': 'Extra options. Field "archive" is for soft delete'
        }),
    ]
    


    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 30:
            return obj.description
        return obj.description[:30] + '...'


class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (
        ProductInline,
    )
    list_display = ('delivery_address', 'promocode', 'created_at', 'user_verbose')

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products').all()
    
    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
