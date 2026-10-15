class Node:
  def __init__ (self, val):
    self.val=val
    self.next=None

class DLLNode:
  def __init__ (self, val):
    self.val=val
    self.next=None
    self.prev=None

class SLL:
    def __init__(self):
       self.head=None

    def display(self):
       if self.head is None:
          print("List is empty")
          return
       current=self.head
       while current is not None:
          print(current.val, end="-> ")
          current=current.next
       print("None")

    def insertAtStart(self, data):
       node=Node(data)
       if self.head is None:
          self.head= node
          return
       node.next=self.head
       self.head=node

    def insertAtEnd(self,data):
       node=Node(data)
       if self.head is None:
          self.head=node
          return
       current=self.head
       while current.next is not None:
          current=current.next
       current.next=node

    def insertAtPos(self, pos, data):
       if pos<0:
          print("invalid position")
          return
       if self.head is None or pos==0:
          self.insertAtStart(data)
          return
       current=self.head
       for  i in range(pos-1):
          current=current.next
          if current is None:
             print("invalid position")
             return
       node=Node(data)
       node.next=current.next
       current.next=node

    def removeAtStart(self):
       if self.head is None:
          print("list is empty")
          return
       self.head=self.head.next

    def removeAtEnd(self):
       if self.head is None:
          print("List is empty")
          return
       if self.head.next is None:
          self.head=None
          return
       current=self.head
       while current.next.next is not None:
          current=current.next
       current.next=None

    def removeAtPos(self,pos):
       if pos<0:
          print("invalid position")
          return
       if self.head is None:
          print("list is empty")
          return
       if pos==0:
          self.removeAtStart()
          return
       current=self.head
       for i in range(pos-1):
          current=current.next
          if current is None or current.next is None:
             print("invalid position")
             return
       current.next=current.next.next

    def rev(self):
       prev=None
       current=self.head
       while current is not None:
          next=current.next
          current.next=prev
          prev=current
          current=next
       self.head=prev

class CLL:
   def __init__(self):
      self.head=None

   def display(self):
      if self.head is None:
         print("List is empty")
         return
      current=self.head
      while True:
         print(current.val,end="->")
         current=current.next
         if self.head==current:
            break
      print(current.val)
   def insertAtStart(self, data):
      node=Node(data)
      if self.head is None:
        self.head= node
        node.next=self.head
        return
      current=self.head
      while current.next!=self.head:
         current=current.next
      current.next=node
      node.next=self.head
      self.head=node
   def insertAtEnd(self,data):
      node=Node(data)
      if self.head is None:
         self.head=node
         node.next=self.head
         return
      current=self.head
      while current.next!=self.head:
         current=current.next
      current.next=node
      node.next=self.head
   def insertAtPos(self, pos, data):
       if pos<0:
          print("invalid position")
          return
       if self.head is None or pos==0:
          self.insertAtStart(data)
          return
       current=self.head
       for  i in range(pos-1):
          current=current.next
          if current is None:
             print("invalid position")
             return
       node=Node(data)
       node.next=current.next
       current.next=node
   def removeAtStart(self):
       if self.head is None:
         print("list is empty")
         return
       current=self.head
       while current.next!=self.head:
         current=current.next
       self.head=self.head.next
       current.next=self.head
   def removeAtEnd(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next==self.head:
            self.head=None
            return
        current=self.head
        while current.next.next!=self.head:
            current=current.next
        current.next=self.head
   def removeAtPos(self,pos):
        if pos<0:
            print("invalid position")
            return
        if self.head is None:
            print("list is empty")
            return
        if pos==0:
            self.removeAtStart()
            return
        current=self.head
        for i in range(pos-1):
            current=current.next
            if current.next==self.head:
              print("invalid position")
              return
        current.next=current.next.next
   def rev(self):
      if self.head is None:
         print("List is empty")
         return
      prev=None
      current=self.head
      next=None
      while True:
         next=current.next
         current.next=prev
         prev=current
         current=next
         if current==self.head:
            break
      self.head.next=prev
      self.head=prev


class DLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.val, end=" <-> ")
            current = current.next
        print("None")

    def displayReverse(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current.next is not None:
            current = current.next

        while current is not None:
            print(current.val, end=" <-> ")
            current = current.prev
        print("None")

    def insertAtStart(self, data):
        node = DLLNode(data)

        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insertAtEnd(self, data):
        node = DLLNode(data)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = node
        node.prev = current

    def insertAtPos(self, pos, data):
        if pos < 0:
            print("invalid position")
            return

        if pos == 0:
            self.insertAtStart(data)
            return

        current = self.head

        for i in range(pos - 1):
            if current is None:
                print("invalid position")
                return
            current = current.next

        if current is None:
            print("invalid position")
            return

        node = DLLNode(data)
        node.next = current.next
        node.prev = current

        if current.next is not None:
            current.next.prev = node

        current.next = node

    def removeAtStart(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    def removeAtEnd(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.prev.next = None

    def removeAtPos(self, pos):
        if pos < 0:
            print("invalid position")
            return

        if self.head is None:
            print("List is empty")
            return

        if pos == 0:
            self.removeAtStart()
            return

        current = self.head

        for i in range(pos):
            current = current.next

            if current is None:
                print("invalid position")
                return

        current.prev.next = current.next

        if current.next is not None:
            current.next.prev = current.prev

    def rev(self):
        current = self.head
        prev_node = None

        while current is not None:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node
            current = current.prev

        if prev_node is not None:
            self.head = prev_node

    
class main:
   
  s=SLL()
  s.insertAtStart(10)
  s.insertAtStart(20)
  s.insertAtEnd(30)
  s.insertAtPos(3,25)
  s.display()
  s.rev()
  s.display()
  s.removeAtPos(2)
  s.display()

  c=CLL()
  c.insertAtStart(10)
  c.insertAtStart(20)
  c.insertAtEnd(30)
  c.insertAtPos(3,25)
  c.display()
  c.rev()
  c.display()
  c.removeAtStart()
  c.display()
  c.removeAtEnd()
  c.display()
  c.removeAtPos(1)
  c.display()

  
d = DLL()
d.insertAtStart(10)
d.insertAtStart(20)
d.insertAtEnd(30)
d.insertAtPos(2, 25)
d.display()
d.displayReverse()
d.rev()
d.display()
d.removeAtStart()
d.removeAtEnd()
d.removeAtPos(1)
d.display()
