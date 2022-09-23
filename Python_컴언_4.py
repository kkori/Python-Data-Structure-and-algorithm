import random as rand

#Problem_1
def pb1(li):
    num = min(li)
    li.remove(num)
    if len(li) == 0:
        li.append(-1)
    print("after deletion : ", end='')
    return li

#Problem_2
def pb2(num):
    sqrt = num ** 0.5
    if sqrt.is_integer():
        print(f'{num}의 제곱근은 {sqrt}')
    else:
        print(f'{num}의 제곱근은 -1')

if __name__ == '__main__':
    #1번
    check = 0
    while check < 1:
        count = int(input("Enter the number of lists >> "))
        if count >= 1 and count <= 10:
            check += 1

    list1 = [rand.randint(1, 100) for i in range(count)]
    print(f'original list : {list1}')
    print(pb1(list1))

    #2번
    while True:
        enter = int(input("enter positive integer >> "))
        if enter < 0:
            print("Wrong number")
        elif enter == 0:
            break
        else:
            pb2(enter)
