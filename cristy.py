import datetime
import sys
import time
class ToDo(object):
    def __init__(self, Task, year, month, day, time_input):
        self.Task = Task
        self.year = year
        self.month = month
        self.day = day
        self.time_input = time_input

    def list(self):
       with open("task.txt", "r") as f:
           lists = f.read()
           print (lists)
          
    def remove(self,Task):
<<<<<<< HEAD
        with open("task.txt", "w" + "\n") as f:
            remove = f.write(Task)
            # print(remove)
            f.close()


    # def update(self, Task, year, month, day, time_input):
    #     with open("task.txt", "w" + "\n") as f:
    #         update = f.write(Task + ' ' + time_input + "\n" + day +'/'+ month +'/'+ year + "\n" + "\n")
    #         print(update)
    #         f.close()
=======
        with open("output.txt", "w" + "\n") as f:
            remove = f.write(Task)
            print(remove)
            f.close()


    def update(self, Task, year, month, day, time_input):
        with open("task.txt", "w" + "\n") as f:
            update = f.write(Task + ' ' + time_input + "\n" + day +'/'+ month +'/'+ year + "\n" + "\n")
            print(update)
            f.close()
>>>>>>> cbe87cee94946b9ccc853b447992d4b69a4fdc56


    def save(self, Task, year, month, day, time_input):
        with open("task.txt", "a+" + "\n") as f:
            f.write(Task + ' ' + time_input + "\n" + day +'/'+ month +'/'+ year + "\n" + "\n")
            


if __name__ == '__main__':

    
    Task = raw_input('To do: ')
    year = raw_input('Enter a year : ')
    month = raw_input('Enter a month : ')
    day = raw_input('Enter a day : ')
    time_input = raw_input("Please enter the time in HH:MM:SS format: ")
    



    t = ToDo(Task, year, month, day, time_input)
    t.save(Task, year, month, day, time_input)
    t.list()
<<<<<<< HEAD
    print(t.remove(Task))
    # t.update(Task, year, month, day, time_input)   
=======
    t.remove(Task)
    t.update(Task, year, month, day, time_input)   
>>>>>>> cbe87cee94946b9ccc853b447992d4b69a4fdc56
     