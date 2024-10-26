import unittest

from linked_list.insert_at_tail import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert_at_tail_empty_list(self):
        ll = LinkedList()
        ll.insert_at_tail(10)
        self.assertEqual(ll.head.data, 10, "Head should be 10")
        self.assertEqual(ll.tail.data, 10, "Tail should also be 10")
        self.assertIsNone(
            ll.head.next, "Head.next should be None in a single-element list"
        )

    def test_insert_at_tail_multiple_elements(self):
        ll = LinkedList()
        ll.insert_at_tail(10)
        ll.insert_at_tail(20)
        ll.insert_at_tail(30)
        self.assertEqual(ll.head.data, 10, "Head should be 10")
        self.assertEqual(ll.head.next.data, 20, "Second element should be 20")
        self.assertEqual(ll.tail.data, 30, "Tail should be 30")
        self.assertIsNone(ll.tail.next, "Tail.next should be None")

    def test_continuity(self):
        ll = LinkedList()
        ll.insert_at_tail(10)
        ll.insert_at_tail(20)
        ll.insert_at_tail(30)
        current = ll.head
        count = 0
        while current:
            count += 1
            current = current.next
        self.assertEqual(count, 3, "There should be 3 elements in the list")


if __name__ == "__main__":
    unittest.main()
