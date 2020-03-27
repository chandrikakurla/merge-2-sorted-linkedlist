#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #function for creating newnode and inserting it into linkedlist
    def insert(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while True:
            if lastnode.next is None:
                break
            lastnode=lastnode.next
        lastnode.next=newnode
    #function for printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    #function for merging 2 sorted linkedlist elements
    def Merge_2_sorted_lists(self,head1,head2):
        temp=None
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if (head1.data<=head2.data):
            temp=head1
            temp.next=self.Merge_2_sorted_lists(head1.next,head2)
        else:
            temp=head2
            temp.next=self.Merge_2_sorted_lists(head1,head2.next)
        #making least valued node as head node
        return temp
if __name__=='__main__':
    llist1=LinkedList()
    llist2=LinkedList()
    llist3=LinkedList()

    llist1.insert(5)
    llist1.insert(15)
    llist1.insert(20)
    print("linkedlist1 elements are:")
    llist1.printllist()

    llist2.insert(12)
    llist2.insert(21)
    llist2.insert(28)
    print("linkedlist2 elements are:")
    llist2.printllist()

    llist3.head=llist3.Merge_2_sorted_lists(llist1.head,llist2.head)
    print("merged linkedlist elements are:")
    llist3.printllist()
