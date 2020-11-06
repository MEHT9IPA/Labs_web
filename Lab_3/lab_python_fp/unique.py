class Unique(object):
    def __init__(self, items, **kwargs):
        self.unique_items = []
        self.items = iter(items)
        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = self.items.__next__()
            current_item = None
            if self.ignore_case and type(item) is str:
                current_item = item.lower()
            else:
                current_item = item
            if current_item not in self.unique_items:
                self.unique_items.append(current_item)
                return item

if __name__ == '__main__':
    data = [1, 3, 1, 3, 1, 2, 2, 5, 2, 2]
    print(list(Unique(data)))