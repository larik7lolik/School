from get_push_data import get_data
from add_data import add_data

def operations():
    print('Что делаем: \n1 - получаем информацию  об учениках \n2- добавляем ученика\n3 - выходим из программы')
    a=input('Выберите действие: ')
    while True:
        if a == '1':
             print(*get_data())
             operations()
        if a =='2':
            add_data()
            operations()
        if a == '3':
            print('Спасибо за сеанс, работа закончена.')
            exit()
        
      
   
       
   


    
