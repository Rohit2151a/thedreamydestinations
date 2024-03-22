from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import *

UserModel = get_user_model()
from .forms import SignUpForm
# from .tokens import account_activation_token


# Create your views here.
def home(request):
    return render(request, 'index.html')


def signup(request):
    try:
                if request.method == 'POST':
                    first_name = request.POST['first_name']
                    last_name = request.POST['last_name']
                    username = request.POST['username']
                    phone_no = request.POST['phone']
                    password1 = request.POST['password1']
                    password2 = request.POST['password2']
                    email = request.POST['email']

                    if password1==password2:
                        if User.objects.filter(username=username).exists():
                            messages.info(request, 'Username taken')
                            return redirect('/signup')
                        elif Employee.objects.filter(phone_no=phone_no, is_active=True).exists():
                            messages.info(request, 'Phone No Exists')
                            return redirect('/signup')
                        elif User.objects.filter(email=email, is_active=True).exists():
                            messages.info(request, 'Email taken')
                            return redirect('/signup')
                        else:
                            user = User.objects.create_user(username=username, password=password1,email=email, first_name= first_name, last_name=last_name)
                            user.is_active = False
                            user.save()
                            Emp = Employee()
                            Emp.user = user
                            Emp.is_active = False
                            Emp.phone_no = phone_no
                            Emp.save()
                            current_site = get_current_site(request)
                            mail_subject = 'Activate your account.'
                            message = render_to_string('acc_active_email.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': default_token_generator.make_token(user),
                             })
                            to_email = user.email
                            email = EmailMessage(
                            mail_subject, message, from_email= 'THE DREAMY DESTINATIONS <noreply@gmail.com>', to=[to_email]
                             )
                            email.send()
                            user.save()
                            messages.info(request, 'Activation link is send to your Email Address please complete the registration.')
                            return redirect('/signup')
                            """
                                messages.info(request, 'user created')
                                return render(request, 'login.html')
                            """
                    else:
                        messages.info(request, 'password not matching..')
                        return redirect('/signup')

                else:
                    return render(request, 'signup.html')
    except Exception as e:
        print('Error:-',e)
        messages.info(request, 'Error')
        return redirect('/signup')
"""
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, from_email= 'THE DREAMY DESTINATIONS < noreply@gmail.com >', to=[to_email]
            )
            email.send()
            messages.info(request, 'Activation link is send to your Email Address please complete the registration.')
            return redirect('/signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
"""
def login(request):
    try:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(username=username, password=password)

                if user is not None:
                    auth.login(request, user)
                    return redirect("/destination")
                else:
                    messages.info(request, 'Invalid credentials..')
                    return redirect('/login')

            else:
              return render(request, 'login.html')
    except Exception as e:
        print('Error:-',e)
        messages.info(request, 'Error')
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.employee.is_active = True
        user.save()
        user.employee.save()
        messages.info(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('/login')
    else:
        return HttpResponse('Activation link is invalid!')


def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html', {'images': images})

def destination(request):
    if request.method == 'GET':
                dests = Destinations.objects.all()
                return render(request, 'destinations.html', {'dests': dests})

    if request.method == 'POST':
           value = request.POST.get ('submit')
           request.session['value'] = value
           request.method = 'GET'
           return redirect('booking')

'''below code is for Stars in Destination'''
from django.template.defaulttags import register
@register.filter
def get_range(value):
    return range(value)

'''code End'''

def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        sub = request.POST['subject']
        message = request.POST['message']
        user = ContactUs(name=name, email=email, phone = phone, subject=sub, message=message)
        user.save()
        mail_subject = 'New Contact Us Query.'
        message = render_to_string('contact_us_mail.html', {'name': name, 'email': email, 'phone': phone, 'sub': sub, 'message': message})
        to_email = 'Roneyyadav121@gmail.com'
        email = EmailMessage(
            mail_subject, message, from_email='THE DREAMY DESTINATIONS < noreply@gmail.com >', to=[to_email]
        )
        email.send()
        messages.info(request, 'Thanks for Contacting US We Will Reach You Soon.')
        abouts = AboutUs.objects.all()
        return render(request, 'aboutus.html',{'abouts': abouts})

    else:
        abouts = AboutUs.objects.all()
        return render(request, 'aboutus.html', {'abouts': abouts})


@login_required
def booking(request):
    try:
                if request.method =='GET':
                    if (request.session.get('value', None) != None):
                         value = request.session['value']
                         dest = Destinations.objects.get(pk=value)
                         return render(request, 'booking.html', { 'dest': dest})
                    else:
                        return render(request, 'booking.html')

                if request.method =='POST':
                    guest = User.objects.get(username=request.user)
                    value = request.session['value']
                    dest = Destinations.objects.get(pk=value)
                    reservation = Reservation()
                    reservation.username = guest.username
                    reservation.name = guest.first_name
                    reservation.last_name = guest.last_name
                    reservation.email = guest.email
                    reservation.phone1 = guest.employee.phone_no
                    reservation.destination = dest.name
                    reservation.phone2 = request.POST['phone']
                    reservation.From_place = request.POST['From']
                    reservation.Members = request.POST['Members']
                    reservation.date = request.POST['date']
                    reservation.Days = request.POST['Days']
                    reservation.Nights = request.POST['Nights']
                    reservation.DestID = value
                    reservation.save()
                    # info = Reservation.objects.get(date=request.POST['date'],username=guest.username,destination=request.POST['Destination'])
                    info = reservation
                    mail_subject = 'Booking Details.'
                    message = render_to_string('booking_mail.html', {'info': info})
                    to_email = guest.email
                    email1 = EmailMessage(
                        mail_subject, message, from_email='THE DREAMY DESTINATIONS < noreply@gmail.com >', to=[to_email]
                    )
                    email1.send()

                    mail_subject = 'Booking Details.'
                    message = render_to_string('booking_mail_CEO.html', {'info': info, 'dest': dest})
                    to_email = 'Roneyyadav121@gmail.com'
                    email2 = EmailMessage(
                        mail_subject, message, from_email='THE DREAMY DESTINATIONS < noreply@gmail.com >', to=[to_email]
                    )
                    email2.send()
                    messages.info(request, 'Booking Successful !')
                    return redirect('/destination')

    except Exception as e:
        print('Error:-',e)
        messages.info(request, 'Something went Wrong!')
        return redirect('/booking')


