#This a datastructure called a queque, it basicly is list of items/numbers/cars or games;)
#The object that goes first in the que will also go first out, just like a real queque
#When you want to know more about the Queue just Google Queue implementation.abs

#This Queue is build on top of a doubly linkedlist

class Node:
    def __init__(self, prev, value, next):
        self.Prev = prev
        self.Value = value
        self.Next = next
        self.IsEmpty = False
    
class Empty:
    def __init__(self):
        self.IsEmpty = True

class List:
    def __init__(self):
        self.Start = Empty()
        self.End = Empty()
    def IsEmpty(self):
        if self.Start.IsEmpty or self.End.IsEmpty:
            return True
        else:
            return False
    def Enqueue(self, item):
        #Add a new item to the back of the Que
        if self.IsEmpty(): 
            newNode = Node(Empty(), item, Empty())
            self.Start = newNode
            self.End = newNode
        else:
            newNode = Node(self.End, item, Empty())
            self.End.Next = newNode
            self.End = newNode
    def Dequeue(self):
        #Remove the first item from the Que
        if not self.IsEmpty():
            dequeued = self.Start.Value
            self.Start = self.Start.Next
            return dequeued
        else:
            return Exception("Que Empty Exception: Can not Dequeue an empty Que")
    def Peek(self):
        #Check the first item in the Que
        if not self.IsEmpty():
            return self.Start.Value
        else:
            return Exception("Que Empty Exception: Can not peek in an empty Que")

            
