from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# 1. The missing Login class that caused the error
class PatientLoginView(LoginView):
    template_name = 'core/patient_login.html'

# 2. The Registration logic we've been working on
def register_patient(request):
    if request.method == "POST":
        # Capture all the data from your form fields
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        dob = request.POST.get('dob')         # Matches name="dob" in your HTML
        gender = request.POST.get('gender')   # Matches name="gender"
        phone = request.POST.get('phone')
        address = request.POST.get('address') # Matches name="address"
         # Save everything to the database
        Patient.objects.create(
            first_name=f_name,
            last_name=l_name,
            date_of_birth=dob,   # This fixes the IntegrityError
            gender=gender,
            phone_number=phone,
            address=address
        )
        return redirect('patient_profile')
    return render(request, 'core/register.html')

# 3. All the other "missing" functions your URLs need
def entrance(request):
    return render(request, 'core/entrance.html')

@login_required
def patient_profile(request):
    return render(request, 'core/patient_profile.html')

@login_required
def dashboard(request):
    context = {
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'appointment_count': Appointment.objects.count(),
    }
    return render(request, 'core/dashboard.html', context)

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'core/patient_list.html', {'patients': patients})

@login_required
def county_selection(request):
    return render(request, 'core/county_selection.html')

@login_required
def hospital_list(request):
    selected_county = request.GET.get('county', 'Unknown')
    return render(request, 'core/hospital_list.html', {'county': selected_county})

@login_required
def book_appointment(request):
    if request.method == "POST":
        time_slot = request.POST.get('slot')
        doc = Doctor.objects.first()
        Appointment.objects.create(
            patient=request.user,
            doctor=doc,
            appointment_date=timezone.now(),
            status='Scheduled'
        )
        return render(request, 'core/book_appointment.html', {'success_msg': f"Success! Slot {time_slot} booked."})
    return render(request, 'core/book_appointment.html')
