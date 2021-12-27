from django.db import models

# Create your models here.
class InvoiceUser(models.Model):
    name = models.CharField(max_length =600)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length =900,unique = True)
    address = models.TextField(max_length =5000,null=True,blank=True)
    
class Service(models.Model):
    title = models.CharField(max_length =600,db_index = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    cost = models.FloatField(default=0)
    
class Invoice(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(InvoiceUser,on_delete=models.CASCADE,related_name="clientinvoices")
    biller = models.ForeignKey(InvoiceUser,on_delete=models.CASCADE,related_name="billerinvoices")
    services = models.ManyToManyField(Service,related_name="serviceinvoices")
    tax_percent = models.FloatField(default=0)
    bank_details = models.TextField(max_length=4000)

    
    
    
