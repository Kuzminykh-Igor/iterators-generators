class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.first_count = 0
        self.second_count = 0
        return self

    def __next__(self):
        if self.first_count >= len(self.list_of_list):
            raise StopIteration

        counter = self.list_of_list[self.first_count]
        if self.second_count >= len(counter):
            self.first_count += 1
            self.second_count = 0
            return self.__next__()

        item = counter[self.second_count]
        self.second_count += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()