"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        has_no_items = self.head is None and self.tail is None
        if has_no_items:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        has_no_items = self.head is None and self.tail is None
        if has_no_items:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        is_head = node.prev == None
        if is_head:
            return None
        else:
            self.delete(node)
            self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        is_tail = node.next == None
        if is_tail:
            return None
        else:
            self.delete(node)
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        has_no_items = self.head is None and self.tail is None
        has_one_item = self.head == self.tail
        is_tail = node.next == None
        is_head = node.prev == None

        value = node.value

        if has_no_items:
            return None

        if has_one_item:
            self.tail = None
            self.head = None
        elif is_head:
            new_head = self.head.next
            self.head = new_head
            node.delete()
        elif is_tail:
            prev_node = self.tail.prev
            self.tail = prev_node
            node.delete()
        else:
            node.delete()

        self.length -= 1
        return value
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current_node = self.head
        max_value = 0
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
