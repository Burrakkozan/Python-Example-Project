
# i  1 dir 

# 1 example with parameters
name = 'ned'
def func():
    name ='stark'

func()
print(name) 

# 2 example with 
c_string = 'welcome to my house'
new_string = c_string.replace('welcome to', 'work') # replace method 'Changes the string'
print(new_string)

# 3 example with 
# upper and lover case
print("UpperCase".upper())
print("LowerCase".lower())

# 4 example with
# join method
list = ['a', 'b', 'c', 'd', 'e',]
print('--'.join(list))
print('??'.join(list))

# 5 example with
#if statement elseif  and create a function
num = 4
if ( num == 4):
    print('the num is 4')
if num > 5:
    print('the num is greater than 5')
elif (num < 5):
    print('the num is less than 5')
print(num)
# if elif else if 
""" dark = 'red'
if dark == 'Green':
    print('go')
elif dark == 'orange':
    print('slow down')
elif dark == 'red':
    print('stop')
    
else:
     print('something wrong')
 """

# 6 example with
# ınput method
name = input('what is your name?')
print('\nhello, ' + name)

# 7 example with
# lambda function - key word wiht MAP
# deger döndürür lambda
my_func = lambda num: 'hello' if num == 1 else 'bye'
print(my_func(2))

# verileri kümleri ayırmak için dict
# set kümeler için tuple kümeleri gruba dahil etmek için kullanılır
# 8 example with  #discard ve remove aynı silmek için kullanılır
# add, sub, mul, div, mod, pow, floor div, remove,update
def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

def calculator(n1,n2,func):
    return func(n1,n2)
print(calculator(2,3,add))
# 9 example with lambda wiht map function
map(func, list)
num_list = ['0', '1', '2', '3', '4']
doubble_list = map(lambda n: n * 2, num_list)
print(list(doubble_list)) # map double the values output 2,4,6,8,10

# 10 example with lambda wiht filter function
fun2 = list(filter(lambda n: n > 1 , num_list))
print(fun2)

# 11 example with dict, get, length method
car_store = dict(honda=12245, toyota=12345, bmw=12345)
second_car_store = {'tofas': 6462, 'ford': 12345}

print(car_store)
print(car_store.get('honda'))
car_store['mercedes'] = 12345
del car_store['toyota'] ## delete likse this otherwihise pop method
print(car_store)
toyota = car_store.pop('toyota')
print(toyota)
print(len(car_store))
print('toyota' in car_store) #key in existence? True or False
car_store.update(second_car_store) # update method
car_store.clear() # clear method
car_store = {1: 'BMW', 2: 'Mercedes', 3: 'Toyota'}
new_cars = {n-2: car  + "!" for (n,car) in car_store.items() if n > 1}
print(new_cars)

# 12 example with
set_A = {1,2,3,4,5}
set_C = {4,5,6,7,8}
set_B = {'a', 'b', 'c', 'd', 'e'}
print(set_A | set_B) # union
print(set_A.union(set_B)) # union
# intersection smilar
print(set_A & set_C)
print(set_A.intersection(set_C))
# difference 
print(set_A - set_C)
print(set_A.difference(set_C))

# 13 example with
import datetime
today = datetime.date.today()
print(today)
time_today = datetime.date.now()
print(time_today)
# import datetime as dt changes names 
import datetime as dt
date_today= dt.date.today()
print(date_today)
time_today = dt.datetime.now()
print(time_today.strftime("%H:%M:%S"))

# 14 example with heaqd 
import heapq
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)

minumum = heapq.heappop(heap) # pop the minimum value
# smallest value is 1
print(minumum)

# 15 example with
temp = 'education'
string = 'I am a student %s' % temp
print(string) # I am a student education 


# 16 example with
num_list = []
for i in range(1, 11):
    num_list.append(i) # append method add the value to the list eleman dizine ekler
print(num_list)

# 17 example with  
num_list = [1,2,3,5,6,7,8,9,10]
num_list.insert(3,4) # insert listeyi bi adim sag kaydırır
print(num_list)

# 18 example with
#append add remove and pop use remove sadece belirli bir ögeyi siler
num_list = [1,2,3,4,5,6,7,8,9,10]
num_list.append(11)
num_list.remove(10)
num_list.pop(2)
print(num_list)

# 19 example with
# index where is value of list
num_list = [1,2,3,4,5,6,7,8,9,10]
print(num_list.index(5))

# 20 example with
# in not in is there value of list var mı yok mu?
num_list = [1,2,3,4,5,6,7,8,9,10]
print(5 in num_list)
print(11 not in num_list)

# 21 example with
# sort kçükkten büyüge sıralar
num_list = [1,2,3,4,5,6,7,8,9,10]
num_list.sort()
print(num_list)


# 22 example with
dict() # create a dict dictionary olusturur bossa deger atamazsın

phone_book = {'ali': 12345, 'veli': 12345, 'ayse': 12345}
print(phone_book)
print(phone_book['ali'])


# 23 example with
# FOR LOOP
for i in range(1, 11): # Range method tamsayı   1 den  10 a dizisi olusturur
    
    if i % 2 == 0:
        print(i, " is tek")
    else:
        print(i, " is cift")

# for loop with example 
for i in range (1,11,3):  # 1 den 10 a kadar 3 er 3 er artar
    print(i)

# for yineleyici karakterlerde kullanılır in var mı yok mu elemen teyit loop with example
cars_list =  [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
print(cars_list)

for i in range(0, len(cars_list)): # len method uzunluk hepsine iki ekler 
    cars_list[i] = cars_list[i] + 2
print(cars_list)

# for loop  continue and break method (pass sadece yazılması için yazılır )
num_list = list(range(0,10))

for num in num_list:
    if num == 5:
        continue
    if num != 5:
        break
    print(num)


# for looop with


# 24 example with
class name: 
    def __init__(self,name):
        self.name = name + "!"
    def __eq__(self,other):
        return self.name == other.name