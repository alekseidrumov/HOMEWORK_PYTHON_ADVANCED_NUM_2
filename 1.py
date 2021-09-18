ourdict =	{
  3 : 5,
  1 : 3,
  5 : 7
}
while True:
    print('1 - вывод словаря, 2 - добавить пару,') 
    print('3 - удалить пару, 4 - изменить')
    print('5 - отсортировать, 6 - проверить наличие')
    print('7 - выход')
    what_do = input()
    if what_do == '1':
        print(ourdict)
    elif what_do == '2':
        type_element = input('1 - int, 2, - str : ')
        if type_element == "1":
            key = int(input("Какой ключ : "))       
        else:
            key = input("Какой ключ : ")
        type_element = input('1 - int, 2, - str : ')
        if type_element == "1":
            value = int(input("Какой значение : "))       
        else:
            value = input("Какой значение : ")
        ourdict.update({key: value})
    elif what_do == '3':
        pop_key = input('какой ключ пары, которую надо удалить : ')
        try:
            ourdict.pop(pop_key)
        except:
            ourdict.pop(int(pop_key))
    elif what_do == '4':
        name_key = input('Ключ по которому надо изменить значение : ')
        name_value = input('Значение, на которое изменить : ')

    elif what_do == '5':
        list = []
        for x,y in ourdict.items():
            list.append(x)
            list.append(y)
        list = sorted(list)
        print(list)
        for index, item in enumerate(list):
            if index % 2 == 0:
                ourdict[item] = list[index+1]
            


    elif what_do == '6':
        type_el = input('1 - int, 2 - str : ')
        if type_el == "1":
            search_el = int(input("Введите елемент : "))
            for x,y in ourdict.items():
                if x == search_el or y == search_el:
                    print("ЕСТЬ")
                    continue
            else:
                print("НЕТУ")
        if type_el == "2":
            search_el = input("Введите елемент : ")
            for x,y in ourdict.items():
                if x == search_el or y == search_el:
                    print("ЕСТЬ")
                    continue
            else:
                print("НЕТУ")
