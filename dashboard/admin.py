from django.contrib import admin
from .models import cust_registration_table, product_table, suppliers_table,sales

# Register your models here.


admin.site.register(cust_registration_table)
admin.site.register(product_table)
admin.site.register(suppliers_table)
admin.site.register(sales)
