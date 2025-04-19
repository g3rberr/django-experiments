from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from shopapp.models import Product, Order
from shopapp.forms import ProductForm, GroupForm



class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('Laptop', 1999),
            ('Desktop', 2777),
            ('Smartphone', 3888),
        ]
        context = {
            'title': 'SkillBox Shop',
            'products': products    
        }
        return render(request, 'shopapp/shop-index.html', context)

   
class GroupsListView(View):
    def get(self,request: HttpRequest) -> HttpResponse:
        context = {
        'form': GroupForm(),
        'groups': Group.objects.prefetch_related('permissions').all()
        }
        return render(request, 'shopapp/groups-list.html', context)
    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)



class ProductDetailView(DetailView):
    template_name = 'shopapp/products-details.html'
    model = Product
    context_object_name = 'product' 



class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    context_object_name = 'products'
    queryset = Product.objects.filter(archive=False)


class ProductCreateView(UserPassesTestMixin,CreateView):
    def test_func(self):
        return self.request.user.is_superuser
    

    model = Product
    fields = ('name', 'price', 'description', 'discount')
    success_url = reverse_lazy('shopapp:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'price', 'description', 'discount')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'shopapp:product_detail',
            kwargs={'pk': self.object.pk},
        )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:products_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archive = True
        self.object.save()
        return HttpResponseRedirect(success_url)

class OrderListView(LoginRequiredMixin, ListView):
    # template_name = 'shopapp/order-list.html'
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )
    context_object_name = 'orders'

class OrderDetailView(PermissionRequiredMixin,DetailView):
    permission_required = ['shopapp.view_order']
    # template_name = 'shopapp/order-detail.html'
    queryset = (
        Order.objects
        .select_related('user')
        .prefetch_related('products')
    )
    context_object_name = 'order'