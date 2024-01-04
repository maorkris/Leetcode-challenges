
class Node:
    def __init__(self,data, next):
        self.data = data
        self.next = next

class ConnectedList:
    def __init__(self,data):
        self.head = Node(data, None)

    def append1(self,data):
        new_Node = Node(data,None)
        temp_Node = self.head
        while temp_Node.next is not None:
            temp_Node = temp_Node.next

        temp_Node.next = new_Node

    def print_all_chine(self):
        temp_node = self.head
        while temp_node is not None:
            print(f" {temp_node.data} ==> ", end="")
            temp_node = temp_node.next


    def merge(list1, list2):
        temp_node1 = list1.head
        temp_node2 = list2.head
        if temp_node1.data <= temp_node2.data:
            little = temp_node1.data
            temp_node1 = temp_node1.next
        else:
            little = temp_node2.data
            temp_node2 = temp_node2.next
        list3 = ConnectedList(little)
        while temp_node1 is not None and temp_node2 is not None:
            if temp_node1.data <= temp_node2.data:
                list3.append1(temp_node1.data)
                temp_node1 = temp_node1.next
            else:
                list3.append1(temp_node2.data)
                temp_node2 = temp_node2.next


        if temp_node1 == None:
            while temp_node2 is not None:
                list3.append1(temp_node2.data)
                temp_node2 = temp_node2.next
            print()
            return ConnectedList.print_all_chine(list3)


        if temp_node2 == None:
            while temp_node1 is not None:
                list3.append1(temp_node1.data)
                temp_node1 = temp_node1.next

            print()
            return ConnectedList.print_all_chine(list3)




list1 = ConnectedList(1)
list1.append1(70)
list1.append1(200)
list1.append1(202)
list1.append1(213)
list1.append1(421)

list2 = ConnectedList(1)
list2.append1(3)
list2.append1(500)

list1.print_all_chine()
print()
list2.print_all_chine()

ConnectedList.merge(list1,list2)
