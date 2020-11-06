from lab_python_fp.field import field
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.gen_random import gen_random
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2

#чисто файл для тестов,
#основная часть выполнена в process_data
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Кресло', 'color': 'brown', 'm': 'meow'}
]
print(list(field(goods, 'color')))
print(list(field(goods, 'price', 'color')))
print("="*60)
