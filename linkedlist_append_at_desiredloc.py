class node:
    def __init__(self,data=None):
        #print(1)
        self.data=data
        self.next=None
class ll:
    lst=[]
    def __init__(self):
        #print(1)
        self.head=None
    def append(self,data):
        #print("hi")
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        #print(self.head)
    def append_at_desired(self,k,data):
        if k>len(self.lst)+1:
            print("there is no such loc...could'nt add")
            return
        #print("hi1")
        new_node=node(data)
        c=1
        cur=self.head
        while(c<k):
            #print("hi2")
            cur=cur.next
            c+=1
        #print(cur.data)
        new_node.next=cur.next
        cur.next=new_node
    def display(self):
        #print("hi1")
        cur=self.head
        self.lst=[]
        while(cur):
            #print("hi2")
            self.lst.append(cur.data)
            cur=cur.next
        print(self.lst)
        print(len(self.lst))
t=ll()
t.append(1)
t.append(2)
t.append(3)
t.append(4)
t.append(5)
t.display()
t.append_at_desired(2,6)
t.display()
t.append_at_desired(8,6)
