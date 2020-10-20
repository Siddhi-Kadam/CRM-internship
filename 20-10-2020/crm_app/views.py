from django.shortcuts import render, redirect
from customer.models import uploads,loan_details, credit_details
from .models import customer_type, bank_name, cocat_type, company_type, salary_type, residence_type, designation, product_policy
from .models import loan_type, bank_cat, tenure, product_and_policy
from .models import prod_policy_master, pp_company_type, pp_salary_type, pp_residence_type, pp_max_age
from .models import pp_cibil, pp_tenure, pp_cocat_type,reasons, pp_foir
#import pyautogui

# Create your views here.

def not_listed(request):
    a = uploads.objects.all()
    l=[]
    for i in a:
        if (i.paid_up_cap!='') or (i.company_yrs!='') or (i.nature_company!=''):
            s = uploads.objects.get(id=i.id)
            l.append(s)
    return render(request, 'not_listed.html', {'alldata':l})

def dash(request):
    return render(request, 'crm_dashboard.html')

def log(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        passw = request.POST.get('passw')
        if user == 'admin' and passw == 'admin':
            #pyautogui.alert("Logged In..")
            return render(request, 'crm_dashboard.html')
        else:
            #pyautogui.alert("Wrong Credentials..")
            return render(request, 'login.html')

def customer(request):
    a = uploads.objects.all()
    return render(request, 'crm_customer.html', {'alldata': a})

def logout(request):
    return render(request, )

def master_cust_type(request):
    a = customer_type.objects.all()
    return render(request, 'master_cust_type.html', {'alldata': a})



def add_cust_type(request):
    return render(request, 'add_cust_type.html')

def add_prd_ply(request):
    cust_type = customer_type.objects.all()
    l_type = loan_type.objects.all()
    bank = bank_name.objects.all()
    s_type = salary_type.objects.all()
    res_type = residence_type.objects.all()
    des_type = designation.objects.all()
    com_type = company_type.objects.all()
    cocatt_type = cocat_type.objects.all()
    tenures = tenure.objects.all()

    return render(request, 'add_prd_ply.html', {'cust_type': cust_type, 'l_type': l_type,'bank': bank, 's_type': s_type, 'res_type': res_type, 'des_type': des_type, 'com_type': com_type, 'cocatt_type': cocatt_type, 'tenures': tenures})


def prd_ply_edit(request, id):
    prd = product_policy.objects.get(id=id)
    cust_type = customer_type.objects.all()
    l_type = loan_type.objects.all()
    bank = bank_name.objects.all()
    s_type = salary_type.objects.all()
    res_type = residence_type.objects.all()
    des_type = designation.objects.all()
    com_type = company_type.objects.all()
    return render(request, 'prd_ply_edit.html', {'prd': prd, 'cust_type': cust_type, 'l_type': l_type,'bank': bank, 's_type': s_type, 'res_type': res_type, 'des_type': des_type, 'com_type': com_type})


def load_company(request):
    bank_name = request.GET.get('bank')
    companies = bank_cat.objects.filter(bank_name = bank_name)

    return render(request, 'company_dropdown.html',{'companies': companies})

def load_cocat(request):
    co_name = request.GET.get('company')
    cocats = bank_cat.objects.filter(co_name = co_name)

    return render(request, 'cocat_dropdown.html',{'cocats': cocats})

def add_cust_type_table(request):
    if request.method == 'POST':
        cust_type = request.POST.get('cust_type')
        o = customer_type(type=cust_type)
        o.save()
        #pyautogui.alert("Upload Done")
    a = customer_type.objects.all()
    return render(request, 'master_cust_type.html', {'alldata': a})

def master_loan_type(request):
    a = loan_type.objects.all()
    return render(request, 'master_loan_type.html', {'alldata': a})

def add_loan_type(request):
    return render(request, 'add_loan_type.html')

def add_loan_type_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = loan_type(loan_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    a = loan_type.objects.all()
    return render(request, 'master_loan_type.html', {'alldata': a})

def master_bank_name(request):
    a = bank_name.objects.all()
    return render(request, 'master_bank_name.html', {'alldata': a})

def add_bank_name(request):
    return render(request, 'add_bank_name.html')

def add_prd_ply_table(request):
    try:
        if request.method == 'POST':
            cust_type = request.POST.get('cust_type')
            loan_type = request.POST.get('loan_type')
            bank_name = request.POST.get('bank_name')
            company_name = request.POST.get('company_name')
            cocat_type = request.POST.get('cocat_type')
            loan_co_category = request.POST.get('loan_cocat')
            gross_salary = request.POST.get('gross_salary')
            net_salary = request.POST.get('net_salary')
            company_type = request.POST.get('company_type')
            salary_acc = request.POST.get('salary_acc')
            salary_type = request.POST.get('salary_type')
            res_type = request.POST.get('res_type')
            designation = request.POST.get('designation')
            min_age = request.POST.get('min_age')
            max_age = request.POST.get('max_age')
            current_exp = request.POST.get('current_exp')
            total_exp = request.POST.get('total_exp')
            cibil_score = request.POST.get('cibil_score')
            tenure = request.POST.get('tenure')
            abc = product_policy(cust_type=cust_type, loan_type=loan_type, bank_name=bank_name, 
            co_category=cocat_type, company_name=company_name, salary_type=salary_type, 
            designation=designation, min_age=min_age, max_age=max_age, current_exp=current_exp, 
            total_exp=total_exp, cibil=cibil_score, tenure=tenure, loan_co_category=loan_co_category, gross_salary=gross_salary,
            net_salary=net_salary,salary_acc=salary_acc, res_type=res_type, company_type=company_type)
            abc.save()
        
        a = product_policy.objects.all()
        return render(request, 'master_product_policy.html', {'a': a})
    except:
        return render(request, 'failure.html')

def add_prd_ply_table1(request):
    cust_type = request.POST.get('cust_type')
    loan_type = request.POST.get('loan_type')
    bank_name = request.POST.get('bank_name')
    salary_acc = request.POST.get('salary_acc')
    designation = request.POST.get('designation')
    min_age = request.POST.get('min_age')
    max_age = request.POST.get('max_age')
    current_exp = request.POST.get('current_exp')
    cibil_score = request.POST.get('cibil_score')
    roi_from = request.POST.get('min_roi')
    roi_to = request.POST.get('max_roi')
    effective_date = request.POST.get('effective_date')
    ineffective_date = request.POST.get('ineffective_date')
    cocat_type_ = request.POST.getlist('cocat_type')
    co_type = request.POST.getlist('company_type')
    salary_type_ = request.POST.getlist('salary_type')
    res_type_ = request.POST.getlist('res_type')
    tenure_ = request.POST.getlist('tenure')

    abc = product_and_policy.objects.create(cust_type=cust_type, loan_type=loan_type, bank_name=bank_name,
    salary_acc=salary_acc, designation=designation, min_age=min_age, max_age=max_age, current_exp=current_exp, cibil_scroe=cibil_score,
    roi_from=roi_from, roi_to=roi_to, effective_date=effective_date, ineffective_date=ineffective_date)

    for i in cocat_type_:
        abcd = cocat_type.objects.filter(c_type=i).values('id')
        abc.cocat_type.add(abcd)

    for i in co_type:
        abcd = company_type.objects.filter(co_type=i).values('id')
        abc.company_type.add(abcd)

    for i in salary_type_:
        abcd = salary_type.objects.filter(s_type=i).values('id')
        abc.salary_type.add(abcd)

    for i in res_type_:
        abcd = residence_type.objects.filter(r_type=i).values('id')
        abc.residence_type.add(abcd)

    for i in tenure_:
        abcd = tenure.objects.filter(tenure=i).values('id')
        abc.tenure.add(abcd)

    return redirect('crm_app/master_product_policy')


def add_prod_policy_table(request):
    if request.method=="POST":
        cust_type = request.POST.get('cust_type')
        loan_type = request.POST.get('loan_type')
        bank_name = request.POST.get('bank_name')
        salary_acc = request.POST.get('salary_acc')
        designation = request.POST.get('designation')
        min_age = request.POST.get('min_age')
        max_age = request.POST.get('max_age')
        current_exp = request.POST.get('current_exp')
        cibil_score = request.POST.getlist('cibil_score')
        max_age_n = request.POST.getlist('max_age_n')
        roi = request.POST.get('min_roi')
        effective_date = request.POST.get('effective_date')
        ineffective_date = request.POST.get('ineffective_date')
        cocat_type_ = request.POST.getlist('cocat_type')
        min_loan_amount = request.POST.getlist('min_loan_amt')
        max_loan_amount = request.POST.getlist('max_loan_amt')
        co_type = request.POST.getlist('company_type')
        salary_type_ = request.POST.getlist('salary_type')
        res_type_ = request.POST.getlist('res_type')
        tenure_ = request.POST.getlist('tenure')
        cocat_no_ = request.POST.getlist('cocat_no')
        salary_exist = request.POST.get('salary_exist')
        salary_new = request.POST.get('salary_new')
        try:
            obj = prod_policy_master.objects.latest('id')
            pp_id = obj.id+1
        except prod_policy_master.DoesNotExist:
            pp_id = 1


        abc = prod_policy_master(id=pp_id, prod_name=loan_type, bank_names=bank_name, type_of_cust=cust_type, 
        salary_acc=salary_acc,salary_exist=salary_exist,salary_new=salary_new, designs=designation, min_age=min_age, max_age=max_age, current_exp=current_exp,
        roi=roi, eff_date=effective_date, ineff_date=ineffective_date, pp_id=pp_id,multiplier='',foir='',both='yes')

        abc.save()

        for i in co_type:
            abc = pp_company_type(comp_type=i, effec_date=effective_date,
            ineffec_date=ineffective_date, ppid_id=pp_id)
            abc.save()

        for (i,j,k,l) in zip(cocat_type_, min_loan_amount, max_loan_amount, cocat_no_):
            abc = pp_cocat_type(cocat_no=l, cocat_types=i, min_loan_amt=j, max_loan_amt=k,
            effec_date6=effective_date, ineffec_date6=ineffective_date, ppid6_id=pp_id)
            abc.save()

        for i in res_type_:
            abc = pp_residence_type(res_type=i, effec_date2=effective_date,
            ineffec_date2=ineffective_date, ppid2_id=pp_id)
            abc.save()

        for i in salary_type_:
            abc = pp_salary_type(sal_type=i, effec_date1=effective_date,
            ineffec_date1=ineffective_date, ppid1_id=pp_id)
            abc.save()

        for i in tenure_:
            abc = pp_tenure(ten_type=i, effec_date5=effective_date,
            ineffec_date5=ineffective_date, ppid5_id=pp_id)
            abc.save()

        for i in cibil_score:
            abc = pp_cibil(cibil_type=i, effec_date4=effective_date,
            ineffec_date4=ineffective_date, ppid4_id=pp_id)
            abc.save()

        for i in max_age_n:
            abc = pp_max_age(max_type=i, effec_date3=effective_date, ineffec_date3=ineffective_date,
            ppid3_id=pp_id)
            abc.save()

        return redirect('crm_app/master_product_policy')



def prd_ply_edit_table(request):
    try:
        if request.method == 'POST':
            cust_type = request.POST.get('cust_type')
            loan_type = request.POST.get('loan_type')
            bank_name = request.POST.get('bank_name')
            company_name = request.POST.get('company_name')
            cocat_type = request.POST.get('cocat_type')
            loan_co_category = request.POST.get('loan_cocat')
            gross_salary = request.POST.get('gross_salary')
            net_salary = request.POST.get('net_salary')
            company_type = request.POST.get('company_type')
            salary_acc = request.POST.get('salary_acc')
            salary_type = request.POST.get('salary_type')
            res_type = request.POST.get('res_type')
            designation = request.POST.get('designation')
            min_age = request.POST.get('min_age')
            max_age = request.POST.get('max_age')
            current_exp = request.POST.get('current_exp')
            total_exp = request.POST.get('total_exp')
            cibil_score = request.POST.get('cibil_score')
            tenure = request.POST.get('tenure')
            pid = request.POST.get('id')

            abc = product_policy.objects.get(id=pid)
            abc.cust_type=cust_type
            abc.bank_name=bank_name
            abc.co_category=cocat_type
            abc.company_name=company_name
            abc.salary_type=salary_type
            abc.designation=designation
            abc.min_age=min_age
            abc.max_age=max_age
            abc.current_exp=current_exp
            abc.total_exp=total_exp
            abc.cibil=cibil_score
            abc.tenure=tenure
            abc.loan_co_category=loan_co_category
            abc.gross_salary=gross_salary
            abc.net_salary=net_salary
            abc.salary_acc=salary_acc
            abc.res_type=res_type
            abc.company_type=company_type
            abc.save()
        
        a = product_policy.objects.all()
        return redirect('crm_app/master_product_policy')
    except:
        return render(request, 'failure.html')

def add_bank_name_table(request):
    if request.method == 'POST':
        name = request.POST.get('bank_name')
        o = bank_name(b_name=name)
        o.save()
        #pyautogui.alert("Upload Done")
    a = bank_name.objects.all()
    return render(request, 'master_bank_name.html', {'alldata': a})

def master_cocat_type(request):
    a = pp_cocat_type.objects.all()
    return render(request, 'master_cocat_type.html', {'alldata': a})

def add_cocat_type(request):
    return render(request, 'add_cocat_type.html')

def add_cocat_type_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = cocat_type(c_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    a = cocat_type.objects.all()
    return render(request, 'master_cocat_type.html', {'alldata': a})



def master_company_type(request):
    a = pp_company_type.objects.all()
    return render(request, 'master_company_type.html', {'alldata': a})

def add_company_type(request):
    return render(request, 'add_company_type.html')

def add_company_type_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = company_type(co_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    a = company_type.objects.all()
    return render(request, 'master_company_type.html', {'alldata': a})

def master_salary_type(request):
    a = pp_salary_type.objects.all()
    return render(request, 'master_salary_type.html', {'alldata': a})

def add_salary_type(request):
    return render(request, 'add_salary_type.html')

def add_salary_type_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = salary_type(s_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    a = salary_type.objects.all()
    return render(request, 'master_salary_type.html', {'alldata': a})



def add_residence_type(request):
    return render(request, 'add_residence_type.html')

def add_residence_type_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = residence_type(r_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    a = residence_type.objects.all()
    return render(request, 'master_residence_type.html', {'alldata': a})

def master_designation(request):
    a = designation.objects.all()
    return render(request, 'master_designation.html', {'alldata': a})

def add_designation(request):
    return render(request, 'add_designation.html')

def add_designation_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = designation(design=type)
        o.save()
        #pyautogui.alert("Upload Done")
    a = designation.objects.all()
    return render(request, 'master_designation.html', {'alldata': a})

def master_bank_cat(request):
    a = bank_cat.objects.all()
    return render(request, 'master_bank_cat.html', {'alldata': a})

def add_bank_cat(request):
    a = cocat_type.objects.all()
    b = bank_name.objects.all()
    return render(request, 'add_bank_cat.html', {'cname': a, 'bname': b})

def bank_cat_delete(request, id):
	m = bank_cat.objects.get(pk=id).delete()
	return redirect('/crm_app/master_bank_cat')

def add_bank_cat_table(request):
    if request.method == 'POST':
        bank_name = request.POST.get('bank_name')
        co_name = request.POST.get('co_name')
        cat = request.POST.get('cat')
        o = bank_cat(bank_name=bank_name, co_name=co_name, cat=cat)
        o.save()
        #pyautogui.alert("Upload Done")
    a = bank_cat.objects.all()
    return render(request, 'master_bank_cat.html', {'alldata': a})


#                                                -------------------------------------------
# Customer Type Start

def cust_type_edit_table(request):
    try:
        if request.method == 'POST':
            cust_type = request.POST.get('cust_type')
            pid = request.POST.get('id')

            abc = customer_type.objects.get(id=pid)
            abc.type = cust_type
            abc.save()

        a = customer_type.objects.all()
        return redirect('crm_app/master_cust_type')
    except:
        return render(request, 'failure.html')

def cust_type_edit(request, id):
    cust = customer_type.objects.get(id=id)
    cust_type = customer_type.objects.all()
    return render(request, 'cust_type_edit.html', {'prd': cust, 'cust_type': cust_type})

# Customer Type End
#                                                -------------------------------------------

#                                                -------------------------------------------
# Loan Type Start

def loan_type_edit_table(request):
    try:
        if request.method == 'POST':
            cust_type = request.POST.get('cust_type')
            pid = request.POST.get('id')

            abc = loan_type.objects.get(id=pid)
            abc.loan_type = cust_type
            abc.save()

        a = loan_type.objects.all()
        return redirect('crm_app/master_loan_type')
    except:
        return render(request, 'failure.html')

def loan_type_edit(request, id):
    cust = loan_type.objects.get(id=id)
    cust_type = loan_type.objects.all()
    return render(request, 'loan_type_edit.html', {'prd': cust, 'cust_type': cust_type})

# Loan Type End
#                                                -------------------------------------------

#                                                -------------------------------------------
# Bank Name Start

def bank_name_edit_table(request):
    try:
        if request.method == 'POST':
            cust_type = request.POST.get('cust_type')
            pid = request.POST.get('id')

            abc = bank_name.objects.get(id=pid)
            abc.b_name = cust_type
            abc.save()

        a = bank_name.objects.all()
        return redirect('crm_app/master_bank_name')
    except:
        return render(request, 'failure.html')

def bank_name_edit(request, id):
    cust = bank_name.objects.get(id=id)
    cust_type = bank_name.objects.all()
    return render(request, 'bank_name_edit.html', {'prd': cust, 'cust_type': cust_type})

# Bank Name End
#                                                -------------------------------------------

#                                                -------------------------------------------
# Co-Category Type Start

def cocat_type_edit_table(request):
    try:
        if request.method == 'POST':
            cocat_type = request.POST.get('cocat_type')
            min_amt = request.POST.get('min_amt')
            max_amt = request.POST.get('max_amt')
            pid = request.POST.get('id')
            abc = pp_cocat_type.objects.get(id=pid)
            abc.cocat_types = cocat_type
            abc.min_loan_amt = min_amt
            abc.max_loan_amt = max_amt
            abc.save()
        return redirect(master_cocat_type)
    except:
        return render(request, 'failure.html')

def cocat_type_edit(request, id):
    m = pp_cocat_type.objects.get(id=id)
    return render(request, 'cocat_type_edit.html', {'prd': m})

def cocat_type_delete(request, id):
	m = pp_cocat_type.objects.get(pk=id).delete()
	return redirect('/crm_app/master_cocat_type')
# Co-Category Type End
#

#                                                -------------------------------------------
# Bank-Category Type Start

def bank_cat_edit_table(request):
    try:
        if request.method == 'POST':
            comp_name = request.POST.get('comp_name')
            pid = request.POST.get('id')
            abc = pp_company_type.objects.get(id=pid)
            abc.comp_type = comp_name
            abc.save()

        a = pp_company_type.objects.all()
        return redirect(master_bank_cat)
    except:
        return render(request, 'failure.html')

def bank_cat_edit(request, id):
    m = pp_company_type.objects.get(id=id)
    cust_type = bank_cat.objects.all()
    bank = bank_name.objects.all()
    cate = cocat_type.objects.all()
    return render(request, 'bank_cat_edit.html', {'prd': m, 'cust_type': cust_type, 'bank': bank, 'cate': cate})

# Bank-Category Type End
#

#                                                -------------------------------------------
# Company Type Start

def company_type_edit_table(request):
    try:
        if request.method == 'POST':
            comp_type = request.POST.get('comp_type')
            pid = request.POST.get('id')
            abc = pp_company_type.objects.get(id=pid)
            abc.comp_type = comp_type
            abc.save()
        return redirect(master_company_type)
    except:
        return render(request, 'failure.html')

def company_type_edit(request, id):
    m = pp_company_type.objects.get(id=id)
    cust_type = company_type.objects.all()
    return render(request, 'company_type_edit.html', {'prd': m, 'cust_type': cust_type})

def company_type_delete(request, id):
	m = pp_company_type.objects.get(pk=id).delete()
	return redirect('/crm_app/master_company_type')
# Company Type End
#

#                                                -------------------------------------------
# Salary Type Start

def salary_type_edit_table(request):
    try:
        if request.method == 'POST':
            sal_type = request.POST.get('sal_type')
            pid = request.POST.get('id')

            abc = pp_salary_type.objects.get(id=pid)
            abc.sal_type = sal_type
            abc.save()

        a = pp_salary_type.objects.all()
        return redirect(master_salary_type)
    except:
        return render(request, 'failure.html')

def salary_type_edit(request, id):
    m = pp_salary_type.objects.get(id=id)
    cust_type = pp_salary_type.objects.all()
    return render(request, 'salary_type_edit.html', {'prd': m, 'cust_type': cust_type})

def salary_type_delete(request, id):
	m = pp_salary_type.objects.get(pk=id).delete()
	return redirect('/crm_app/master_salary_type')
# Salary Type End
#

#                                                -------------------------------------------
# Residence Type Start

def master_residence_type(request):
    a = pp_residence_type.objects.all()
    return render(request, 'master_residence_type.html', {'alldata': a})

def residence_type_edit_table(request):
    try:
        if request.method == 'POST':
            res_type = request.POST.get('res_type')
            pid = request.POST.get('id')
            abc = pp_residence_type.objects.get(id=pid)
            abc.res_type = res_type
            abc.save()

        a = pp_residence_type.objects.all()
        return redirect(master_residence_type)
    except:
        return render(request, 'failure.html')

def residence_type_edit(request, id):
    m = pp_residence_type.objects.get(id=id)
    cust_type = residence_type.objects.all()
    return render(request, 'residence_type_edit.html', {'prd': m, 'cust_type': cust_type})

def residence_type_delete(request, id):
	m = pp_residence_type.objects.get(pk=id).delete()
	return redirect('/crm_app/master_residence_type')
# Residence Type End
#

#                                                -------------------------------------------
# Designation Type Start

def designation_type_edit_table(request):
    try:
        if request.method == 'POST':
            cust_type = request.POST.get('cust_type')
            pid = request.POST.get('id')

            abc = designation.objects.get(id=pid)
            abc.design = cust_type
            abc.save()

        a = designation.objects.all()
        return redirect('crm_app/master_designation')
    except:
        return render(request, 'failure.html')

def designation_type_edit(request, id):
    cust = designation.objects.get(id=id)
    cust_type = designation.objects.all()
    return render(request, 'designation_type_edit.html', {'prd': cust, 'cust_type': cust_type})

# Designation Type End
#

#                                                -------------------------------------------
# Cibil Start

def master_cibil(request):
    a = pp_cibil.objects.all()
    return render(request, 'master_cibil.html', {'alldata': a})

def cibil_edit_table(request):
    try:
        if request.method == 'POST':
            cibil_type = request.POST.get('cibil_type')
            pid = request.POST.get('id')

            abc = pp_cibil.objects.get(id=pid)
            abc.cibil_type = cibil_type
            abc.save()
        return redirect(master_cibil)
    except:
        return render(request, 'failure.html')

def cibil_edit(request, id):
    m = pp_cibil.objects.get(id=id)
    return render(request, 'cibil_edit.html', {'prd': m})

# Cibil End
#

#                                                -------------------------------------------
# Tenure Start

def master_tenure(request):
    a = pp_tenure.objects.all()
    return render(request, 'master_tenure.html', {'alldata': a})

def tenure_edit_table(request):
    try:
        if request.method == 'POST':
            ten_type = request.POST.get('ten_type')
            pid = request.POST.get('id')

            abc = pp_tenure.objects.get(id=pid)
            abc.ten_type = ten_type
            abc.save()
        return redirect(master_tenure)
    except:
        return render(request, 'failure.html')

def tenure_edit(request, id):
    m = pp_tenure.objects.get(id=id)
    return render(request, 'tenure_edit.html', {'prd': m})


def tenure_delete(request, id):
	m = pp_tenure.objects.get(pk=id).delete()
	return redirect('/crm_app/master_tenure')
# Tenure End
#

#                                                -------------------------------------------
# Max Age Start

def master_max_age(request):
    a = pp_max_age.objects.all()
    return render(request, 'master_max.html', {'alldata': a})

def max_edit_table(request):
    try:
        if request.method == 'POST':
            max_type = request.POST.get('max_type')
            pid = request.POST.get('id')

            abc = pp_max_age.objects.get(id=pid)
            abc.max_type = max_type
            abc.save()
        return redirect(master_max_age)
    except:
        return render(request, 'failure.html')

def max_edit(request, id):
    m = pp_max_age.objects.get(id=id)
    return render(request, 'max_edit.html', {'prd': m})

def max_delete(request, id):
	m = pp_max_age.objects.get(pk=id).delete()
	return redirect('/crm_app/master_max')
# Max Age End
#

#                                                -------------------------------------------
# PP Start

def master_product_policy(request):
    a = prod_policy_master.objects.all()
    return render(request, 'master_product_policy.html',{'a':a})

def pp_edit_table(request):
    try:
        if request.method == 'POST':
            bank_names = request.POST.get('bank_names')
          

            pid = request.POST.get('id')

            abc = prod_policy_master.objects.get(id=pid)
            abc.bank_names = bank_names
         

            abc.save()
        return redirect(master_product_policy)
    except:
        return render(request, 'failure.html')

def pp_edit(request, id):
    m = prod_policy_master.objects.get(id=id)
    return render(request, 'pp_edit.html', {'prd': m})

# PP End
#

# Cibil Start

def add_cibil(request):
    a = prod_policy_master.objects.all()
    return render(request, 'add_cibil.html', {'a': a})

def add_cibil_table(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        sid = prod_policy_master.objects.get(id=pid)
        cibil = request.POST.get('cibil')
        o = pp_cibil(ppid4=sid, cibil_type=cibil, effec_date4=sid.eff_date, ineffec_date4=sid.ineff_date)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(master_cibil)

def master_cibil(request):
    a = pp_cibil.objects.all()
    return render(request, 'master_cibil.html', {'alldata': a})

def cibil_edit_table(request):
    try:
        if request.method == 'POST':
            cibil_type = request.POST.get('cibil_type')
            pid = request.POST.get('id')

            abc = pp_cibil.objects.get(id=pid)
            abc.cibil_type = cibil_type
            abc.save()
        return redirect('/crm_app/master_cibil')
    except:
        return render(request, 'failure.html')

def cibil_edit(request, id):
    m = pp_cibil.objects.get(pk=id)
    return render(request, 'cibil_edit.html', {'prd': m})

def cibil_delete(request, id):
	m = pp_cibil.objects.get(pk=id).delete()
	return redirect('/crm_app/master_cibil')
	
# Cibil End
#

#                                                -------------------------------------------
# Tenure Start

def add_tenure(request):
    a = prod_policy_master.objects.all()
    return render(request, 'add_tenure.html', {'a': a})

def add_tenure_table(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        sid = prod_policy_master.objects.get(id=pid)
        ten_type = request.POST.get('ten_type')
        o = pp_tenure(ppid5=sid, ten_type=ten_type,effec_date5=sid.eff_date,ineffec_date5=sid.ineff_date)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(master_tenure)

def master_tenure(request):
    a = pp_tenure.objects.all()
    return render(request, 'master_tenure.html', {'alldata': a})

def tenure_edit_table(request):
    try:
        if request.method == 'POST':
            ten_type = request.POST.get('ten_type')
            pid = request.POST.get('id')

            abc = pp_tenure.objects.get(id=pid)
            abc.ten_type = ten_type
            abc.save()
        return redirect(master_tenure)
    except:
        return render(request, 'failure.html')

def tenure_edit(request, id):
    m = pp_tenure.objects.get(id=id)
    return render(request, 'tenure_edit.html', {'prd': m})

# Tenure End
#

#                                                -------------------------------------------
# Max Age Start

def master_max_age(request):
    a = pp_max_age.objects.all()
    return render(request, 'master_max.html', {'alldata': a})

def max_edit_table(request):
    try:
        if request.method == 'POST':
            max_type = request.POST.get('max_type')
            pid = request.POST.get('id')

            abc = pp_max_age.objects.get(id=pid)
            abc.max_type = max_type
            abc.save()
        return redirect(master_max_age)
    except:
        return render(request, 'failure.html')

def max_edit(request, id):
    m = pp_max_age.objects.get(id=id)
    return render(request, 'max_edit.html', {'prd': m})

# Max Age End
#

#                                                -------------------------------------------
# PP Start

def master_product_policy(request):
    a = prod_policy_master.objects.all()
    return render(request, 'master_product_policy.html',{'a':a})

def pp_edit_table(request):
    try:
        if request.method == 'POST':
            bank_names = request.POST.get('bank_names')
            type_of_cust=request.POST.get('type_of_cust')
            salary_acc=request.POST.get('salary_acc')
            designs=request.POST.get('designs')
            min_age=request.POST.get('min_age')
            max_age=request.POST.get('max_age')
            current_exp=request.POST.get('current_exp')
            roi=request.POST.get('roi')
            #eff_date=request.POST.get('eff_date')
            #ineff_date=request.POST.get('ineff_date')
            pid = request.POST.get('id')
            abc = prod_policy_master.objects.get(id=pid)
            


            abc = prod_policy_master.objects.get(id=pid)
            abc.bank_names = bank_names
            abc.type_of_cust=type_of_cust
            abc.salary_acc=salary_acc
            abc.designs=designs
            abc.min_age=min_age
            abc.max_age=max_age
            abc.current_exp=current_exp
            abc.roi=roi
            #abc.eff_date=eff_date
            #abc.ineff_date=ineff_date

            abc.save()
        return redirect(master_product_policy)
    except:
        return render(request, 'failure.html')

def pp_edit(request, id):
    m = prod_policy_master.objects.get(id=id)
    return render(request, 'pp_edit.html', {'prd': m})

# PP End
#

#                                                -------------------------------------------
# PP Entire Master Start

def pp_master(request):
    a = prod_policy_master.objects.all()
    return render(request, 'pp_master.html',{'a':a})


def ppm_search(request, id):
    v = prod_policy_master.objects.get(id=id)
    c = pp_cibil.objects.all()
    cocat = pp_cocat_type.objects.all()
    comp = pp_company_type.objects.all()
    max = pp_max_age.objects.all()
    res = pp_residence_type.objects.all()
    sal = pp_salary_type.objects.all()
    ten = pp_tenure.objects.all()
    return render(request, 'ppm_search.html',{'v':v,'c':c,'cocat':cocat,'comp':comp,'max':max,'res':res,'sal':sal,'ten':ten})

def add_prp(request):
    return render(request, 'add_cibil.html')

# PP Entire Master End
#

#                                                -------------------------------------------
# Customer Details Start

def customer(request):
    a = uploads.objects.all()
    return render(request, 'crm_customer.html', {'alldata': a})

def cust_edit(request, id):
    v = uploads.objects.get(id=id)
    return render(request, 'cust_edit.html', {'prd': v})

def cust_edit_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        cibil_score = request.POST.get('cibil_score')
        bank_name = request.POST.get('bank_name')
        gross_sal = request.POST.get('gross_sal')
        net_sal = request.POST.get('net_sal')
        age = request.POST.get('age')
        retire_age = request.POST.get('retire_age')
        company_type = request.POST.get('company_type')
        designation = request.POST.get('designation')
        designation_type = request.POST.get('designation_type')
        current_exp = request.POST.get('current_exp')
        total_exp = request.POST.get('total_exp')
        emp_type = request.POST.get('emp_type')
        form_16 = request.POST.get('form_16')
        residence_type = request.POST.get('residence_type')
        stt = request.POST.get('stt')
        sttt = request.POST.get('sttt')
        tenure = request.POST.get('tenure')
        custo_type = request.POST.get('custo_type')
        loan_type = request.POST.get('loan_type')
        pid = request.POST.get('id')

        abc = uploads.objects.get(id=pid)
        abc.criteria = ''
        abc.remark = ''
        abc.paid_up_cap=''
        abc.company_yrs = ''
        abc.nature_company = ''
        abc.loan_type = loan_type
        abc.tenure = tenure
        abc.custo_type = custo_type
        abc.name = name
        abc.mobile = mobile
        abc.email = email
        abc.cibil_score = cibil_score
        abc.bank_name = bank_name
        abc.gross_sal = gross_sal
        abc.net_sal = net_sal
        abc.age = age
        abc.retire_age = retire_age
        abc.company_type = company_type
        abc.designation = designation
        abc.designation_type = designation_type
        abc.current_exp = current_exp
        abc.total_exp = total_exp
        abc.emp_type = emp_type
        abc.form_16 = form_16
        abc.residence_type = residence_type
        abc.stt = stt
        abc.sttt = sttt
        abc.save()
        #pyautogui.alert("Upload Done")
    return redirect(customer)

def check_eligible(request, id):
    v = uploads.objects.get(id=id)
    c = pp_cibil.objects.all()
    comp = pp_company_type.objects.all()
    bnkcat = bank_cat.objects.all()
    ten = pp_tenure.objects.all()
    pc = pp_cocat_type.objects.all()
    rs = pp_residence_type.objects.all()
    rea = reasons.objects.all()
    l=[]
    msg=''
    camt=0
    cat='Not calculated'
    elamt=0
    alamt=0
    cv=''
    prod=''
    final=0
    alamt1=0
    eligible=0
    cate=''
    mul=0
    foi=0
    for i in c:
        prod = prod_policy_master.objects.get(id=i.ppid4_id)
        if v.loan_type == prod.prod_name:
            if v.custo_type == prod.type_of_cust:
                if int(v.cibil_score) >= i.cibil_type:
                    if (int(v.age) >= prod.min_age) and (int(v.age) < prod.max_age):
                        for j in comp:
                            if i.ppid4 == j.ppid:
                                if v.company_type == j.comp_type:
                                    for k in bnkcat:
                                        if prod.bank_names == k.bank_name:
                                            if v.company_name == k.co_name :
                                                for a in pc :
                                                    if i.ppid4 == a.ppid6 :
                                                        if k.cat == a.cocat_types:
                                                            cat = k.cat
                                                            elamt = int(v.net_sal)*(a.cocat_no)
                                                            co = a.cocat_no
                                                            if elamt > a.max_loan_amt:
                                                                alamt = a.max_loan_amt
                                                                final = alamt
                                                                camt = a.max_loan_amt
                                                            else:
                                                                alamt = elamt
                                                                final = alamt
                                                                camt = a.max_loan_amt
                                                        for m in rs:
                                                            if m.ppid2 == i.ppid4:
                                                                if v.residence_type == m.res_type:
                                                                    if int(v.total_exp) >= prod.current_exp:
                                                                        for t in ten:
                                                                            if i.ppid4 == t.ppid5:
                                                                                if v.tenure == t.ten_type:
                                                                                    if int(v.net_sal) >=int(prod.salary_new):
                                                                                        # l1=[]
                                                                                        # l1.append(prod.pp_id)
                                                                                        # l1.append(alamt)
                                                                                        # l1.append(elamt)
                                                                                        # l.append()

                                                                                        if alamt > v.loan_amt:
                                                                                            mul = v.loan_amt
                                                                                        else:
                                                                                            mul = alamt
                                                                                        cate = cat
                                                                                        l.append(prod.pp_id)
                                                                                        msg='ELIGIBLE'
                                                                    else:
                                                                        if msg != 'ELIGIBLE':
                                                                            for mno in rea:
                                                                                if mno.rname=='total experience':
                                                                                    msg=mno.rrea
                                                                else:
                                                                    if msg != 'ELIGIBLE':
                                                                        for mno in rea:
                                                                            if mno.rname == 'Residence Type':
                                                                                msg = mno.rrea
                    else:
                        if msg != 'ELIGIBLE':
                            for mno in rea:
                                if mno.rname == 'age':
                                    msg = mno.rrea
                else:
                    if msg != 'ELIGIBLE':
                        for mno in rea:
                            if mno.rname == 'cibil score':
                                msg = mno.rrea

    if msg != 'ELIGIBLE':
        if msg == '':
            msg = 'Other criterias is not satisfying'

    sets = set(l)
    cv = list(sets)
    prod = prod_policy_master.objects.all()
    loan = loan_details.objects.all()
    credit=credit_details.objects.all()
    cut=0
    f = pp_foir.objects.all()
    for i in f:
        if (int(v.net_sal) > i.min_amt) and (int(v.net_sal) <= i.max_amt):
            cut = int(v.net_sal)*i.cutoff/100
    sum_limit=0
    ob=0
    for i in credit:
        if v.id == i.uid_id:
            sum_limit = sum_limit + int(i.limit_utilize)
    sum_limit = sum_limit * 5 / 100
    for i in loan:
        if v.id == i.uid_id:
            sum_limit = sum_limit + int(i.emi)
    tot = int(cut - sum_limit)
    ppmm = prod_policy_master.objects.all()
    emi=0
    elig=0
    for mn in loan:
        if mn.uid_id == v.id:
            for i in l:
                for k in ppmm:
                    if i == k.pp_id:
                        p = 100000
                        roi = int(k.roi) / (12 * 100)
                        t = v.tenure
                        emi = (p * roi * pow(1 + roi, t)) / (pow(1 + roi, t) - 1)
                        emi = round(emi, 2)
                        elig = int(round(tot/emi,5)*100000)
                        if elig > v.loan_amt:
                            foi = v.loan_amt
                        else:
                            foi = elig
                        eligible = elig*co
                        eligible = round(eligible,2)
            if eligible > camt:
                alamt1 = camt
            else:
                alamt1 = eligible
    for i in loan:
        if i.uid_id == v.id:
            if int(alamt) > elig:
                final = elig
                if final > v.loan_amt:
                    final = v.loan_amt
            else:
                final = int(alamt)
                if final > v.loan_amt:
                    final = v.loan_amt
    return render(request, 'check_el.html',{'foi':foi,'mul':mul,'cate':cate,'final':final,'alamt1':alamt1,'camt':camt,'eligible':eligible,'elig':elig,'emi':emi,'tot':tot,'ob':sum_limit,'cut':cut,'s':v,'loan':loan,'credit':credit,'cat':cat,'elamt':elamt,'alamt':alamt,'cv':cv,'prod':prod,'msg':msg})

# def sendSimpleEmail(request,id):
#    v = uploads.objects.get(id=id)
#    emailto = v.email
#    res = send_mail("Eligibility check by Creative Finserve", "Your documents have been verified", "siddhi3107.com", [emailto],fail_silently=False)
#
#    return redirect(customer)

# Customer Details End


#                                                -------------------------------------------
# Derived Residence Start
def derived_residence(request):
    a = residence_type.objects.all()
    return render(request, 'derived_residence.html', {'alldata': a})

def add_derived_residence(request):
    return render(request, 'add_derived_res.html')

def add_derived_residence_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = residence_type(r_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(derived_residence)

def res_delete(request, id):
	m = residence_type.objects.get(pk=id).delete()
	return redirect('/crm_app/derived_residence')

# Derived Residence End

#                                                -------------------------------------------
# Derived Salary Start
def derived_salary(request):
    a = salary_type.objects.all()
    return render(request, 'derived_salary.html', {'alldata': a})

def add_derived_salary(request):
    return render(request, 'add_derived_sal.html')

def add_derived_salary_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = salary_type(s_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(derived_salary)

def sal_delete(request, id):
	m = salary_type.objects.get(pk=id).delete()
	return redirect('/crm_app/derived_salary')

# Derived Salary End


#                                                -------------------------------------------
# Derived Company Start
def derived_company(request):
    a = company_type.objects.all()
    return render(request, 'derived_company.html', {'alldata': a})

def add_derived_company(request):
    return render(request, 'add_derived_com.html')

def add_derived_company_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = company_type(co_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(derived_company)

def com_delete(request, id):
	m = company_type.objects.get(pk=id).delete()
	return redirect('/crm_app/derived_company')

# Derived Company End


#                                                -------------------------------------------
# Derived Cocat Start
def derived_cocat(request):
    a = cocat_type.objects.all()
    return render(request, 'derived_cocat.html', {'alldata': a})

def add_derived_cocat(request):
    return render(request, 'add_derived_coc.html')

def add_derived_cocat_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = cocat_type(c_type=type)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(derived_cocat)

def coc_delete(request, id):
	m = cocat_type.objects.get(pk=id).delete()
	return redirect('/crm_app/derived_cocat')

# Derived Cocat End

#                                                -------------------------------------------
# Derived Tenure Start
def derived_ten(request):
    a = tenure.objects.all()
    return render(request, 'derived_ten.html', {'alldata': a})

def add_derived_ten(request):
    return render(request, 'add_derived_ten.html')

def add_derived_ten_table(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        o = tenure(tenure=type)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(derived_ten)

def ten_delete(request, id):
	m = tenure.objects.get(pk=id).delete()
	return redirect('/crm_app/derived_ten')

# Derived Tenure End


#                                       -------------------------------
# Reasons Start
def reasonsp(request):
    a = reasons.objects.all()
    return render(request, 'reasons.html', {'alldata': a})

def add_rea(request):
    a = reasons.objects.all()
    return render(request, 'add_rea.html', {'prd': a})

def add_rea_table(request):
    if request.method == 'POST':
        rname = request.POST.get('rname')
        rrea = request.POST.get('rrea')
        o = reasons(rname=rname,rrea=rrea)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(reasonsp)

def rea_edit(request, id):
    m = reasons.objects.get(id=id)
    return render(request, 'rea_edit.html', {'prd': m})

def rea_edit_table(request):
    try:
        if request.method == 'POST':
            rname = request.POST.get('rname')
            rrea = request.POST.get('rrea')
            pid = request.POST.get('id')
            abc = reasons.objects.get(id=pid)
            abc.rname = rname
            abc.rrea = rrea
            abc.save()
        return redirect(reasonsp)
    except:
        return render(request, 'failure.html')

def rea_delete(request, id):
	m = reasons.objects.get(pk=id).delete()
	return redirect('/crm_app/reasonsp')

# Reasons End

#                                                -------------------------------------------
# Foir Start
def master_foir(request):
    a = pp_foir.objects.all()
    return render(request, 'master_foir.html', {'alldata': a})

def add_foir(request):
    a = prod_policy_master.objects.all()
    return render(request, 'add_foir.html', {'a': a})

def add_foir_table(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        sid = prod_policy_master.objects.get(id=pid)
        min_amt = request.POST.get('min_amt')
        max_amt = request.POST.get('max_amt')
        cutoff = request.POST.get('cutoff')
        o = pp_foir(ppid7=sid,min_amt=min_amt,max_amt=max_amt,cutoff=cutoff)
        o.save()
        #pyautogui.alert("Upload Done")
    return redirect(master_foir)

def foir_edit_table(request):
    try:
        if request.method == 'POST':
            min_amt = request.POST.get('min_amt')
            max_amt = request.POST.get('max_amt')
            cutoff = request.POST.get('cutoff')
            pid = request.POST.get('id')

            abc = pp_foir.objects.get(id=pid)
            abc.min_amt = min_amt
            abc.max_amt = max_amt
            abc.cutoff = cutoff
            abc.save()
        return redirect('/crm_app/master_foir')
    except:
        return render(request, 'failure.html')

def foir_edit(request, id):
    m = pp_foir.objects.get(pk=id)
    return render(request, 'foir_edit.html', {'prd': m})

def foir_delete(request, id):
	m = pp_foir.objects.get(pk=id).delete()
	return redirect('/crm_app/master_foir')

# Foir End

def cust_delete(request, id):
	m = uploads.objects.get(pk=id).delete()
	return redirect('/crm_app/customer')


def add_customer_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile')
        e_mail = request.POST.get('email')
        loan_type = request.POST.get('loan_type')
        custo_type = request.POST.get('custo_type')
        if request.POST.get('ten') != "Select":
            ten = request.POST.get('ten')
        else:
            ten = "0"
        loan_amt = request.POST.get('loan_amt')
        if request.POST.get('cibil_score'):
            cibil_score = request.POST.get('cibil_score')
        else:
            cibil_score = "0"
        bank_name = request.POST.get('bank_name')
        if request.POST.get('gross_sal'):
            gross_sal = request.POST.get('gross_sal')
        else:
            gross_sal = "0"
        if request.POST.get('net_sal'):
            net_sal = request.POST.get('net_sal')
        else:
            net_sal = "0"
        if request.POST.get('age'):
            age = request.POST.get('age')
        else:
            age = "0"
        if request.POST.get('retire_age'):
            retire_age = request.POST.get('retire_age')
        else:
            retire_age = "0"
        company_type = request.POST.get('company_type')
        company_name = request.POST.get('company_name')
        designation = request.POST.get('designation')
        designation_type = request.POST.get('designation_type')
        if request.POST.get('current_exp'):
            current_exp = request.POST.get('current_exp')
        else:
            current_exp = "0"
        if request.POST.get('total_exp'):
            total_exp = request.POST.get('total_exp')
        else:
            total_exp = "0"
        emp_type = request.POST.get('emp_type')
        form_16 = request.POST.get('form_16')
        residence_type = request.POST.get('residence_type')
        stt = request.POST.get('stt')
        sttt = request.POST.get('sttt')

        try:
            obj = uploads.objects.latest('id')
            uid = obj.id + 1
        except uploads.DoesNotExist:
            uid = 1

        o = uploads(id=uid, loan_amt=loan_amt, name=name, mobile=mobile_no, email=e_mail, loan_type=loan_type,
                        custo_type=custo_type, tenure=ten, cibil_score=cibil_score, bank_name=bank_name,
                        gross_sal=gross_sal, net_sal=net_sal, age=age, retire_age=retire_age, company_type=company_type,
                        company_name=company_name, paid_up_cap='', company_yrs='',
                        nature_company='', designation=designation, designation_type=designation_type,
                        current_exp=current_exp, total_exp=total_exp, emp_type=emp_type, form_16=form_16,
                        residence_type=residence_type, stt=stt, sttt=sttt)
        o.save()
        v = uploads.objects.get(id=uid)
        c = pp_cibil.objects.all()
        comp = pp_company_type.objects.all()
        bnkcat = bank_cat.objects.all()
        ten = pp_tenure.objects.all()
        pc = pp_cocat_type.objects.all()
        rs = pp_residence_type.objects.all()
        rea = reasons.objects.all()
        l = []
        msg = ''
        camt = 0
        cat = 'Not calculated'
        elamt = 0
        alamt = 0
        cv = ''
        prod = ''
        final = 0
        alamt1 = 0
        eligible = 0
        cate = ''
        mul = 0
        foi = 0
        for i in c:
            prod = prod_policy_master.objects.get(id=i.ppid4_id)
            if v.loan_type == prod.prod_name:
                if v.custo_type == prod.type_of_cust:
                    if int(v.cibil_score) >= i.cibil_type:
                        if (int(v.age) >= prod.min_age) and (int(v.age) < prod.max_age):
                            for j in comp:
                                if i.ppid4 == j.ppid:
                                    if v.company_type == j.comp_type:
                                        for k in bnkcat:
                                            if prod.bank_names == k.bank_name:
                                                if v.company_name == k.co_name:
                                                    for a in pc:
                                                        if i.ppid4 == a.ppid6:
                                                            if k.cat == a.cocat_types:
                                                                cat = k.cat
                                                                elamt = int(v.net_sal) * (a.cocat_no)
                                                                co = a.cocat_no
                                                                if elamt > a.max_loan_amt:
                                                                    alamt = a.max_loan_amt
                                                                    final = alamt
                                                                    camt = a.max_loan_amt
                                                                else:
                                                                    alamt = elamt
                                                                    final = alamt
                                                                    camt = a.max_loan_amt
                                                            for m in rs:
                                                                if m.ppid2 == i.ppid4:
                                                                    if v.residence_type == m.res_type:
                                                                        if int(v.total_exp) >= prod.current_exp:
                                                                            for t in ten:
                                                                                if i.ppid4 == t.ppid5:
                                                                                    if v.tenure == t.ten_type:
                                                                                        if int(v.net_sal) >= int(
                                                                                                prod.salary_new):
                                                                                            # l1=[]
                                                                                            # l1.append(prod.pp_id)
                                                                                            # l1.append(alamt)
                                                                                            # l1.append(elamt)
                                                                                            # l.append()

                                                                                            if alamt > v.loan_amt:
                                                                                                mul = v.loan_amt
                                                                                            else:
                                                                                                mul = alamt
                                                                                            cate = cat
                                                                                            l.append(prod.pp_id)
                                                                                            msg = 'ELIGIBLE'
                                                                        else:
                                                                            if msg != 'ELIGIBLE':
                                                                                for mno in rea:
                                                                                    if mno.rname == 'total experience':
                                                                                        msg = mno.rrea
                                                                    else:
                                                                        if msg != 'ELIGIBLE':
                                                                            for mno in rea:
                                                                                if mno.rname == 'Residence Type':
                                                                                    msg = mno.rrea
                        else:
                            if msg != 'ELIGIBLE':
                                for mno in rea:
                                    if mno.rname == 'age':
                                        msg = mno.rrea
                    else:
                        if msg != 'ELIGIBLE':
                            for mno in rea:
                                if mno.rname == 'cibil score':
                                    msg = mno.rrea

        if msg != 'ELIGIBLE':
            if msg == '':
                msg = 'Other criterias is not satisfying'

        sets = set(l)
        cv = list(sets)
        prod = prod_policy_master.objects.all()
        loan = loan_details.objects.all()
        credit = credit_details.objects.all()
        cut = 0
        f = pp_foir.objects.all()
        for i in f:
            if (int(v.net_sal) > i.min_amt) and (int(v.net_sal) <= i.max_amt):
                cut = int(v.net_sal) * i.cutoff / 100
        sum_limit = 0
        ob = 0
        for i in credit:
            if v.id == i.uid_id:
                sum_limit = sum_limit + int(i.limit_utilize)
        sum_limit = sum_limit * 5 / 100
        for i in loan:
            if v.id == i.uid_id:
                sum_limit = sum_limit + int(i.emi)
        tot = int(cut - sum_limit)
        ppmm = prod_policy_master.objects.all()
        emi = 0
        elig = 0
        for mn in loan:
            if mn.uid_id == v.id:
                for i in l:
                    for k in ppmm:
                        if i == k.pp_id:
                            p = 100000
                            roi = int(k.roi) / (12 * 100)
                            t = v.tenure
                            emi = (p * roi * pow(1 + roi, t)) / (pow(1 + roi, t) - 1)
                            emi = round(emi, 2)
                            elig = int(round(tot / emi, 5) * 100000)
                            if elig > v.loan_amt:
                                foi = v.loan_amt
                            else:
                                foi = elig
                            eligible = elig * co
                            eligible = round(eligible, 2)
                if eligible > camt:
                    alamt1 = camt
                else:
                    alamt1 = eligible
        for i in loan:
            if i.uid_id == v.id:
                if int(alamt) > elig:
                    final = elig
                    if final > v.loan_amt:
                        final = v.loan_amt
                else:
                    final = int(alamt)
                    if final > v.loan_amt:
                        final = v.loan_amt
        return render(request, 'check_el.html',
                      {'foi': foi, 'mul': mul, 'cate': cate, 'final': final, 'alamt1': alamt1, 'camt': camt,
                       'eligible': eligible, 'elig': elig, 'emi': emi, 'tot': tot, 'ob': sum_limit, 'cut': cut, 's': v,
                       'loan': loan, 'credit': credit, 'cat': cat, 'elamt': elamt, 'alamt': alamt, 'cv': cv,
                       'prod': prod, 'msg': msg})


def add_customer(request):
    custo_type = customer_type.objects.all().distinct()
    l = loan_type.objects.all()
    t = tenure.objects.all()
    b = company_type.objects.all()
    c = designation.objects.all()
    d = residence_type.objects.all()
    e = bank_cat.objects.all()
    return render(request, 'add_customer.html', {'custo_type':custo_type,'t':t,'loan_type':l,'com_type': b, 'des': c, 'res':d, 'com_name':e})

#CALCULATION
t21 = 0
t3 = 0
t1 = 0
l1 = []
l4 = []
l5 = []
l6 = []
e = 0
no = 1
namount = 0
typ = 0
gst, Bcharges, Install_no, fc, amt, intr, emi, years, months, days, totalamt, totalint, p, c = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


def index_calc(request):
    global t1, t21, t3, l1, l4, l5, l6, e, gst, Bcharges, Install_no, fc, amt, intr, l1, l6, l4, l5, emi, years, months, days, totalamt, totalint, p, c, typ
    if request.method == 'POST':
        choice = request.POST.get('type')
        amount = float(request.POST['amount'])
        amt = float(request.POST['amount'])
        intrest = float(request.POST['intrest'])
        intr = float(request.POST['intrest'])
        option = int(request.POST['options'])
        if (option == 1):
            typ = 'Half year'
        if (option == 2):
            typ = 'Quater'
        if (option == 3):
            typ = 'Month'
        if (option == 4):
            typ = 'Forth nightly'
        if (option == 5):
            typ = 'week'
        if (option == 6):
            typ = 'Day'
        print(typ)
        l1.clear()
        l4.clear()
        l5.clear()
        l6.clear()
        try:
            years = int(request.POST['years'])
        except:
            years = 0
        try:
            months = int(request.POST['months'])
        except:
            months = 0
        try:
            days = int(request.POST['days'])
        except:
            days = 0
        try:
            Install_no = int(request.POST['Install_no'])
        except:
            Install_no = 0
        try:
            Bcharges = float(request.POST['Bank charges'])
        except:
            Bcharges = 0
        try:
            gst = float(request.POST['GST'])
        except:
            gst = 0

        dic = {1: 2, 2: 4, 3: 12, 4: 24, 5: 52, 6: 365}
        if (years != 0):
            t1 = years * dic[option]
        if (months != 0):
            if (option == 3):
                t21 = months * 1
            elif (option == 4):  # 1-HALF Y
                t21 = months * 2  # 2-FOURTH             quater
            elif (option == 2):  # 3-QUATER                      month
                t21 = months / 3  # 4-MONTHLY             forth
            elif (option == 5):  # 5-WEEKLY
                t21 = months * 4  # 6-DAILY
            elif (option == 6):
                t21 = months * 30
            elif (option == 1):
                if (months > 5):
                    t21 = months / 6
                else:
                    message = 'you cannot select since months are less than 5'
                    return render(request, 'invinp.html', {'message': message})

        if (days != 0):
            if (years != 0 or months != 0):
                if (days > 29):
                    message = ' YOU CANNOT more than 29 day'
                    return render(request, 'invinp.html', {'message': message})

                elif (option == 6):
                    t3 = days

                elif (option == 5):
                    t3 = days / 7
                elif (option == 4):
                    if (days > 14):
                        t3 = days / 14
                    else:
                        message = 'you cannot enter days less than 15'
                        return render(request, 'invinp.html', {'message': message})

            elif (months != 0 or years != 0):
                if (option == 6):
                    t3 = days

                elif (option == 5):
                    t3 = days / 7
                elif (option == 4):
                    t3 = days / 14
            else:
                if (option == 6):
                    t3 = days


                elif (option == 5):
                    t3 = days / 7

                elif (option == 4):
                    if (days > 14):
                        t3 = days / 14

                    else:
                        message = 'you cannot enter days less than 15'
                        return render(request, 'invinp.html', {'message': message})

                elif (option == 1 or 2 or 3):
                    message = 'you can select only weeks or days'
                    return render(request, 'invinp.html', {'message': message})
        try:

            t = t1 + t21 + t3
            r = intrest / (100 * dic[option])
            if (int(choice) == 1):
                e = (amount / t) + (amount * r)
            else:
                e = (amount * r * pow((1 + r), t)) / (pow((1 + r), t) - 1)

            totalint = round((e * t) - amount)
            totalamt = round((e * t))

            for i in range(int(t)):
                intrest = r * amount
                pri_pay = e - intrest
                remain = amount - pri_pay
                l1.append(i + 1)
                l4.append(round(intrest))
                l5.append(round(pri_pay))
                l6.append(round(remain))
                amount = remain
            try:
                i = l4[Install_no - 1]
                p = l6[Install_no - 1]
                bi = p * (Bcharges / 100)
                g = (gst / 100) * bi
                c = bi + g
                fc = p + bi + g
            except:
                fc = 0
                c = 0

            t21 = 0
            t3 = 0
            t1 = 0
            amount = 0
            intrest = 0

        except:
            t21 = 0
            t3 = 0
            t1 = 0
            amount = 0
            intrest = 0
            typ = 0
            return render(request, 'error.html')

        if (int(choice) == 1):
            return render(request, "flat.html",
                          {'typ': typ, 'amt': amt, 'intr': intr, 'amount': amount, 'intrest': intrest, 'emi': round(e),
                           'years': years, 'months': months, 'days': days, 'totalint': totalint, 'totalamt': totalamt})
        else:
            return render(request, "reducing.html",
                          {'typ': typ, 'p': p, 'c': round(c), 'gst': gst, 'Bcharges': Bcharges,
                           'Install_no': Install_no, 'fc': round(fc), 'amt': amt, 'intr': intr, 'amount': amount,
                           'intrest': intrest, 'l1': l1, 'l6': l6, 'l5': l5, 'l4': l4, 'emi': round(e), 'years': years,
                           'months': months, 'days': days, 'totalint': totalint, 'totalamt': totalamt})

    return render(request, "index.html")


def advance(request):
    global typ, t1, t21, t3, l1, l4, l5, l6, e, gst, Bcharges, Install_no, fc, amt, intr, l1, l6, l4, l5, emi, years, months, days, totalamt, totalint, no, namount, p, c
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        amt = float(request.POST['amount'])
        intrest = float(request.POST['intrest'])
        intr = float(request.POST['intrest'])
        option = int(request.POST['options'])
        if (option == 1):
            typ = 'Half year'
        if (option == 2):
            typ = 'Quater'
        if (option == 3):
            typ = 'Month'
        if (option == 4):
            typ = 'Forth nightly'
        if (option == 5):
            typ = 'week'
        if (option == 6):
            typ = 'Day'
        print(typ)
        l1.clear()
        l4.clear()
        l5.clear()
        l6.clear()
        try:
            years = int(request.POST['years'])
        except:
            years = 0
        try:
            months = int(request.POST['months'])
        except:
            months = 0
        try:
            days = int(request.POST['days'])
        except:
            days = 0
        try:
            Install_no = int(request.POST['Install_no'])
        except:
            Install_no = 0
        try:
            Bcharges = float(request.POST['Bank charges'])
        except:
            Bcharges = 0
        try:
            no = int(request.POST['no'])
        except:
            no = 1
        try:
            gst = float(request.POST['GST'])
        except:
            gst = 0

        dic = {1: 2, 2: 4, 3: 12, 4: 24, 5: 52, 6: 365}
        if (years != 0):
            t1 = years * dic[option]
        if (months != 0):
            if (option == 3):
                t21 = months * 1
            elif (option == 4):  # 1-HALF Y
                t21 = months * 2  # 2-FOURTH             quater
            elif (option == 2):  # 3-QUATER                      month
                t21 = months / 3  # 4-MONTHLY             forth
            elif (option == 5):  # 5-WEEKLY
                t21 = months * 4  # 6-DAILY
            elif (option == 6):
                t21 = months * 30
            elif (option == 1):
                if (months > 5):
                    t21 = months / 6
                else:
                    message = 'you cannot select since months are less than 5'
                    return render(request, 'invinp.html', {'message': message})

        if (days != 0):
            if (years != 0 or months != 0):
                if (days > 29):
                    message = ' YOU CANNOT more than 29 day'
                    return render(request, 'invinp.html', {'message': message})

                elif (option == 6):
                    t3 = days

                elif (option == 5):
                    t3 = days / 7
                elif (option == 4):
                    if (days > 14):
                        t3 = days / 14
                    else:
                        message = 'you cannot enter days less than 15'
                        return render(request, 'invinp.html', {'message': message})

            elif (months != 0 or years != 0):
                if (option == 6):
                    t3 = days

                elif (option == 5):
                    t3 = days / 7
                elif (option == 4):
                    t3 = days / 14
            else:
                if (option == 6):
                    t3 = days


                elif (option == 5):
                    t3 = days / 7

                elif (option == 4):
                    if (days > 14):
                        t3 = days / 14

                    else:
                        message = 'you cannot enter days less than 15'
                        return render(request, 'invinp.html', {'message': message})

                elif (option == 1 or 2 or 3):
                    message = 'you can select only weeks or days'
                    return render(request, 'invinp.html', {'message': message})
        try:

            t = t1 + t21 + t3
            r = intrest / (100 * dic[option])
            try:
                for i in range(int(no)):
                    intrest = r * amount
                    pri_pay = e - intrest
                    remain = amount - pri_pay
                    l1.append(i + 1)
                    l4.append(round(intrest))
                    l5.append(round(pri_pay))
                    l6.append(round(remain))
                    amount = remain
                ti = sum(l4)
                namount = amt - ti
                l1.clear()
                l4.clear()
                l5.clear()
                l6.clear()
            except:
                namount = amt - (r * amt)
            print(namount)
            e = (namount * r * pow((1 + r), t)) / (pow((1 + r), t) - 1)
            # totalint=round((e*t)-amount)
            totalamt = round((e * t))
            print(e, totalint, totalamt)
            for i in range(int(t)):
                intrest = r * namount
                pri_pay = e - intrest
                remain = namount - pri_pay
                l1.append(i + 1)
                l4.append(round(intrest))
                l5.append(round(pri_pay))
                l6.append(round(remain))
                namount = remain
            for j in range(no):
                l4[j] = 0
                l5[j] = round(e)
            try:
                i = l4[Install_no - 1]
                p = l6[Install_no - 1]
                bi = p * (Bcharges / 100)
                g = (gst / 100) * bi
                c = bi + g
                fc = p + bi + g
            except:
                fc = 0
                c = 0
            t21 = 0
            t3 = 0
            t1 = 0
            amount = 0
            intrest = 0

        except:
            t21 = 0
            t3 = 0
            t1 = 0
            amount = 0
            intrest = 0
            typ = 0
            return render(request, 'error.html')

        return render(request, "advance.html",
                      {'typ': typ, 'p': p, 'c': round(c), 'namount': namount, 'no': no, 'gst': gst,
                       'Bcharges': Bcharges, 'Install_no': Install_no, 'fc': round(fc), 'amt': amt, 'intr': intr,
                       'amount': namount, 'intrest': intrest, 'l1': l1, 'l6': l6, 'l5': l5, 'l4': l4, 'emi': round(e),
                       'years': years, 'months': months, 'days': days, 'totalint': sum(l4), 'totalamt': totalamt})

    return render(request, "advance.html")


def details(request):
    global gst, Bcharges, Install_no, fc, amt, intr, l1, l6, l4, l5, emi, years, months, days, totalamt, totalint, p, c
    return render(request, "details.html",
                  {'typ': typ, 'p': p, 'c': round(c), 'gst': gst, 'Bcharges': Bcharges, 'Install_no': Install_no,
                   'fc': round(fc), 'amt': amt, 'intr': intr, 'l1': l1, 'l6': l6, 'l5': l5, 'l4': l4, 'emi': round(e),
                   'years': years, 'months': months, 'days': days, 'totalint': totalint, 'totalamt': totalamt})


def adetails(request):
    global no, gst, Bcharges, Install_no, fc, amt, intr, l1, l6, l4, l5, emi, years, months, days, totalamt, totalint, p, c
    return render(request, "adetails.html",
                  {'typ': typ, 'p': p, 'c': round(c), 'no': no, 'gst': gst, 'Bcharges': Bcharges,
                   'Install_no': Install_no, 'fc': round(fc), 'amt': amt, 'intr': intr, 'l1': l1, 'l6': l6, 'l5': l5,
                   'l4': l4, 'emi': round(e), 'years': years, 'months': months, 'days': days, 'totalint': totalint,
                   'totalamt': totalamt})


def fdetails(request):
    global amt, emi, years, months, days, totalamt, totalint, typ

    return render(request, "fdetails.html",
                  {'typ': typ, 'amt': amt, 'intr': intr, 'emi': round(e), 'years': years, 'months': months,
                   'days': days, 'totalint': totalint, 'totalamt': totalamt})