from django.db import models

# 1. DOCTORS (Medical Staff)
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"

# 2. PATIENTS (Already created, but keep it here)
class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# 3. MEDICAL RECORDS
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    diagnosis = models.TextField()
    prescription = models.TextField()
    lab_results = models.TextField(blank=True, null=True)
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.patient} - {self.date_recorded.date()}"

# 4. APPOINTMENTS
class Appointment(models.Model):
    STATUS_CHOICES = [('P', 'Pending'), ('C', 'Completed'), ('X', 'Cancelled')]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

# 5. WARD/INVENTORY
class Ward(models.Model):
    name = models.CharField(max_length=50) # e.g., Maternity, ICU
    capacity = models.IntegerField()
    occupied_beds = models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    expiry_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.stock_quantity} left)"
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    expiry_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.stock_quantity} units)"
