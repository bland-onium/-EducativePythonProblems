# РИДМИ !!! README
# Когда решаем 27-ю, можно встретить несколько типов задач:
# 1.-Классика. В ней пункт А решается простым перебором как в 17-й
# 2.-Файлирование. Как правило мы должны среди кучи пар чисел найти те, которые дают наибольшую(наим) сумму и не делятся на что-то.
#Требует она правильной расстановки чтения всего списка значений и разложения его на множители
# 3.-Фантастика копирования. Одна из веселейший задачек - требует понимать как пользоваться командой int(input()) и как правило описывает "Ситуацию из жизни".
# Самый простой способ решения - прогнать её через кучу дулителей и делимостей, что приведет к быстрому и правильному ответу
# =-=
# Чтобы решить 27-ю - нужно преисполниться и понять что от тебя требуют. Лучше всего будет четкое построение и т.п., но за неимением ничего, кроме надежды - можно потыкаться с перебором
# ПЕРЕД РЕШЕНИЕМ ПОСМОТРИ ВНУТЬ ФАЙЛА !
#
# Everything will be fine... at once...
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# 27424
srt = open('27-B_demo.txt')# Выбираем один из существующих файлов(A or B(that's only your choice(you have no choice(: ))
n = srt.readline()
sum = 0 # Задаем сумму всех чисел из пар
min = 20001 # 10000 + 10000 + 1 (Максимально возможная сумма обоих чисел + 1(Не спорить!))
for i in range(int(n)): # Перебор всех пар чисел "n"
    cnt = srt.readline() # Строка из двух чисел превращается в список из двух чисел
    pos = cnt.index(' ') # Задаем область работы для "cnt". "index" says that you separate couple of numbers\
    # ( 7777 1024 -> [7777, 1024](later we'll imagine that this is two different names)
    dig1 = int(cnt[:pos]) # Задаём первое число из пары
    dig2 = int(cnt[pos+1:]) # Второе число из этого дуплета
    if dig1 > dig2: # Нужно задать условие нахождения максимально возможного числа
        sum = sum + dig1 # Сумма увеличивается с каждым новым членом
    else: # Или
        sum = sum + dig2
    if abs(dig1 - dig2)<min and abs(dig1-dig2)%3!=0: # "abs" - функция, которая находит модуль числа (-7 -> +7)
        min = abs(dig1 - dig2) # Минимальное значение тоже должно плавать для работы(Don't ask me why)
if sum%3!=0: # По условию не делится на 3
    print(sum) # Если всё хорошо и не делится на 3 - то пусть выводит
else:
    print(sum - min) # Если все плохо - то из суммы вычитаем минималку чтобы получить наибольшее не делящееся на 3 число

# 27889
srt = open('27-A_demo.txt')
count = int(srt.readline())
sum = 0
minn = 20001
for i in range(count):
    cnt2 = srt.readline()
    pos = cnt2.index(' ')
    pcs1 = int(cnt2[:pos])
    pcs2 = int(cnt2[pos+1:])
    if pcs1 < pcs2: # Теперь у нас минимально возможная сумма
        sum += pcs1
    else:
        sum += pcs2
    if abs(pcs1-pcs2)<minn and abs(pcs1-pcs2)%3!=0:
        minn = abs(pcs1-pcs2) # Не спрашивайте меня зачем эта хрень тут
if sum%3!=0:
    print(sum)
else:
    print(sum - minn) # Тут можно и "+" впихнуть, но я не знаю зачем

# 27890
srt = open('27-B_1.txt')
n = int(srt.readline())
sum = 0
minn = 20001
for i in range(n):
    cnt = srt.readline()
    pose = cnt.index(' ')
    pc1 = int(cnt[:pose])
    pc2 = int(cnt[pose+1:])
    if pc1>pc2:
        sum += pc1
    else:
        sum += pc2
    delta = abs(pc1 - pc2) # Now i decided to imagine our difference like "delta"
    if delta < minn and delta % 5 != 0:
        minn = delta
if sum%5!=0:
    print(sum)
else:
    print(sum - minn)

# 27891
# Вот тут что-то новенькое
# Algorythm for file "A"
# Решается почти аналогично 17-й задаче
srt = open('27-A_2.txt') # It's good only for "A"
n = []
for a in srt:
    n.append(int(a))
mx = 0
for i in range(len(n)-1):
    for j in range(i+1, len(n)):
        if n[i]*n[j]%14==0 and n[i]*n[j] > mx: # У нас произведение чисел делится на 14 => каждое новое, большее предыдущего становится новым числом
            mx = n[i]*n[j]
            print(mx)

