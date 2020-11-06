def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            for arg in args:
                if arg in item:
                    yield item[arg]
    else:
        for item in items:
            new_item = {}
            arg_c = 0
            for arg in item:
                if arg in args:
                    arg_c += 1
            if arg_c == len(args):
                for i in item:
                    new_item[i] = item[i]
                yield new_item

if __name__ == '__main__':
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Кресло', 'color': 'brown', 'm': 'meow'}
    ]
    print(list(field(goods, 'color')))
    print(list(field(goods, 'price', 'color')))