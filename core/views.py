from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import *
from django.contrib import messages as alert
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    products = Product.objects.all()
    context={'products': products}
    return render(request, 'frontend/home.html', context)



@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_quantity = sum(item.quantity for item in cart_items)
    context = {'cart_items': cart_items, 'total_quantity': total_quantity}
    return render(request, 'cart/cart.html', context)

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id)
    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('cart')



    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'frontend/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'frontend/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('home')  


@login_required(login_url='admin-login')
def admin_home(request):
    if request.user.is_superuser:
        products = Product.objects.all()
        users_count = User.objects.all().count()
        products_count = Product.objects.all().count()
        context = {'products': products, 'products_count': products_count, 'users_count': users_count}
        return render(request, 'backend/home.html', context)
    else:
        return redirect('admin-login')


def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:
                login(request, user)
                alert.success(request, 'Login Successfully')
                return redirect('dashboard')  
            else:
                alert.error(request, 'You have not permission to Admin Panel')
                return redirect('admin-login')
        else:
            alert.error(request, 'User not found')
            return redirect('admin-login')

    form = LoginForm()
    return render(request, 'backend/login.html', {'form': form})




@login_required(login_url='admin-login')
def add_product(request):
    if request.user.is_superuser:
        form = ProductForm
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                alert.success(request, 'Product Added Successfully')
                return redirect('dashboard')
            else:
                alert.error(request, 'Something went Wrong !')
                return redirect('add-product')
        context = {'form': form}
        return render(request, 'backend/add-product.html', context)
    else:
        return redirect('admin-login')



@login_required(login_url='admin-login')
def edit_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.user.is_superuser:
        form = ProductForm(instance=product)
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                alert.success(request, 'Product Updated Successfully')
                return redirect('dashboard')
            else:
                alert.error(request, 'Something went Wrong !')
                return redirect('edit-product')
        context = {'form': form, 'product':product}
        return render(request, 'backend/edit-product.html', context)
    else:
        return redirect('admin-login')


@login_required(login_url='admin-login')
def delete_product(request, pk):
    if request.user.is_superuser:
        product = Product.objects.get(id=pk)
        product.delete()
        alert.success(request, "Product Deleted Successfully")
        return redirect('dashboard')
    else:
        return redirect('admin-login')



# logout 
@login_required(login_url='login')
def logout_user(request):
    if request.user.is_superuser:
        logout(request)
        print(request.user.is_superuser)
        alert.success(request, "Sign Out")
        return redirect('admin-login')
    else:
        logout(request)
        print(request.user.is_superuser)
        alert.success(request, "Sign Out")
        return redirect('login')