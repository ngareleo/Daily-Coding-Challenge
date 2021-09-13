"""
This problem was asked by Twitter.

Implement an autocomplete system.
That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
"""


class Node:

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


class Letter(Node):

    def __init__(self, value, parents):
        super().__init__(value, parents)


class Link:

    def __init__(self, value=None, right=None):
        self.value = value
        self.right = right


class LinkedList:

    def __init__(self, root=None):
        self.root = root

    def add_item(self, value):
        new_link = Link(value)
        root = self.root
        while root.right:
            root = root.right
        root.right = new_link


class LeadLetter(Link):

    def __init__(self, value, child=None):
        super().__init__(value)
        self.child = child


class Dictionary(LinkedList):

    def __init__(self, root=None):
        super().__init__(root)
        self.root = LeadLetter('A')
        for i in range(66, 91):
            lead_letter = LeadLetter(value=chr(i))
            self.add_link(lead_letter)

    def print_dict(self):
        root = self.root
        while root is not None:
            print(root.value)
            root = root.right

    def add_link(self, link):
        root = self.root
        while root.right:
            root = root.right

        root.right = link

    def add_word(self, word):
        """
             a -> b -> c -> d
           /|\
         p  b c

         we need to transverse through the Dictionary looking for the lead letter we need

         We then look for nodes that pre-exist that are linked to the lead letter


        :return:None
        """


if __name__ == '__main__':

    pass
