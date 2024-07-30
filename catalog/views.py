from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Version


class ProductListView(ListView):
    """Контроллер для списка продуктов"""
    model = Product

    def get_context_data(self, *args, **kwargs):
        """Метод для получения списка продуктов активной версии"""
        context_data = super().get_context_data(*args, **kwargs)
        active_product_list = []
        for product in context_data['product_list']:
            product.current_version = Version.objects.filter(product=product, is_current_version=True).first()
            if product.current_version:
                product.active_version = product.current_version
                active_product_list.append(product)
        context_data['object_list'] = active_product_list
        return context_data


class ProductDetailView(DetailView):
    """Контроллер для просмотра конкретного продукта"""
    model = Product


class ProductCreateView(CreateView):
    """Контроллер для добавления нового продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    """Контроллер для редактирования продукта"""
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ContactsView(TemplateView):
    """Контроллер для страницы контактов"""
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_contacts"] = Contact.objects.all()[:5]
        return context

    def post(self, request, **kwargs):
        if request.method == 'POST':
            contact = Contact()
            contact.name = request.POST.get('name')
            contact.phone = request.POST.get('phone')
            contact.message = request.POST.get('message')
            contact.save()

        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)
