from django.db import models

class Product(models.Model):
    name = models.CharField(max_length= 256, unique= True)
    description = models.TextField()
    options = models.ManytoManyField("Option")
    category = models.ManytoManyField("Category")
    unit_price = models.FloatField()
    discount_price = models.FloatField()

    def __str__(self):
        return self.name

    @property
    def price(self):
        return self.discount_price if self.discount_price else self.unit_price


class Category(models.Model):
    name = models.CharField(max_length= 256)
    slug = models.CharField(max_length= 256)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductOrder(models.Model):
    product = models.ForeignKey("Product", on_delete= models.CASCADE)
    count = models.IntegerField(default= 1)

class Order(model.Model):
    address = models.CharField(max_length= 256)
    phone_number = models.CharField(max_length= 32)
    email = models.CharField(max_length= 32)
    comment = models.TextField()
    name = models.CharField(max_length= 256)
    sname = models.CharField(max_length= 256)

    products = models.ManytoManyField("ProductOrder")

    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return "Order %i" % self.pk

    @property
    def total(self):
        return sum([po.product.price * po.count for po in products])
