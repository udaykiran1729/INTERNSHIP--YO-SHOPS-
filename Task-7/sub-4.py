import csv
from datetime import date

# Function to mark attendance
def mark_attendance(employee_id):
    today = date.today()
    attendance_data = [str(today), employee_id]

    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(attendance_data)

# Example usage
employee_id = 'EMP001'
mark_attendance(employee_id)
