import os
import time

import Filler

prefix = '{remaining:02d} remaining'
suffix = '{current_value}/{max_value} ({percent:.2f}%)'

a = Filler.Filler(25, 0).set_prefix(prefix).set_suffix(suffix)

b = Filler.Filler(25, 0).set_fill_stages(
    ('(ﾉ◕ヮ◕)ﾉ', '(ﾉ◕ヮ◕)ﾉ*:', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧')).set_prefix(prefix).set_suffix(suffix)

c = Filler.Pie(25, 0).set_prefix(prefix).set_suffix(suffix)

arr = [a, b, c]

for i in range(len(arr)):
    thing = arr[i]
    print('printing {}:'.format(i))
    print(thing, end='\r')
    while not thing.complete():
        text = (' ' * os.get_terminal_size()[0]) + '\r'
        time.sleep(0.2)
        thing.next()
        text += str(thing)
        print(text, end='\r')

    print()
