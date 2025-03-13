
employees = [(1, "John", "HR"), (2, "Sunil", "IT"),(3, "Ramesh", "Finance"),]


attendance_records = [
    (1, "2025-03-01", "Present"),
    (2, "2025-03-01", "Absent"),
    (3, "2025-03-01", "Present"),
]

def mark_attendance(employee_id, date, status):
    attendance_records.append((employee_id, date, status))
    print(f"Attendance marked for Employee {employee_id}: {status}")
print ("-----------------------------------------------------------------------")

def search_attendance(employee_id):
    print(f"Searching Attendance for Employee ID {employee_id}:")
    for value in attendance_records:
     if value[0] ==  employee_id: 
           print(f"Date: {value[1]}, Status: {value[2]}")

    else: ("Value not found") 

       

mark_attendance(1, "2025-03-02", "Present")
mark_attendance(2, "2025-03-02", "Present")
mark_attendance(3, "2025-03-02", "Absent")

search_attendance(3)

