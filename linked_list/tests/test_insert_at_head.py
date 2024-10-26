import unittest

from linked_list.insert_at_head import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert_at_head(self):
        ll = LinkedList()
        ll.insert_at_head(10)
        self.assertEqual(ll.head.data, 10, "The head should contain the data 10 after insertion.")

        ll.insert_at_head(20)
        self.assertEqual(ll.head.data, 20, "The head should now contain the data 20 after another insertion.")
        self.assertEqual(ll.head.next.data, 10, "The second element should be 10.")
