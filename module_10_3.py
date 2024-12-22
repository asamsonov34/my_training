# ДЗ "Блокировки и обработка ошибок"

import threading
from random import randint
from time import sleep

class Bank:
    lock = threading.Lock()

    def __init__(self):
        self.balance = 500

    def deposit(self):
        for i in range(100):
            depsum = randint(50, 500)
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += depsum
            print(f'+++ Пополнение в сумме {depsum}. Баланс: {self.balance}. ')

    def draw(self):
        for i in range(100):
            sleep(0.001)
            drawsum = randint(50, 500)
            print(f'Запрос на снятие: {drawsum}', end = ' ••• ')
            if drawsum <= self.balance:
                self.balance -= drawsum
                print(f'Одобрено. Остаток: {self.balance}. ')
            else:
                print('Отклонено: недостаточно средств. ')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.draw, args=(bk,))

th1.start()
sleep(0.01) # Пытался подобрать, чтоб операции снятия и пополнения не слипались в одну строчку... или хотя бы пореже.
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')