import sys
from colorsys import yiq_to_rgb
from threading import Thread
from queue import Queue
from random import randint
from time import sleep
# =====================================================================
class Table():

    def __init__(self, number, guest):
        self.number = number
        self.guest = guest
# =====================================================================
class Guest(Thread):

    def __init__(self, name, done):
        Thread.__init__(self)
        self.name = name
        self.done = done

    def run(self):
        sleep(randint(3, 10)) # Random dining time 3...9 seconds
        self.done = True

# =====================================================================
class Cafe():
    q = Queue()
    empty_tbls = 0

    def __init__(self, *tables):
        self.tables = [Table(number, guest = None) for number in range(1, 6)]
        self.empty_tbls = len(self.tables)

    def guests_arrival(self, *guests):
        for i in range(len(guests)):
            for j in range(len(self.tables)):
                numtbl = 0
                if self.tables[j].guest == None:
                    numtbl = j+1
                    self.tables[j].guest = guests[i]
                    self.empty_tbls -= 1
                    guests[i].start()
                    print(f'{guests[i].name} has taken Table {self.tables[j].number}')
                    break
                else:
                    continue
            if numtbl == 0:
                self.q.put(guests[i])
                print(f'{guests[i].name} is waiting in queue')

    def serve_guests(self):
        while True:
            for i in range(len(self.tables)):
                if not self.tables[i].guest == None:
                    if not self.tables[i].guest.is_alive():
                        print(f'{self.tables[i].guest.name} has finished dining'
                              f'and left Table {self.tables[i].number}.') # См. комментарий в конце.
                        if not self.q.empty():
                            self.tables[i].guest = self.q.get()
                            print(f'Now {self.tables[i].guest.name} has taken Table {self.tables[i].number}')
                            self.tables[i].guest.start()
                        else:
                            self.tables[i].guest = None
                            self.empty_tbls +=1
                    else:
                        continue
                if self.empty_tbls == 5:
                    print('\nTom\'s Diner is empty of guests now.')
                    sys.exit()

cafe = Cafe()
guest_names = ['Alice', 'Elsie', 'Esme', 'Isabelle', 'Megan', 'Olivia',
               'Albert', 'Arthur', 'Daniel', 'George', 'James', 'Oliver']
guests = [Guest(name, done = False) for name in guest_names]
print('========================================\nWelcome to Tom\'s Dinder!\n\n(Tut, tut, too-dut,\n'
      'Tut, tu-doo, dut...\n\nRemeber Suzanne Vega\'s song\nof the early eighties?)\n'
      '========================================')
sleep(3)

cafe.guests_arrival(*guests)
cafe.serve_guests()

# Здесь по заданию я, по идее, должен присвоить столу статус "Свободен" (self.tables[i].guest = None), а потом только
# сажать за него гостя из очереди, но не вижу в этом смысла. Как только поток текущего гостя сдох, почему бы сразу не
# посадить за стол гостя из очереди?