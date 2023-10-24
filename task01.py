#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891
import json
class main():
    def find(self,task = "task01a.txt"):
        with open(task,'r') as task1a:
            data = task1a.read()
            temp = json.loads(data)
            temp.sort()
            print(temp[-1])
            return temp[-1]

    def __init__(self) -> None:

        self.find()#BOO
        self.find("task01b.txt")
        self.find("task01c.txt")


main()



"""
with open('task01a.txt','r') as t1:
    #data = t1.read()
    t = json.loads(t1.read())
    t.sort()
    print(t)


import json
task1a =  open('task01a.txt','r')
data = task1a.read()
print(data)
temp = json.loads(data)
temp.sort()
print(temp)
print('-')
with open('task01a.txt','r') as t1:
    #data = t1.read()
    t = json.loads(t1.read())
    t.sort()
    print(t)
"""