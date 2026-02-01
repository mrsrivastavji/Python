class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next

class Singly:
    def __init__(self,head=None):
        self.head=head
    
    def insertEnd(self,value):
        temp=Node(value)

        if(self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp
        
        else:
            self.head=temp
    
    def print(self):
        t1=self.head
        while(t1.next!=None):
            print(t1.data)
            t1=t1.next
        print(t1.data)
    
obj=Singly()
obj.insertEnd(10)
obj.insertEnd(20)
obj.insertEnd(30)
obj.print()