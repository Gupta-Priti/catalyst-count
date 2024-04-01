from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
import csv
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CompaniesDataSerializer


# Home page
def home(request):
    return render(request, 'home.html') 


# UPLOAD Data Section
def decode_utf8(line_iterator):
    for line in line_iterator:
        yield line.decode('utf-8')

@login_required
def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.save(commit=False) 
            uploaded_file.save()
            # print(uploaded_file,"Fileeee")
            companies_file = csv.reader(decode_utf8(uploaded_file.file))
            next(companies_file)
            count = 0
            for line in companies_file:
                company_number, name, domain, year_founded, industry, size_range, \
                    locality, country, linkedin_url, current_employee_estimate, \
                    total_employee_estimate = line
                
                CompaniesData.objects.create(
                    company_number=company_number,
                    name=name,
                    domain=domain,
                    year_founded=year_founded,
                    industry=industry,
                    size_range=size_range,
                    locality=locality,
                    country=country,
                    linkedin_url=linkedin_url,
                    current_employee_estimate=current_employee_estimate,
                    total_employee_estimate=total_employee_estimate
                )
                count +=1
                if count == 10 :
                    break
            return render(request, 'upload_data.html')
        else:
            print(form.errors)

    else:
        form = UploadFileForm()

    return render(request, 'upload_data.html', {'form': form})
    

# QUERY Builder Section
@login_required
def query_builder_data_show(request):
    distinct_industries = CompaniesData.objects.values('industry').distinct()
    distinct_years_founded = CompaniesData.objects.values('year_founded').distinct()

    distinct_localities = CompaniesData.objects.values('locality').distinct()
    distinct_cities = []
    distinct_states = []
    for locality in distinct_localities:
        locality_parts = locality['locality'].split(', ')
        if len(locality_parts) >= 2:
            distinct_cities.append(locality_parts[0])
            distinct_states.append(locality_parts[1])

    distinct_countries = CompaniesData.objects.values('country').distinct()
    distinct_employees_from = CompaniesData.objects.values('current_employee_estimate').distinct()
    distinct_employees_to = CompaniesData.objects.values('total_employee_estimate').distinct()

    return render(request, 'query_builder.html', {
        'distinct_industries': distinct_industries,
        'distinct_years_founded': distinct_years_founded,
        'distinct_cities': distinct_cities,
        'distinct_states': distinct_states,
        'distinct_countries': distinct_countries,
        'distinct_employees_from': distinct_employees_from,
        'distinct_employees_to': distinct_employees_to,
    })


@login_required
@api_view(['POST'])
def filtered_data_count_api(request):
    keyword = request.data.get('keyword')
    industry = request.data.get('industry')
    year_founded = request.data.get('year_founded')
    city = request.data.get('city')
    state = request.data.get('state')
    country = request.data.get('country')
    employees_from = request.data.get('employeesFrom')
    employees_to = request.data.get('employeesTo')
    
    filtered_data = CompaniesData.objects.all()
    
    if keyword:
        filtered_data = filtered_data.filter(name__icontains=keyword)
    
    if industry:
        filtered_data = filtered_data.filter(industry=industry)
    
    if year_founded:
        filtered_data = filtered_data.filter(year_founded=year_founded)
    
    if city:
        filtered_data = filtered_data.filter(locality__icontains=city)
    
    if state:
        filtered_data = filtered_data.filter(locality__icontains=state)
    
    if country:
        filtered_data = filtered_data.filter(country=country)
    
    if employees_from:
        filtered_data = filtered_data.filter(current_employee_estimate__gte=employees_from)
    
    if employees_to:
        filtered_data = filtered_data.filter(total_employee_estimate__lte=employees_to)
    
    filtered_count = filtered_data.count()
    # print(filtered_count,"CCCCCCCCCCCC")
    
    serializer = CompaniesDataSerializer(filtered_data, many=True)

    return Response({'filtered_count': filtered_count, 'filtered_data': serializer.data}, status=status.HTTP_200_OK)


# USERS Section
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users, 'messages': messages.get_messages(request)})


@login_required
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'New user added!')
            return redirect('user_list') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'add_user.html', {'form': form})


@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  
    else:
        return redirect('user_list')
