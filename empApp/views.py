from django.shortcuts import render , HttpResponse
from . models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')



def add_emp(request):
    if request.method=='POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus= int(request.POST['bonus'])
        phone= int(request.POST['phone'])
        dept=request.POST['dept']
        role=request.POST['role']
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date= datetime.now() )
        new_emp.save()
        return HttpResponse('employee added successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("an Exception Occurred! Employee")




def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
        }
    return render(request, 'all_emp.html' , context)



def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_remove = Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("Employee Removed Successfully ")
        except:
            return HttpResponse("Please Provide Valid emp id ")
    
    emps = Employee.objects.all()
    context = {
        'emps': emps
        }
    return render(request, 'remove_emp.html', context)





def filter_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')
        emps = Employee.objects.all()
        if first_name or last_name:
            emps = emps.filter(Q(first_name__icontains = first_name) | Q(last_name__icontains = first_name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
            
        context = {
            'emps' : emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')