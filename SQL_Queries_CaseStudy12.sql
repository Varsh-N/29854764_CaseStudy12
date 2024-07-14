-- Query 1: Write a query to find the number of appointments scheduled for each doctor.
SELECT d.name AS doctor_name, COUNT(a.appointment_id) AS number_of_appointments
FROM healthclinic_managementsystem.doctors d
LEFT JOIN healthclinic_managementsystem.appointments a
ON  d.doctor_id = a.doctor_id
GROUP BY d.name;

-- Query 2: Write a query to find the patients who have appointments in the next week.
SELECT p.name AS patient_name, a.appointment_date, a.reason
FROM healthclinic_managementsystem.patients p
JOIN healthclinic_managementsystem.appointments a
ON p.patient_id = a.patient_id
WHERE a.appointment_date BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 7 DAY);

-- Query 3: Write a query to find the doctors who specialize in a specific field.
SELECT name AS doctor_name,specialty,contact_info
FROM healthclinic_managementsystem.doctors
WHERE specialty = 'Dermatology';

-- Query 4: Write a query to find the available dates for a particular doctor.
SELECT name AS doctor_name, available_dates
FROM healthclinic_managementsystem.doctors
WHERE name = 'Dr. Pavitra M';

-- Query 5: Write a query to find the appointment history of a specific patient.
SELECT p.name AS patient_name, d.name AS doctor_name, a.appointment_date, a.reason
FROM healthclinic_managementsystem.patients p
JOIN healthclinic_managementsystem.appointments a
ON p.patient_id = a.patient_id
JOIN healthclinic_managementsystem.doctors d
ON a.doctor_id = d.doctor_id
WHERE p.name = 'Varshaa'
ORDER BY a.appointment_date;






