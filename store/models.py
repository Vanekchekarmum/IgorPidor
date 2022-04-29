from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	tel = models.CharField(max_length=200)
	def __str__(self):
		return self.name
	'''
	def __str__(self):
		template = 'Имя: {0.name} , Номер: {0.tel}'
		return template.format(self)
	'''

class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	compound = models.CharField(max_length=200)
	digital = models.BooleanField(default=False,null=True, blank=True)

	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)


	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)

	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	street = models.CharField(max_length=200, null=False)
	home = models.CharField(max_length=200, null=False)
	flat = models.CharField(max_length=200, null=False)
	porch = models.CharField(max_length=200, null=False)
	comment = models.CharField(max_length=200, null=False)
	date = models.CharField(null=True, max_length=80)
	time = models.CharField( max_length=80)
	contacts = models.CharField(max_length=80,blank=False, default='whatsapp' )
	pickup=models.CharField(max_length=80, default='доставка')
	date_added = models.DateTimeField(auto_now_add=True)
	# products = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return str(self.id)
class Comments(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='comments')
	name = models.CharField(max_length=80)
	tel = models.CharField(max_length=80)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	class Meta:
		ordering = ['created_on']


	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)