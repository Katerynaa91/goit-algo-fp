"""Завдання 1. 
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
- написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
- розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
- написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список."""

class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


def reverse(head: LinkedList):
    """Функція, яка реалізує реверсування однозв'язного списку"""
    curr = head.head
    prev = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

"""Алгоритм сортування злиттям для однозв'язного списку"""
def split(head):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        if fast:
            slow = slow.next

    second = slow.next
    slow.next = None
    return second

def merge(first, second):
  
    if not first:
        return second
    if not second:
        return first

    if first.data < second.data:
        first.next = merge(first.next, second)
        return first
    else:
        second.next = merge(first, second.next)
        return second

def merge_sort(head):
  
    if not head or not head.next:
        return head

    second = split(head)
    head = merge_sort(head)
    second = merge_sort(second)
    return merge(head, second)

"""Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список"""
def merge_sorted_linked_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data < l2.data:
        l1.next = merge_sorted_linked_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_linked_lists(l2.next, l1)
        return l2

if __name__=="__main__":
    GREEN = '\033[32m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

    #перевірка функції сортування злиттям
    llist = LinkedList()
    llist.insert_at_end(111)
    llist.insert_at_end(1111111)
    llist.insert_at_end(1)
    llist.insert_at_end(111111111)
    llist.insert_at_end(11111111111)
    llist.insert_at_end(11111)

    print(CYAN + 'BEFORE SORTING:' + RESET)
    llist.print_list()

    print(CYAN + 'MERGE SORT RESULT:' + RESET)
    llist=merge_sort(llist.head)
    while llist is not None:
        print(llist.data)
        llist = llist.next


    #перевірка функції реверсування списку
    llist2 = LinkedList()
    llist2.insert_at_end(111111)
    llist2.insert_at_end(11111)
    llist2.insert_at_end(1111)
    llist2.insert_at_end(111)
    llist2.insert_at_end(11)
    llist2.insert_at_end(1)

    print('\n'+GREEN + 'BEFORE REVERSING:'+ RESET)
    llist2.print_list()

    print('\n'+GREEN + 'REVERSE RESULT:'+ RESET)
    llist2 = reverse(llist2)
    while llist2 is not None:
        print(llist2.data)
        llist2 = llist2.next
    
    #перевірка функції об'єднання двох відсортованих однозв'язних списків в один відсортований список
    list1 = LinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(3)
    list1.insert_at_end(11)
    list1.insert_at_end(20)

    list2 = LinkedList()
    list2.insert_at_end(4)
    list2.insert_at_end(12)
    list2.insert_at_end(25)

    print('\n'+YELLOW + "2 SORTED LINKED LISTS: " + RESET)
    list1.print_list()
    list2.print_list()

    print('\n'+YELLOW + "2 SORTED LINKED LISTS MERGED INTO 1 LINKED LIST: " + RESET)
    merged = merge_sorted_linked_lists(list1.head, list2.head)
    while merged is not None:
        print(merged.data)
        merged = merged.next