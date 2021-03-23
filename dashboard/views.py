import math

from django.shortcuts import render, redirect

# Create your views here.
from dashboard.forms import cust_registration_form
from dashboard.models import cust_registration_table, product_table, suppliers_table, sales, accounts_table


def dashboard(request):

    return render(request,'dashboard.html')

def customers(request):

    return render(request,'customers.html')

def suppliers(request):

    if request.method=='POST':
        sup_name = request.POST['name']
        sup_address = request.POST['address']
        sup_contact = request.POST['contact']
        sup_contact2 = request.POST['alt_contact']
        sup_email = request.POST['sup_email']
        web = request.POST['sup_web']
        sup_table=suppliers_table(sup_name=sup_name,sup_address=sup_address,sup_contact=sup_contact,sup_contact2=sup_contact2,sup_email=sup_email,web=web)
        sup_table.save()

    return render(request,'suppliers.html')

def services(request):
    sales_table=sales.objects.all()



    return render(request,'dash_services.html',{'sales':sales_table})

def accounts(request):

    return render(request,'accounts.html')

def cust_reg_form(request):
    form=cust_registration_table()
    if request.method=='POST':
        cust_data=cust_registration_table(fname=request.POST['fname'],lname=request.POST['lname'],address=request.POST['address'],contact1=request.POST['contact1'],alt_contact=request.POST['alt_contact'],dest_contact=request.POST['dest_contact'],email=request.POST['email'],ref_person_name=request.POST['ref_person_name'],ref_person_contact=request.POST['ref_person_contact'],passport_no=request.POST['passport_no'],dob=request.POST['dob'])
        cust_data.save()
        return redirect(cust_reg_form)

    return render(request,'cust_reg_form.html',{'reg_form':form})

def sales_function(request):
    customers=cust_registration_table.objects.all()
    products=product_table.objects.all()
    suppliers=suppliers_table.objects.all()

    if request.method=='POST':
        product_id=100
        customer_name_with_id = request.POST['customer_name']
        customer_name_array=customer_name_with_id.split("-")
        customer_name=customer_name_array[1]
        cust_id=customer_name_array[0]

        #product_id = request.POST['product_id']
        service = request.POST['service']
        supplier = request.POST['supplier']
        supplier_name_array = supplier.split("-")
        supplier_name = supplier_name_array[1]
        supplier_id = supplier_name_array[0]

        sales_rate = request.POST['sales_rate']
        purchase_rate = request.POST['purchase_rate']
        if purchase_rate == "":
            purchase_rate = 0
        passport_no=request.POST['passport number']
        passport_expiry1 = request.POST.get('passport_expiry1')
        dob=request.POST['dob']
        sales_table=sales(cust_id=cust_id,cust_name=customer_name,product_id=product_id,product_name=service,sup_name=supplier_name,sales_price=sales_rate,purchase_rate=purchase_rate,sup_id=supplier_id)
        sales_table.save()

        customer_update_table=cust_registration_table.objects.get(id=cust_id)
        customer_update_table.passport_no=passport_no
        customer_update_table.passport_expiry=passport_expiry1
        customer_update_table.dob=dob
        customer_update_table.save()


        accounts = accounts_table(cust_id=cust_id, ac_discription=service)
        accounts.save()




    return render(request,'sales.html',{'customers':customers,'products':products,'suppliers':suppliers})

def ac_payments(request):
    customers = cust_registration_table.objects.all()
    selected_customer_info = ""
    customer_dues = {
        "dues": ""
    }

    if request.method=="POST":
        #selected_customer = request.POST.get('payment_customer', False)
        selected_customer = request.POST['payment_customer']
        selected_customer_ary=selected_customer.split('-')
        customer_id=selected_customer_ary[0]
        #customer_id1=1

        selected_customer_info = cust_registration_table.objects.filter(id=customer_id)

        accounts = accounts_table.objects.filter(cust_id=customer_id)
        debit = []
        credit = []
        for account in accounts:
            debit.append(account.ac_debit)
            credit.append(account.ac_credit)

        cust_total_debit = sum(debit)
        cust_total_credit = sum(credit)
        cust_total_dues = cust_total_debit - cust_total_credit

        customer_dues = {
            "dues": cust_total_dues
        }

        print("total due is :")

        print(cust_total_dues)
    return render(request,'ac_payments.html',{'customers':customers,'selected_customer_info':selected_customer_info,'customer_dues':customer_dues})

def make_payment(request,cust_id):
    accounts=accounts_table.objects.filter(cust_id=cust_id)
    debit=[]
    credit=[]
    for account in accounts:
        debit.append(account.ac_credit)
        credit.append(account.ac_debit)
    cust_total_credit=sum(credit)
    cust_total_debit=sum(debit)
    cust_total_dues=cust_total_credit-cust_total_debit
    print("total due is :")
    print(cust_total_dues)

    if request.method=='POST':
        discription = request.POST['discription']
        #print(type(request.POST['payment_amount']))
        ac_credit = float(request.POST['payment_amount'])
        print(type(ac_credit))
        if ac_credit=="":
            ac_credit=0
        p_ref = request.POST['transaction_id']
        accounts=accounts_table(cust_id=cust_id,ac_discription=discription,ac_credit=ac_credit,p_ref=p_ref,ac_ref='customer_payment')
        accounts.save()

    return render(request,'make_payment.html')

