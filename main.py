#инициализация списка
list=[1,2,3,7,-12,-1,98,45,1,1,1]

#максимальное число
max=list[0]
#индекс
index=1

while index<len(list) :
    if list[index]>max :
        max=list[index]
        index+=1

print(f"максимальное число в списке : {max}")