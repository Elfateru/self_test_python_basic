Задача 1. Имена
В базе данных одной компании
 есть баг (или, может быть, фича): если ввести
 туда имя сотрудника меньше чем из трёх букв, 
то база сломается и упадёт. Как компания принимает
 на работу людей, например, с китайскими именами, непонятно.

Дан файл people.txt, в котором построчно хранится N имён пользователей. 

Напишите программу, которая берёт
 количество символов в каждой строке 
файла и в качестве ответа выводит 
общую сумму. 
Если в какой-либо 
строке меньше трёх 
символов (не считая литерала \n),
 то вызывается ошибка, и программа завершается.