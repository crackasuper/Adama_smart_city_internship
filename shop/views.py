from django.shortcuts import render, get_object_or_404

#from carts.views import cartIDs
from .models import Product
from core.models import Category
from carts.views import cart, cartIDs
#from carts.views import cartIDs
from carts.models import CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
#from carts.views import get_cart_ids

# Create your views here.

def shop(request, category_slug=None):
    cat = Category.objects.all()
    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by('id')
        count = products.count()
        paginator = Paginator(products, 1)  
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 8)
        page = request.GET.get("page")
        paged_products = paginator.get_page(page)
        count = products.count()
    return render(request, "shop.html", {"products": paged_products, "count": count, "cat": cat})

def product_detail(request, category_slug, product_slug):
    detail = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=cartIDs(request), product=detail).exists()
    return render(request, "product-detail.html", {"detail": detail, "in_cart": in_cart})

def search(request):
    context = {}
    keyword = request.GET.get('keyword')
    
    if keyword:
        products = Product.objects.order_by('created_date').filter(
            Q(product_name__icontains=keyword) | Q(description__icontains=keyword)
        )
        count = products.count()
        
        # Paginate the search results
        paginator = Paginator(products, 3)  # Display 3 products per page
        page = request.GET.get('page')
        try:
            paged_products = paginator.get_page(page)
        except PageNotAnInteger:
            paged_products = paginator.page(1)
        except EmptyPage:
            paged_products = paginator.page(paginator.num_pages)
        
        context = {
            'products': paged_products,
            'count': count,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            'keyword': keyword,
        }
    
    return render(request, "shop.html", context)
