from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Products,Order
from .Forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    orders_count=orders.count()
    products=Products.objects.all()
    items_count=products.count()
    workers_count=User.objects.all().count()


    if request.method == 'POST' :
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            instance = form_order.save(commit=False)
            instance.staff =request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form_order = OrderForm()

    
    context = {
        'orders' :orders,
        'form_order' : form_order,
        'products' : products,
        'workers_count':  workers_count,
        'items_count':items_count,
        'orders_count':orders_count,
                }
    return render(request,'dashboard/index.html',context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = User.objects.count() 
    items_count=Products.objects.all().count()
    orders_count=Order.objects.all().count()
    context = {

        'workers' : workers,
        'workers_count':  workers_count,
        'items_count':items_count,
        'orders_count':orders_count,
    }
    return render(request,'dashboard/staff.html',context)
@login_required(login_url='user-login')
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers' : workers,
    }
    return render(request,'dashboard/staff_detail.html',context)

@login_required(login_url='user-login')
def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} a été ajouté')
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm()

    items=Products.objects.all()
    items_count=items.count()
    workers_count = User.objects.count()
    orders_count=Order.objects.all().count()
    # items= Products.objects.raw('SELECT * FROM "dashboard_products"')

    context = {
        'items' : items,
        'form' : form,
        'workers_count':workers_count,
        'items_count':items_count,
        'orders_count':orders_count,
    }
    return render(request,'dashboard/products.html', context )





@login_required(login_url='user-login')
def product_delete(request,pk):
    item = Products.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    return render(request,'dashboard/product_delete.html')




def products_update(request, pk):
    item=Products.objects.get(id =pk)
    if request.method == 'POST':
        item_form = ProductForm(request.POST,instance=item)
        if item_form.is_valid():
            item_form.save()
            return redirect('dashboard-products')
    else:
        item_form =ProductForm(instance=item)
    context = {
        'item_form':item_form,
    }
    return render(request,'dashboard/product_update.html',context)
@login_required(login_url='user-login')
def order(request):
    workers_count = User.objects.count() 
    orders=Order.objects.all()
    orders_count=orders.count()


    items_count=Products.objects.all().count()
    context = {
        'orders' : orders,
        'workers_count' : workers_count,
        'items_count':items_count,
        'orders_count':orders_count
             }


    return render(request,'dashboard/order.html',context)