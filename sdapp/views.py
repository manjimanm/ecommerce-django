from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import contact,Category,Product,Relatedimage,Cart
from .forms import SignupForm,SigninForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import decimal
from django.contrib.auth.decorators import login_required
# Create your views here.

def indexpg(request):
    return render(request,'index.html')

def regpage(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect('loginpage')
            messages.info(request,'user saved succesfully')
        else:
            messages.info(request,'invalid')
    else:
        form=SignupForm()
    context={
        'form':form
    }
    
    return render(request,'regist.html',context)

def loginpage(request):
    if request.method=='POST':
        form=SigninForm(request.POST)
        username=form['username'].value()
        password=form['password'].value()
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,'login success')
            return redirect('/')
        else:
            messages.info(request,'invalid')
    else:
        form=SigninForm()
    context={
        'form':form
    }
    return render(request,'login.html',context)

def aboutpg(request):
    return render(request,'about.html')
def blogpg(request):
    return render(request,'blog.html')
def contactpg(request):
    if request.method=="POST":
        cmail=request.POST["email"]
        sms=request.POST["msg"]
        contact(mail=cmail,msg=sms).save()
    return render(request,'contact.html')


def categorypg(request):
    ctr=Category.objects.filter(is_active=True)
    return render(request,'category.html',{'ctr':ctr})
def category_products(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=Product.objects.filter(is_active=True,category=category)
    context={
        'products':products,
    }
    return render(request,'product.html',context)
def detail_page(request,slug):
    product=get_object_or_404(Product,slug=slug,)
    relimg=Relatedimage.objects.filter(products=product.id)
    context={
        'product':product,
        'relimg':relimg,
        }
    return render(request,'product-detail.html',context)




        
@login_required
def shopcart(request):
    user=request.user
    cart_products=Cart.objects.filter(user=user)
    amount=decimal.Decimal(0)
    shipping_amount=decimal.Decimal(10)
    cp=[p for p in Cart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            temp_amount=(p.quantity*p.product.price)
            amount+=temp_amount
    context={
        'cart_products':cart_products,
        'amount':amount,
        'shipping_amount':shipping_amount,
        'total_amount':amount+shipping_amount,
    }
    return render(request,'shoping-cart.html',context)

@login_required
def add_to_cart(request):
    user=request.user
 
    product_id=request.GET.get('prod_id')
    product=get_object_or_404(Product,id=product_id)
    item_already_in_cart=Cart.objects.filter(product=product_id,user=user)
    if item_already_in_cart:
        cp=get_object_or_404(Cart,product=product_id,user=user)
        cp.quantity +=1
        cp.save()
    else:
        Cart(user=user,product=product).save()
        return redirect('shopcart')
    return redirect('shopcart')

@login_required
def pluscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.quantity += 1
        if cp.quantity>=cp.product.productStock:
            cp.quantity -= 1
        cp.save()
    return redirect('shopcart')

@login_required
def minuscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        if cp.quantity==1:
            cp.delete()
        else:
            cp.quantity-=1
            cp.save()
    return redirect('shopcart')

@login_required
def deletecart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.delete()
    return redirect('categorypg')

def logout_fn(request):
    logout(request)
    return redirect('/')

def searchpg(request):
    q=request.GET.get('q','')
    data=Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request,'search.html',{'data':data})



 
