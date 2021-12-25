from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.db.models import Q
from mainapp.forms import ProductForm, CategoryForm
from mainapp.models import Product, Category
from django.utils import timezone
from datetime import timedelta
from cart.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404


class ProductCreate(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        user = self.request.user
        product = form.save(commit=False)
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductDelete(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('base')


class CategoryCreate(CreateView):
    pass
    # model = Category
    # template_name = 'add_category.html'
    # form_class = CategoryForm
    # success_url = reverse_lazy('index')


class CategoryDetailView(DetailView):
    pass
    # model = Category
    # template_name = 'category_detail.html'
    # context_object_name = 'category'
    #
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.id = kwargs.get('pk', None)
    #
    #     return super().get(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.filter(category_id=self.id)
    #     return context
    #
    # def form_valid(self, form):
    #
    #     user = self.request.user
    #     product = form.save(commit=False)
    #     product.user = user
    #     product.save()
    #     return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('base')


class ProductList(ListView):
    model = Product
    template_name = 'index.html'
    paginate_by = 3
    context_object_name = 'products'

    def get_template_names(self):
        template_name = super(ProductList, self).get_template_names()
        search = self.request.GET.get('q')
        filter = self.request.GET.get('filter')

        if search:
            template_name = 'search.html'
        elif filter:
            template_name = 'product_new.html'
        return template_name

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        global PAGE
        PAGE = context.get(("page_obj")).number
        search = self.request.GET.get('q')
        filter = self.request.GET.get('filter')
        context['is_empty'] = False

        if search:
            context['products'] = Product.objects.filter(Q(title__icontains=search) |
                                                         Q(descriptions__icontains=search))
        elif filter:
            start_date = timezone.now() - timedelta(days=1)
            context['products'] = Product.objects.filter(created_at__gte=start_date)
        return context


def ProductDetailView(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_detail.html', {'product': product, 'cart_product_form': cart_product_form})

