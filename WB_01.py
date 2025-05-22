# หน่วยที่ 2: ตัวแปรและชนิดข้อมูลในภาษา Python

# 1. ประกาศตัวแปรพื้นฐาน
Name = "วรวุฒิ"
age = 20
height = 1.75
# ประกาศตัวแปร
Name = "สมชาย"
age = 18
height = 170.5
is_student = True

# 1. แสดงค่าตัวแปร
print("ชื่อ:", Name)
print("อายุ:", age)
print("ส่วนสูง:", height)
print("สถานะนักเรียน:", is_student)

# 2. แสดงชนิดข้อมูลของแต่ละตัวแปร
print("ชนิดของ Name:", type(Name))
print("ชนิดของ age:", type(age))
print("ชนิดของ height:", type(height))
print("ชนิดของ is_student:", type(is_student))

# 3. แสดงผลแบบรวมข้อความ
print("สวัสดี " + Name + " อายุ " + str(age) + " ปี")

# 4. รับค่าจากผู้ใช้และแปลงชนิดข้อมูล
income_str = input("กรุณากรอกรายได้ต่อวัน (บาท): ")
income = float(income_str)
days = int(input("จำนวนวันที่ทำงานในสัปดาห์: "))

weekly_income = income * days
print("รายได้ต่อสัปดาห์คือ:", weekly_income, "บาท")

# 5. ทดสอบการแปลงข้อมูลผิดพลาด
try:
    value = int("ABC")
except ValueError:
    print("ไม่สามารถแปลง 'ABC' เป็นจำนวนเต็มได้")
