from django.db import models

# Create your models here.

class cust_registration_table(models.Model):
    fname=models.CharField(max_length=24,default=0,blank=True)
    lname=models.CharField(max_length=24,default=0,blank=True)
    address=models.CharField(max_length=253,default=0,blank=True)
    contact1=models.CharField(max_length=24,blank=True,default=0)
    alt_contact = models.CharField(max_length=24,blank=True,default=0)
    dest_contact = models.CharField(max_length=24,blank=True,default=0)
    dest_ref=models.CharField(max_length=256,default=0,blank=True)
    email=models.EmailField(blank=True)
    ref_person_name=models.CharField(max_length=225,default=0,blank=True)
    ref_person_contact=models.CharField(max_length=225,default=0,blank=True)
    home_address=models.CharField(max_length=225,default=0,blank=True)
    description=models.CharField(max_length=225,default=0,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    passport_no=models.CharField(max_length=16,blank=True)
    dob=models.DateField(blank=True,null=True)
    passport_expiry=models.DateField(blank=True,null=True)
    uid=models.CharField(max_length=36,blank=True)




class product_table(models.Model):
    p_name=models.CharField(max_length=225,blank=True)

class suppliers_table(models.Model):
    sup_name=models.CharField(max_length=225,blank=True)
    sup_address=models.TextField(blank=True)
    sup_contact=models.IntegerField(blank=True)
    sup_contact2 = models.IntegerField(blank=True)
    sup_email=models.EmailField(blank=True)
    web=models.CharField(max_length=225,blank=True)

class sales(models.Model):
    sales_date=models.DateTimeField(auto_now_add=True)
    cust_name=models.CharField(max_length=225,blank=True)
    cust_id=models.IntegerField(blank=True,default=0)
    product_id=models.IntegerField(blank=True,default=0)
    product_name=models.CharField(max_length=225,blank=True,default=0)
    sup_name=models.CharField(max_length=225,blank=True,default=0)
    sup_id=models.IntegerField(blank=True,default=0)
    purchase_rate = models.FloatField(blank=True,default=0)
    sales_price=models.FloatField(blank=True,default=0)
    paid_amount=models.FloatField(blank=True,default=0)
    balance=models.FloatField(blank=True,default=0)

class accounts_table(models.Model):
    ac_date=models.DateTimeField(auto_now_add=True)
    ac_ref=models.CharField(max_length=10,blank=True,default=0)
    cust_id=models.IntegerField(blank=True,default=0)
    sup_id=models.IntegerField(blank=True,default=0)
    ac_discription=models.CharField(max_length=225)
    ac_debit=models.FloatField(null=True)
    ac_credit=models.FloatField(null=True)
    ac_balance=models.FloatField(blank=True,default=0)
    p_ref=models.CharField(max_length=225,blank=True)











