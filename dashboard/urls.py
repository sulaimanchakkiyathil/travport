from django.urls import path


from . import views
from .views import dashboard, customers, suppliers, services, accounts, cust_reg_form, sales_function, ac_payments, \
    make_payment, ticketing, branch_based_reports, sup_make_payment, sup_payment_making

urlpatterns = [
    path('',dashboard),
    path('customers/',customers),
    path('suppliers/',suppliers),
    path('services/',services),
    path('accounts/',accounts),
    path('cust_reg/',cust_reg_form,name='cust_regist'),
    path('sales/',sales_function,name='cust_regist'),
    path('payments/',ac_payments,name='payments'),
    path('pay/<int:cust_id>',make_payment,name='make_payment'),
    path('sup_payment/',sup_make_payment,name='sup_make_payment'),
    path('sup_pay/<int:sup_id>',sup_payment_making,name='sup_make_payment'),
    path('tickets/',ticketing),
    path('branch_report/',branch_based_reports)


    ]
