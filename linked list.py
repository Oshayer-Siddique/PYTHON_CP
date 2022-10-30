print("Linked list creat and insertion")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def inser_afer(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def size_list(self):
        temp = self.head
        count = 0
        while (temp):
            temp = temp.next
            count = count.next
        return count


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(23)
    third = Node(34)
    forth = Node(345)

    llist.head.next = second
    second.next = third
    third.next = forth

    llist.push(1000)
    llist.inser_afer(second, 5)
    llist.printlist()
    print("lentgh of linked list", llist.size_list())

    print("Linked List activity")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def get_size(self):
        temp = self.head
        count = 0
        while (temp):
            temp = temp.next
            count = count + 1
        return count

    def getnth(self, index):
        temp = self.head
        count = 0
        while (temp):
            if count == index:
                return temp.data
            count = count + 1
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(534)
    third = Node(343)

    llist.head.next = second
    second.next = third
    llist.push(999)
    llist.insert_after(second, 1000)
    llist.printlist()
    print("size of LinkedList", llist.get_size())
    print("Nth node of LinkedList", llist.getnth(4))
