def print_result(func, *args):
    def decorator(*args):
        print(func.__name__)
        result = func(*args)
        if type(result) is list:
            for item in result:
                print(item)
        elif type(result) is dict:
            for key, item in result.items():
                print(str(key) + ' = ' + str(item))
        else:
            print(result)
        return result
    return decorator



if __name__ == '__main__':
    @print_result
    def test_1():
        return 1

    @print_result
    def test_2():
        return 'iu5'

    @print_result
    def test_3():
        return {'a': 1, 'b': 2}

    @print_result
    def test_4():
        return [1, 2]
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()