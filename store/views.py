from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder, guestComment
from .forms import CommentForm

def store(request):
	category = request.GET.get('category')
	if category == None:
		products = Product.objects.all()
	else:
		products = Product.objects.filter(category__name = category)

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	categories = Category.objects.all()
	context = {'products':products, 'cartItems':cartItems, 'categories': categories}
	return render(request, 'store/store.html', context)

def index(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/jega.html', context)
def about(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/about.html', context)
def category(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/category.html', context)
def feedback(request, pk):
	data = cartData(request)
	feedback = Comments.object.get(id=pk)
	if request.method == 'POST':
		feedback = Comments.objects.get(id=pk)
		try:
			customer = request.user.customer
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)
	context = {}
	return render(request, 'store/feedback.html', context)
def product(request, pk):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	product = Product.objects.get(id=pk)
	comments  = product.comments.all()
	new_comment = None

	if request.method == 'POST':
		product = Product.objects.get(id=pk)
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():

			new_comment = comment_form.save(commit=False)
			new_comment.product = product
			new_comment.save()

		#Get user account information
		# try:
		# 	customer = request.user.customer
		# except:
		# 	# device = request.COOKIES['device']
		# 	# customer, created = Customer.objects.get_or_create()
		#
		# order, created = Order.objects.get_or_create(customer=customer, complete=False)
		# orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
		# orderItem.quantity=request.POST['quantity']
		# orderItem.save()
	else:
		comment_form = CommentForm()

	context = {'product':product, 'items':items, 'order':order, 'cartItems':cartItems, 'comments': comments,'new_comment': new_comment,'comment_form': comment_form}
	return render(request, 'store/product.html', context)

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		street=data['shipping']['street'],
		flat=data['shipping']['flat'],
		home=data['shipping']['home'],
		porch=data['shipping']['porch'],
		comment=data['shipping']['comment'],
		date=data['shipping']['date'],
		time=data['shipping']['time'],
		contacts=data['shipping']['contacts'],
		pickup=data['shipping']['pickup'],
		)


	return JsonResponse('Payment submitted..', safe=False)
def processComment(request):
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestComment(request, data)

	if order.comment == True:
		Comments.objects.create(
		customer=customer,
		body=data['comment']['body'],
		)


	return JsonResponse('Payment submitted..', safe=False)