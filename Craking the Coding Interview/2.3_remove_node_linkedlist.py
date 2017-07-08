__author__ = 'Minsuk Heo & Chris Jones'
"""
Linked List
"""
class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def remove_item(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                next_node = cur.next.next
                cur.next = next_node
                break
            cur = cur.next

    def print_list(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)


ll = LinkedList(9)
ll.add(5)
ll.add(8)
ll.add(7)
ll.add(6)
ll.remove_item(8)
print(ll.print_list())
