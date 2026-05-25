import locale

locale.setlocale(locale.LC_ALL, 'vi_VN')

transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "
transaction.strip()
parts = transaction.split("|")
print(parts)

student_name = parts[0].lower().title().strip()
course_code = parts[1].strip()
amount  = int(parts[2])
status = parts[3].upper()

print(f"""
    Học viên : {student_name}
    Khóa học : {course_code}
    Số tiền  : {amount:,} VND
    Trạng  thái : {status}
    """)

# phương pháp strip() chỉ tạo ra chuỗi bản sao 
# định dạng của amount phải được chuyền về int , nếu không chuyển sẽ không dùng được ép "," trong 
# định dạng tiền