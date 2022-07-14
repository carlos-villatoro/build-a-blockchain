import hashlib

class Node:
    # no prev hash if this is the first node
    def __init__(self, value, prev_hash = 'head'):
        # this node's value
        self.value = value
        # hash from prev node
        self.prev_hash = prev_hash
        # ref to next node
        self.next = None
        # sha256(self.value + self.prev_hash)
        self.hash = Node.make_hash(self.value, self.prev_hash)

    def __str__(self):
        return f'{self.hash} : {self.value}'

    @staticmethod # decarator
    def make_hash(value, prev_hash):
        # creates the hash for a node
        history = str(value) + prev_hash
        # print('making an new node, history is:', history)
        return hashlib.sha256(history.encode()).hexdigest()

    @staticmethod
    def validate(prev_node, current_node):
        # check to see if the node has valid hashes
        if current_node.hash == Node.make_hash(current_node.value, prev_node.hash):
            return True
        else:
            return False

    @staticmethod
    def concensus(head):
        # if the head is the only node in the list, the list is valid
        if not head.next:
            return True
        # loop over a list and see if all nodes valid
        current_node = head
        while current_node.next:
            # if two nodes fail, we will retunr false
            if not Node.validate(current_node, current_node.next):
                return False

            current_node = current_node.next

        # return true after checking the entire list
        return True

head = Node(0)
# print('the head node:', head)
one = Node(1, head.hash)
head.next = one
# print('node one:', one)
two = Node(2, one.hash)
one.next = two
# print('node 2:', two)
three = Node(3, two.hash)
two.next = three
# print('node 3:', three)

# test validation
# print(Node.validate(one, two)) # true
# print(Node.validate(one, three)) # false


# test consensus
print(Node.concensus(head)) # true
print(Node.concensus(Node(10))) # true
two.value = 11
print(Node.concensus(head)) # false