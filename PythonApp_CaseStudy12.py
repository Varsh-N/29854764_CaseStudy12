class Patient:
    def __init__(self, patient_id, name, date_of_birth, gender, contact_info):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_info = contact_info

    def __str__(self):
        return f"ID: {self.patient_id}, Name: {self.name}, DOB: {self.date_of_birth}, Gender: {self.gender}, Contact: {self.contact_info}"

class Doctor:
    def __init__(self, doctor_id, name, specialty, contact_info, available_dates):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.contact_info = contact_info
        self.available_dates = available_dates

    def __str__(self):
        available_dates_str = ", ".join(self.available_dates)
        return f"ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}, Contact: {self.contact_info}, Available Dates: {available_dates_str}"

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date, reason):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.reason = reason

    def __str__(self):
        return f"ID: {self.appointment_id}, Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}, Date: {self.appointment_date}, Reason: {self.reason}"

class HealthClinicManagementSystem:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        date_of_birth = input("Enter Date of Birth: ")
        gender = input("Enter Gender: ")
        contact_info = input("Enter Contact Info: ")
        self.patients[patient_id] = Patient(patient_id, name, date_of_birth, gender, contact_info)
        print("Patient added successfully.")

    def update_patient(self):
        patient_id = input("Enter Patient ID to update: ")
        if patient_id in self.patients:
            name = input("Enter Name: ")
            date_of_birth = input("Enter Date of Birth: ")
            gender = input("Enter Gender: ")
            contact_info = input("Enter Contact Info: ")
            self.patients[patient_id] = Patient(patient_id, name, date_of_birth, gender, contact_info)
            print("Patient updated successfully.")
        else:
            print("Patient not found.")

    def delete_patient(self):
        patient_id = input("Enter Patient ID to delete: ")
        if patient_id in self.patients:
            del self.patients[patient_id]
            print("Patient deleted successfully.")
        else:
            print("Patient not found.")

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
        else:
            for patient in self.patients.values():
                print(patient)

    def add_doctor(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Name: ")
        specialty = input("Enter Specialty: ")
        contact_info = input("Enter Contact Info: ")
        available_dates = input("Enter Available Dates (comma-separated): ").split(',')
        self.doctors[doctor_id] = Doctor(doctor_id, name, specialty, contact_info, available_dates)
        print("Doctor added successfully.")

    def update_doctor(self):
        doctor_id = input("Enter Doctor ID to update: ")
        if doctor_id in self.doctors:
            name = input("Enter Name: ")
            specialty = input("Enter Specialty: ")
            contact_info = input("Enter Contact Info: ")
            available_dates = input("Enter Available Dates (comma-separated): ").split(',')
            self.doctors[doctor_id] = Doctor(doctor_id, name, specialty, contact_info, available_dates)
            print("Doctor updated successfully.")
        else:
            print("Doctor not found.")

    def delete_doctor(self):
        doctor_id = input("Enter Doctor ID to delete: ")
        if doctor_id in self.doctors:
            del self.doctors[doctor_id]
            print("Doctor deleted successfully.")
        else:
            print("Doctor not found.")

    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.")
        else:
            for doctor in self.doctors.values():
                print(doctor)

    def add_appointment(self):
        appointment_id = input("Enter Appointment ID: ")
        patient_id = input("Enter Patient ID: ")
        doctor_id = input("Enter Doctor ID: ")
        appointment_date = input("Enter Appointment Date: ")
        reason = input("Enter Reason: ")
        self.appointments[appointment_id] = Appointment(appointment_id, patient_id, doctor_id, appointment_date, reason)
        print("Appointment added successfully.")

    def update_appointment(self):
        appointment_id = input("Enter Appointment ID to update: ")
        if appointment_id in self.appointments:
            patient_id = input("Enter Patient ID: ")
            doctor_id = input("Enter Doctor ID: ")
            appointment_date = input("Enter Appointment Date: ")
            reason = input("Enter Reason: ")
            self.appointments[appointment_id] = Appointment(appointment_id, patient_id, doctor_id, appointment_date, reason)
            print("Appointment updated successfully.")
        else:
            print("Appointment not found.")

    def delete_appointment(self):
        appointment_id = input("Enter Appointment ID to delete: ")
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            print("Appointment deleted successfully.")
        else:
            print("Appointment not found.")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments found.")
        else:
            for appointment in self.appointments.values():
                print(appointment)

def main():
    system = HealthClinicManagementSystem()

    while True:
        print("\nHealth Clinic Management System")
        print("1. Manage Patients")
        print("2. Manage Doctors")
        print("3. Manage Appointments")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n1. Add Patient")
            print("2. Update Patient")
            print("3. Delete Patient")
            print("4. View Patients")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                system.add_patient()
            elif sub_choice == '2':
                system.update_patient()
            elif sub_choice == '3':
                system.delete_patient()
            elif sub_choice == '4':
                system.view_patients()

        elif choice == '2':
            print("\n1. Add Doctor")
            print("2. Update Doctor")
            print("3. Delete Doctor")
            print("4. View Doctors")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                system.add_doctor()
            elif sub_choice == '2':
                system.update_doctor()
            elif sub_choice == '3':
                system.delete_doctor()
            elif sub_choice == '4':
                system.view_doctors()

        elif choice == '3':
            print("\n1. Add Appointment")
            print("2. Update Appointment")
            print("3. Delete Appointment")
            print("4. View Appointments")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                system.add_appointment()
            elif sub_choice == '2':
                system.update_appointment()
            elif sub_choice == '3':
                system.delete_appointment()
            elif sub_choice == '4':
                system.view_appointments()

        elif choice == '4':
            break

if __name__ == "__main__":
    main()
