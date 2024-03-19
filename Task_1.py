class ListNode:
    """Клас для представлення вузла однозв'язного списку."""
    def __init__(self, value=0, next=None):
        self.value = value  # Значення поточного вузла
        self.next = next  # Посилання на наступний вузол

class LinkedList:
    """Клас для представлення однозв'язного списку."""
    def __init__(self):
        self.head = None  # Початковий вузол списку

    def append(self, value):
        """Додає новий вузол з заданим значенням у кінець списку."""
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def to_list(self):
        """Конвертує список у звичайний Python список для відображення."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self):
        """Реверсує однозв'язний список."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        """Сортує однозв'язний список використовуючи сортування злиттям."""
        self.head = self._merge_sort_rec(self.head)

    def _merge_sort_rec(self, head):
        if not head or not head.next:
            return head

        left, right = self._split(head)
        left = self._merge_sort_rec(left)
        right = self._merge_sort_rec(right)
        return self._merge(left, right)

    def _split(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid

    def _merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    @staticmethod
    def merge_sorted_lists(l1, l2):
        """Об'єднує два відсортованих списки в один."""
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.value < l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Забезпечуємо, що всі елементи з обох списків будуть додані
        tail.next = l1 or l2
        return dummy.next

def main():
    # Ініціалізація та наповнення двох списків
    llist1 = LinkedList()
    for value in [3, 4, 2, 7]:
        llist1.append(value)
    llist1.merge_sort()  # Сортуємо перший список

    llist2 = LinkedList()
    for value in [1, 5, 6, 8]:
        llist2.append(value)
    llist2.merge_sort()  # Сортуємо другий список

    # Виведення відсортованих списків
    print("Відсортований список 1:", llist1.to_list())
    print("Відсортований список 2:", llist2.to_list())

    # Об'єднання відсортованих списків
    merged_head = LinkedList.merge_sorted_lists(llist1.head, llist2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("Об'єднаний відсортований список:", merged_list.to_list())

if __name__ == "__main__":
    main()
