''' 
Напишите функцию которая подсчитает количество счетных и несчетных чисел в списке
чисел.
'''
def even_odd_in_list(some_list):
    even = 0
    odd = 0
    i=0
    while i < len(some_list):
        if some_list[i]%2 == 0:
            even += 1
            i+=1
        else:
            odd += 1
            i+=1
    print(f"Данный список состоит из: {even} чётных чисел и {odd} нечетных чисел ")

spisok = [1, 2, 3, 4, 5, 8, 9, 6, 11, 25, 15, 32]
even_odd_in_list(spisok)