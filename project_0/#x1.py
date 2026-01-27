#x1


#Напишите функцию get_loto(num), генерирующую трёхмерный массив случайных целых чисел от 1 до 100 (включительно). 
# Это поля для игры в лото.Трёхмерный массив должен состоять из таблиц чисел формы 5х5, то есть итоговая форма — (num, 5, 5).
# Функция возвращает полученный массив.    


import numpy as np
def get_unique_loto(num):
    uniq_loto = np.empty((num, 5, 5))
    loto = np.arange(1,101)  
    for i in range(num):
        u_loto = np.random.choice(loto, size=(5,5), replace=False)
        uniq_loto = np.append(loto, u_loto)
    return uniq_loto
print(get_unique_loto(10))    