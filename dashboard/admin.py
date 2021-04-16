from django.contrib import admin
from .models import cust_registration_table, product_table, suppliers_table, sales, accounts_table, saved_sales_data

# Register your models here.


admin.site.register(cust_registration_table)
admin.site.register(product_table)
admin.site.register(suppliers_table)
admin.site.register(sales)
admin.site.register(accounts_table)
admin.site.register(saved_sales_data)