# Algorythm for file "B"
srt = int(input()) # Ctrl+c -> ctrl+v всех значений из файла "B"
m7 = m2 = m14 = mx = maxall = 0 # Максимумы для всех делителей (mx2 - max for 2, another meanings are same)(maxall - max from maximums)
n = int(input()) # Первое чисто из пары
for i in range(srt-1): # Задаем перебор значений
    if n%14==0 and n>m14: # Ищем максимальное
        m14=n
    elif n%14==7 and n>m7: # Аналогично
        m7=n
    elif n%14==2 and n>m2:
        m2=n
    if n>mx:
        mx=n
    n = int(input()) # Второе число из пары
    if n%14==0 and n*mx>maxall: # Теперь выводим максимально большое произведение среди максимумов
        maxall = n*mx
    elif n%14 == 7 and n*m2 > maxall: # Для каждого числа
        maxall = n*m2
    elif n%14 == 2 and n*m7 > maxall:
        maxall = n*m7
    elif n*mx % 14 == 0 and n*mx > maxall:
        maxall = n * mx
    print(maxall) # Найденный максимум - то самое произведение из условия

# 27985
srt = int(input())
mx2=mx7=mx14=mx=maxall=0
n = int(input())
for i in range(srt-1):
    if n%2==0 and n%7!=0:
        mx2 = max(n, mx2)
    if n%7==0 and n%7!=0:
        mx7 = max(mx7, n)
    if n%14==0:
        mx14 = max(mx14, n)
    if n > mx:
        mx = n
    n = int(input())
    if n%14==7 and mx2*n > maxall:
        maxall = mx2*n
    if n%14==2 and mx7*n > maxall:
        maxall = mx7*n
    if n%14==0 and mx14*n > maxall:
        maxall = mx14*n
    if n*mx%14==0 and n*mx > maxall:
        maxall = mx*n
    print(maxall)

# 27986
# Код очень странный и постоянно выдает разные ответы, так что верить ему нельзя
srt = open('27986_A.txt')
mx7 = mx = 0
n = int(srt.readline())
for i in range(n):
    if n ==0: break
    if n%7==0 and n%49!=0 and n > mx7:
        mx7 = n
    if n%7==0 and n > mx:
        mx = n
    mxall = n*mx
    if mxall:
        print(mxall)
    else:
        print('1')

# 36040
s = open('27_A.txt')
n = int(s.readline())
smm = 0
mmx = float('inf')
for i in range(n):
    a,b,c = s.readline().split() # Для каждого числа из тройки даем свое значение
    a = int(a)
    b = int(b)
    c = int(c)
    smm += max(a,b,c) # Максимальная сумма нужных нам значение
    n1 = max(a,b,c)-min(a,b,c) # Одна из сумм, к которым изем делители
    deltn = a+b+c-max(a,b,c)-min(a,b,c)
    n2 = max(a,b,c)-deltn # # Вторая
    if n1%109!=0:
        mmx = min(mmx, n1) # Те самые условия делимости
    if n2%109!=0:
        mmx = min(mmx, n2)
if smm%109!=0:
    print(smm)
else:
    print(smm-mmx)

#27986
srt = open('27986_B.txt')
mx7=mx=0
while True:
    n = int(srt.readline())
    if n == 0: break
    if n%7==0 and n%49!=0 and n>mx7: mx7 = n
    if n%7!=0 and n%49!=0 and n>mx: mx = n
smm = mx7*mx
if smm:
    print(smm)
else:
    print('1')

# 27988
srt = int(input())
n = int(input())
mx13=mx2=mx26=mxspec=mxal= 0
for i in range(srt-1):
    if n%2==0 and n%13!=0:
        mx2 = max(mx2, n)
    if n%2!=0 and n%13==0:
        mx13 = max(mx13, n)
    if n%26==0:
        mx26 = max(mx26, n)
    if n > mxspec:
        mxspec = n
    n = int(input())
    if n%26==0:
        mxal = max(mxal, n)
    if n%2==0 and n%13!=0:
        mxal = max(mxal, n)
    if n%13==0 and n%2!=0:
        mxal = max(mxal, n)
    if n*mxspec%26==0:
        mxal = max(mxal, mxspec*n)
    print(mxal)
    #Just do not ask any questions
# 27989
# A
srt = open('27989_A.txt')
n = []
for a in srt:
    n.append(int(a))
mx = cnt = 0
for i in range(1,len(n)-1):
    for j in range(i+1, len(n)):
        if (n[i]*n[j])%26==0:
            cnt += 1
            print(cnt)
# B (Работает немного(~15%) быстрее предыдущей)
n = []
srt = int(input())
for i in range(srt):
    n.append(int(input()))
cnt = 0
for i in range(srt-1):
    for j in range(i+1, srt):
        if n[i]*n[j]%26==0:
            cnt+=1
            print(cnt)

print('jopa')