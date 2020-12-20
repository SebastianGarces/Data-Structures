class Node:
    def __init__(self, value, next_node=None):
        # value that the node is holding
        self.value = value
        # ref to next node in the chain
        self.next_node = next_node

    def __str__(self):
        return f"value: {self.value}, next node: {self.next_node}"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a new Node
        new_node = Node(value)
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in there
        else:
            # update the last node's "next_node" to the new node
            self.tail.set_next(new_node)
            # update the "self.tail" to point to the new node that we just added
            self.tail = new_node

    def add_to_head(self, value):
        # wrap the value in a new Node
        new_node = Node(value)
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in there
        else:
            # update the new node's next to the previous head
            new_node.set_next(self.head)
            # update the "self.tail" to point to the new node that we just added
            self.head = new_node

    def remove_tail(self):
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        # check if the list only has one item
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.tail.get_value()
            # remove the tail
            # set head and tail to None
            self.tail = None
            self.head = None
            # return the stored value
            return value
        # otherwise
        else:
            # store the last node value
            value = self.tail.get_value()
            # set tail to second to last node
            # we can only do this by traversing the whole list from beginning to end
            # starting from the head
            current_node = self.head
            # keep iterating until the node after "current_node" is the tail
            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()
            # set tail to "current_node"
            self.tail = current_node
            # set tail "next_node" to None
            self.tail.set_next(None)
            # return value
            return value

    def remove_head(self):
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        # check if the list only has one item
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.head.get_value()
            # remove the tail
            # set head and tail to None
            self.tail = None
            self.head = None
            # return the stored value
            return value
        else:
            # store the old head's value
            value = self.head.get_value()
            # set self.head to old head's next
            self.head = self.head.get_next()
            return value
