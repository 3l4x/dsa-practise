"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
    def get_position(self, position):
        current = self.head
        index = 1
        while current and position != index:
            current = current.next
            index += 1
        if(index == position):
            return current
        return None

    def insert(self, new_element, position):
        current = self.head
        if(position==1):
            new_element.next = current
            self.head = new_element
            return
        #always enters if not early return
        previous = self.get_position(position-1)
        if(previous):
            new_element.next = previous.next
            previous.next = new_element

        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        pass

    def delete(self, value):
        if not(self.head):
            return

        if(self.head.value == value):
            self.head = self.head.next
        current = self.head
        while(current.next and current.next.value != value):
            current = current.next
        if(current.next and current.next.value == value):
            current.next = current.next.next
        """Delete the first node with a given value."""
        pass

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print( ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)
# Test insert
ll.insert(e4,3)
# Should print 4 now
print( ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print( ll.get_position(1).value)
# Should print 4 now
print( ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)