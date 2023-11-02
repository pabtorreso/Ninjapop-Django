from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from .forms import UserForm, SuperuserCreationForm, UserEditForm, ProductForm, RegistrationForm
from .models import Product, Cart, CartItem

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def buscar_productos(request):
    q = request.GET.get('q')
    if q:
        # Realizar la búsqueda y obtener los resultados
        resultados = Product.objects.filter(nombre__icontains=q).order_by('id')
        paginator = Paginator(resultados, 6)  # Mostrar 6 productos por página

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'resultados': page_obj, 'q': q}
        return render(request, 'buscar.html', context)
    else:
        resultados = []
    context = {'resultados': resultados, 'q': q}
    return render(request, 'buscar.html', context)

def catalogo(request):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 6)  # Mostrar 6 productos por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }
    return render(request, 'catalogo.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_panel' if user.is_staff else 'index')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página de registro exitoso
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_panel(request):
    return render(request, 'admin_panel.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def user_panel(request):
    users = User.objects.all()
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_panel')

    context = {
        'users': users,
        'form': form
    }
    return render(request, 'user_panel.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def product_panel(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_panel')

    context = {
        'product_list': products,
        'form': form
    }
    return render(request, 'product_panel.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_panel')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_panel')
    return render(request, 'delete_user.html', {'user': user})

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_superuser(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_panel')
    else:
        form = SuperuserCreationForm()
    return render(request, 'create_superuser.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_user(request, user_id=None):
    user = None

    if user_id:
        user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('user_panel')
    else:
        form = UserEditForm(instance=user)

    context = {
        'form': form,
        'user_id': user_id,
    }

    return render(request, 'edit_user.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_panel')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'create_product.html', context)

@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_panel')
    else:
        form = ProductForm(instance=product)

    context = {
        'form': form,
        'product_id': product_id,
    }

    return render(request, 'edit_product.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_panel')
    return render(request, 'delete_product.html', {'product': product, 'product_id': product.id})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def carrito(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    
    # Realizar cálculos
    total_quantity = cart.get_total_quantity()
    total_price = calculate_total_price(cart)  # Calcula el precio total
    shipping_cost = 5000  # costo de envío fijo
    discount = 0  # descuento
    discounted_total = total_price + shipping_cost - discount
    
    context = {
        'cart': cart,
        'total_quantity': total_quantity,
        'total_price': total_price,
        'shipping_cost': shipping_cost,
        'discount': discount,
        'discounted_total': discounted_total,
    }
    
    return render(request, 'carrito.html', context)

def calculate_total_price(cart):
    total_price = 0
    for item in cart.cartitem_set.all():
        total_price += item.subtotal
    return total_price


@require_POST
def agregar_al_carrito(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Si el artículo ya está en el carrito, aumenta la cantidad
    if not item_created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1

    # Actualiza el subtotal
    cart_item.subtotal = cart_item.quantity * product.precio
    cart_item.save()

    return redirect('carrito')

def modificar_cantidad(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cantidad = int(request.POST.get('cantidad', 1))

    if cantidad < 1:
        # Si la cantidad es menor a 1, se establece en 1 como mínimo
        cantidad = 1

    cart_item.quantity = cantidad
    cart_item.subtotal = cart_item.quantity * cart_item.product.precio
    cart_item.save()

    return redirect('carrito')


def eliminar_producto(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()

    return redirect('carrito')

def acerca(request):
    template_name = "acerca.html"
    return render(request, template_name)

def contacto(request):
    template_name = "contacto.html"
    return render(request, template_name)

def faq(request):
    template_name = "faq.html"
    return render(request, template_name)


