from django.shortcuts import render, redirect
import random
import razorpay
from datetime import datetime
from traveller_project.settings import RAZORPAY_API_KEY, RAZORPAT_API_SECERTKEY
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .models import user1
from .models import trip_data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'index.html')

def log_In(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username not exists")
            return redirect('/log')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Password invalid")
            return redirect('/log')
        
        else:
            login(request, user)
            return redirect('/pro')
    return render(request, 'login.html')

def regist(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        state = request.POST.get('state')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, 'User already taken')
            return redirect('/regist')

        user = User.objects.create(
            username = username,
            email = email
            )

        user.set_password(password)
        user.save()

        cuser = user1.objects.create(
            user=user,
            full_name = full_name,
            state = state,
            phone_number = phone_number
                       
        )

        print(cuser)
        
        cuser.save()
        messages.info(request, 'Account created successfull')
    return render(request, 'reg.html')
    

def trip(request):
    '''user_id = request.POST.get('user_id')
    
    if user_id is not None:
        try:
            user = get_object_or_404(User, id=int(user_id))
            return HttpResponse(f"User ID is {user_id}")
        except (ValueError, TypeError):
            return HttpResponse("Invalid User ID. Please provide a valid integer.")
    else:
        True'''
    
    if request.method == "POST":
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get("Last_name")
        Date_of_birth = request.POST.get("Date_of_birth")
        Phone_number = request.POST.get("Phone_number")
        Email = request.POST.get("Email")
        Address = request.POST.get("Address")
        State = request.POST.get("State")
        Zip_code = request.POST.get("Zipcode")
        Document = request.POST.get("Document")
        Document_number = request.POST.get("Document_number")
        Holiday_place = request.POST.get("Holiday_place")
        Child = request.POST.get("Child")
        Adult = request.POST.get("Adult")
        Old = request.POST.get("Old")
        Guest = request.POST.get("Guest")
        Guest_Doc_number = request.POST.get("Guest_document")
        Check_in = request.POST.get("Check_in")
        Check_out = request.POST.get("Check_out")
        Meal = request.POST.get("Meal")
        Star = request.POST.get("Star")
        Mount = request.POST.get("mount")
        Mount_number = request.POST.get("mount_number")
        Bungy = request.POST.get("bungy")
        Bungy_number = request.POST.get("bungy_number")
        River = request.POST.get("river")
        River_number = request.POST.get("river_number")
        Cab = request.POST.get("Cab")
        Picklocation = request.POST.get("Picklocation")
        Droplocation = request.POST.get("Droplocation")

        tr = trip_data.objects.create(
            #user = user,
            First_name = First_name,
            Last_name = Last_name,
            Date_of_birth = Date_of_birth,
            Phone_number = Phone_number,
            Email = Email,
            Address = Address,
            State = State,
            Zip_code = Zip_code,
            Document = Document,
            Document_number = Document_number,
            Holiday_place = Holiday_place,
            Child = Child,
            Adult = Adult,
            Old = Old,
            Guest = Guest,
            Guest_Doc_number = Guest_Doc_number,
            Check_in = Check_in,
            Check_out = Check_out,
            Meal = Meal,
            Star = Star,
            Mount = Mount,
            Mount_number = Mount_number,
            Bungy = Bungy,
            Bungy_number = Bungy_number, 
            River = River,
            River_number = River_number,
            Cab = Cab,
            Picklocation = Picklocation,
            Droplocation = Droplocation
        )
        tr.save()
    
        return redirect('/trip_detail')
    return render(request, 'trip.html')

def trip_detail(request):
    tr = trip_data.objects.latest('Check_in') 
    
    return render(request, 'tripdetail.html', context = {'trp': tr})

def delete_data(request, id):
    tr = trip_data.objects.get(id=id)
    tr.delete()
    return redirect('/')

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAT_API_SECERTKEY))
def paym(request, id):
    tr = trip_data.objects.get(id = id)
    total_guest = tr.Child+tr.Adult+tr.Old
    total_day = (tr.Check_out-tr.Check_in).days
    hotel_list=['The Leela Palace', 'Niraamaya Retreats', 'The iconic Taj Mahal Tower', 'The Taj Mahal Palace', 'Rambagh Palace', 'Shangri-La Eros', 'The Oberoi Cecil']
    hotel_rand = random.choice(hotel_list)
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%B %d, %Y at %I:%M:%S %p")
    one_day = 1150*total_day
    mealday = 750*total_guest
    mount_rate = 999*tr.Mount_number
    bungy_rate = 1199*tr.Bungy_number
    river_rate = 1499*tr.River_number
    sub_total = one_day+mealday+mount_rate+bungy_rate+river_rate
    dic_count =(10/100)*sub_total
    sub_total1 = sub_total-dic_count
    gst = (18/100)*sub_total1
    total = gst+sub_total1

    order_amount = 50000
    order_currency = 'INR'

    payment_order = client.order.create(dict(amount = order_amount, currency = order_currency, payment_capture =1))
    payment_order_id = payment_order['id']
    context = {
        'amount' : total, 'api_key':RAZORPAY_API_KEY, 'order_id':payment_order_id, 'trp': tr, 'tg' : total_guest, 'td' : total_day, 'hr' : hotel_rand, 'ftd' : formatted_date_time,
        'od': one_day, 'odm': mealday, 'mt': mount_rate, 'bj': bungy_rate, 'rr': river_rate, 'sub': sub_total
    }
    return render(request, 'pay.html', context)
    

@login_required(login_url='/log')
def profile(request):
    queryset = user1.objects.filter(user=request.user).first()
    context = {
        'use' : queryset
    }
    return render(request, 'profile.html', context)

@login_required(login_url="/log")
def lgout(request):
    logout(request)
    return redirect('/')

def offer_1(request):
    return render(request, 'offer1.html')

def offer_2(request):
    return render(request, 'offer2.html')

def offer_3(request):
    return render(request, 'offer3.html')

def offer_4(request):
    return render(request, 'offer4.html')