def sup_make_payment(request):
    suppliers=suppliers_table.objects.all()
    selected_suppliers_info =''
    supplier_due=0

    if request.method=="POST":
        sup_payments=[]
        #selected_customer = request.POST.get('payment_customer', False)
        selected_customer = request.POST['payment_supplier']
        selected_customer_ary=selected_customer.split('-')
        supplier_id=selected_customer_ary[0]
        supplier_name=selected_customer_ary[1]
        selected_suppliers_info = suppliers_table.objects.filter(id=supplier_id)
        total_sup_payments=sales.objects.filter(sup_id=supplier_id)
       
        for payments in total_sup_payments:
            sup_payments.append(payments.purchase_rate)
            total_sup_payments=sum(sup_payments)
        supplier_paid=[]
        total_sup_paid=accounts_table.objects.filter(sup_id=supplier_id)
        print(total_sup_paid)
        for payments in total_sup_paid:
            supplier_paid.append(payments.ac_debit)
        supplier_paid_total=sum(supplier_paid)
        print(type(total_sup_payments))
        print("supplier total :"+str(total_sup_payments))
        supplier_due=total_sup_payments-supplier_paid_total
        print(supplier_due)

    return render(request,'sup_make_payment.html',{'suppliers':suppliers,'selected_suppliers':selected_suppliers_info,'supplier_due':supplier_due})
def sup_payment_making(request,sup_id):

    if request.method == 'POST':
        discription = request.POST['sup_discription']
        ac_debit = request.POST['sup_payment_amount']
        if ac_debit == "":
            ac_debit = 0
        p_ref = request.POST['sup_transaction_id']

        accounts = accounts_table(sup_id=sup_id, ac_discription=discription, ac_debit=ac_debit, p_ref=p_ref,
                                  ac_ref='Supplier Payment')
        accounts.save()

    return render(request,'sup_payment_making.html')
def ticketing(request):
    customers = cust_registration_table.objects.all()
    products = product_table.objects.all()
    suppliers = suppliers_table.objects.all()

    if request.method=='POST':
        product_id=100
        customer_name_with_id = request.POST['customer_name']
        customer_name_array=customer_name_with_id.split("-")
        customer_name=customer_name_array[1]
        cust_id=customer_name_array[0]

        #product_id = request.POST['product_id']
        service = request.POST['service']
        supplier = request.POST['supplier']
        supplier_name_array = supplier.split("-")
        supplier_name = supplier_name_array[1]
        supplier_id = supplier_name_array[0]

        sales_rate = request.POST['ticket_fare']
        purchase_rate = request.POST['purchase_rate']
        #if not purchase_rate==int or purchase_rate==float :
        if purchase_rate == "" :
            purchase_rate=0
        passport_no=request.POST['passport number']
        passport_expiry1 = request.POST.get('passport_expiry1')

        sales_table=sales(cust_id=cust_id,cust_name=customer_name,product_id=product_id,product_name=service,sup_name=supplier_name,sales_price=sales_rate,purchase_rate=purchase_rate,sup_id=supplier_id)
        sales_table.save()

        accounts = accounts_table(cust_id=cust_id, ac_discription=service, ac_debit=sales_rate)
        accounts.save()

    return render(request,'ticketing.html',{'customers':customers,'products':products,'suppliers':suppliers})

def branch_based_reports(request):

    total_90D_visas=sales.objects.filter()
    total_sales=[]
    total_purchases=[]
    for visas90d in total_90D_visas:
        total_sales.append(visas90d.sales_price)

        total_purchases.append(visas90d.purchase_rate)
    total_sales_sales_price=sum(total_sales)
    total_purchase_coast=sum(total_purchases)
    nos=len(total_sales)


    total_payment_recieved = accounts_table.objects.filter(ac_ref='customer_payment')
    cust_payments = []
    for cust_payment in total_payment_recieved:
        cust_payments.append(cust_payment.ac_credit)
    cust_payments_total=sum(cust_payments)

    pay_pendings=(total_sales_sales_price-cust_payments_total)

    #pay_pendings="100"

    total_supplier_payments = accounts_table.objects.filter(ac_ref='Supplier Payment')
    sup_payments = []
    for sup_payment in total_supplier_payments:
        sup_payments.append(sup_payment.ac_debit)
    sup_payments_total = sum(sup_payments)

    sup_dues=total_purchase_coast-sup_payments_total
    exp_income=total_sales_sales_price-total_purchase_coast
    net_income=cust_payments_total-total_purchase_coast



    sales_info={
        'total_sales':total_sales_sales_price,
        'total_service_purchase_coast':total_purchase_coast,
        'nos':nos,
        'total_cust_payments':cust_payments_total,
        'total_cust_pending':pay_pendings,
        'sup_paid_total':sup_payments_total,
        'sup_dues':sup_dues,
        'exp_income':exp_income,
        'net_income':net_income,

    }



    #return render(request,'branch_based_reports.html',{'total_90s':visa_90_days_total_sales_price,'purchase90':visa_90_days_total_purchase_coast,'nos':nos})
    return render(request,'branch_based_reports.html',{'sales':sales_info})