import random
import threading

lock = threading.Lock

balance = 0

class Bank:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self):
        global balance  # Объявляем, что будем использовать глобальную переменную
        for i in range(99):  # Выполняем 99 итераций
            random_number = random.randint(50, 500)  # Генерируем случайное число
            balance += random_number  # Увеличиваем баланс
            print(f'Пополнение: {random_number}. Баланс: {balance}')




    def take(self):
        global balance
        for i in range(99):
            random_number_take = random.randint(50, 500)
            print(f'"Запрос на {random_number_take}"')
            if random_number_take <= balance:
                balance -= random_number_take
                print(f'"Снятие: {random_number_take}. Баланс: {balance}"')
            if random_number_take >= balance:
                print(f'"Запрос отклонён, недостаточно средств"')





bk = Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {balance}')


