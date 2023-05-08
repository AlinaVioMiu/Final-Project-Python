from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import homepage_view, CategoryDetailView, ProductListView, ProductDetailView


class TestUrls(SimpleTestCase):
    def test_homepage_url(self):
        url = reverse('homepage')
        print(resolve(url))
        self.assertEquals(resolve(url).func, homepage_view)

    def test_category_detail_url_resolves(self):
        url = reverse('category_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CategoryDetailView)

    def test_product_list_url_resolves(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProductListView)

    def test_product_detail_url_resolves(self):
        url = reverse('product_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)
