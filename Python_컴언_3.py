import random as rand

# 1번
answer = rand.randint(1,30)
count = 0
your_li = []
while True:
    if count < 3:
        your = int(input("숫자를 입력하세요 >> "))
        your_li.append(your)
        if your == answer:
            print("You Win!!")
            count += 1
            print(f'정답은 {answer}, 입력하였던 숫자는 {your_li}입니다.')
            break
        elif your < answer:
            print("입력한 숫자가 정답보다 작습니다.")
            count += 1
        else:
            print("입력한 숫자가 정답보다 큽니다.")
            count += 1
    else:
        print(f'정답은 {answer}, 입력하였던 숫자는 {your_li}입니다.')
        break

# 2번
dict_f = {'A':90, 'B':80}

while True:
    num = int(input("start(1) or stop(0) : "))
    if num == 0:
        print("program end")
        break
    elif num == 1:
        search = input("Please enter a key to search. ex) C, D>> ")
        if search in dict_f.keys():
            ans = dict_f[search]
            print(f'{search}의 값은 {ans}')
            print(f'딕셔너리 :: {dict_f}')
        else:
            print("찾는 키가 없습니다, 딕셔너리에 추가할 값을 입력하세요")
            new = int(input(f'{search}에 해당되는 값 입력 :: '))
            dict_f[search] = new
            print(f'딕셔너리 :: {dict_f}')
    else:
        print("잘못된 숫자를 입력하였습니다.")


# 3번
while True:
    word = input("단어를 입력하세요: ")
    word_li = list(word)
    if word == 'quit':
        print("prgram end...")
        break
    else:
        for i in range(len(word_li) // 2):
            if word_li[i] != word_li[-i-1]:
                print(f'{word} is not palindrome')
                break
            else:
                if i == (len(word_li) // 2) - 1:
                    print(f'{word} is palindrome')
                    break
                continue
