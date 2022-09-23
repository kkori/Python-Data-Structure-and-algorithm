# 1. 입력된 초를 시/분/초로 나누어 출력하는 코드를 작성하시오.
time = int(input("초를 입력하세요: "))
hour = time // 3600
time %= 3600
minute = time // 60
second = time % 60

print(f'{hour}시간 {minute}분 {second}초')
print()

# 2. 다음과 같은 출력결과를 얻기 위한 print 함수를 작성하시오.

print('''임진왜란은
1592년('선조 25년')부터
1598년까지 2차에 걸친
'왜군의 침략'으로
일어난 전쟁이다.''')
print()

# 3. 다음과 같은 출력결과를 얻기 위해서 print함수의 format함수를 이용하여 코드를 작성하시오.
# (필드폭과 정밀도 활용)

num1 = int(input("첫번째 정수 입력>> "))
num2 = int(input("두번째 정수 입력>> "))
print("덧셈, 뺄셈, 곱셈, 나눗셈, 나누기의 몫, 나누기의 나머지 계산")
print("{:5d} + {:5d} = {:10d}".format(num1, num2, num1 + num2))
print("{:5d} - {:5d} = {:10d}".format(num1, num2, num1 - num2))
print("{:5d} * {:5d} = {:10d}".format(num1, num2, num1 * num2))
print("{:5d} / {:5d} = {:10.2f}".format(num1, num2, num1 / num2))
print("{:5d} / {:5d}의 몫: {:7d}".format(num1, num2, num1 // num2))
print("{:5d} / {:5d}의 나머지: {:4d}".format(num1, num2, num1 % num2))
print()

# 4. 다음과 같은 결과가 나올 수 있도록 코드를 작성하시오, input 함수 사용

num3 = float(input("실수값 입력 >> "))
print("%.3f은 정수 %d과(와) 소수점 이하 %.3f로 구성" %(num3, int(num3), num3 - int(num3)))
print()
num4 = float(input("실수값 입력 >> "))
print("{:.4f}은 정수 {:d}과(와) 소수점 이하 {:.4f}로 구성".format(num4, int(num4), num4 - int(num4)))
print()

# 5. 다음과 같은 결과가 나올 수 있도록 코드를 작성하시오, 입력은 input 함수 사용하고, 입력의 형태는 두 종류의 알
# 파벳만 입력하도록 함, 즉 aaabbbbbb 또는 ccccccczzzzzzz 또는 ddddddaaa 이며 모두 소문자로 입력, 만약 대문자
# 입력 시 소문자로 변환 후 결과를 도출 함

ent_alpha = input("Enter alphabet >> ")
alpha_set = set(ent_alpha)
i = 0
while i < 1:
    if len(alpha_set) > 2:
        ent_alpha = input("Enter alphabet >> ")
        alpha_set = set(ent_alpha)
    else:
        i += 1
alpha1 = ent_alpha.lower()
alpha_list = list(alpha1)
alpha1_list = []
for i in alpha1:
    if i in alpha1_list:
        continue
    else:
        alpha1_list.append(i)
print("압축 결과는 {}{}{}{}".format(alpha1_list[0], alpha_list.count(alpha1_list[0]), alpha1_list[1], alpha_list.count(alpha1_list[1])))

ent_alpha2 = input("Enter alphabet >> ")
alpha_set2 = set(ent_alpha2)
i = 0
while i < 1:
    if len(alpha_set2) > 2:
        ent_alpha2 = input("Enter alphabet >> ")
        alpha_set2 = set(ent_alpha2)
    else:
        i += 1
alpha2 = ent_alpha2.lower()
alpha_list2 = list(alpha2)
alpha2_list = []
for i in alpha2:
    if i in alpha2_list:
        continue
    else:
        alpha2_list.append(i)
print("압축 결과는 {}{}{}{}".format(alpha2_list[0], alpha_list2.count(alpha2_list[0]), alpha2_list[1], alpha_list2.count(alpha2_list[1])))
