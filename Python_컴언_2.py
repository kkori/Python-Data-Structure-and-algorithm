# Problem_1

num = int(input("enter num of list >> "))

list1 = []
for i in range(num):
    enter_data = input("enter data >> ")
    list1.append(enter_data)

list2 = []
for i in range(num):
    obj = list1[i]
    if obj in list1[i+1:] and obj not in list2:
        list2.append(obj)
print(list2)
print()
# Problem_2

while True:
    year = int(input("연도를 입력하세요: "))

    if year < 0:
        print("program end!")
        break
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"    => {year}년은 윤년입니다")
    else:
        print(f"    => {year}년은 평년입니다")

print()
# Problem_3

number = int(input("정수를 한 개 입력하시오. >> "))
list3 = []

for i in range(1, number + 1):
    if number % i == 0:
        list3.append(i)

print(f'{number}의 약수는 {list3} 입니다.')
