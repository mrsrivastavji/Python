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
    
    def insertBeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp

    def insertMid(self,value,x):
        temp=Node(value)
        t1=self.head
        
        while(t1.next!=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            
            t1=t1.next

    def delete(self,value):
        t1=self.head
        pre=t1

        if(t1.data==value):
            self.head=t1.next

        while(t1.next!=None):
            if(t1.data==value):
                pre.next=t1.next
                break
            else:
                pre=t1
                t1=t1.next
        
        if(t1.data==value):
            pre.next=None
        
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
obj.insertBeg(5)
obj.insertMid(25,20)
obj.delete(5)
obj.print()