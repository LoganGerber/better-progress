import os
import time

import Bar

prefix = '{remaining:02d} remaining'
suffix = '{current_value}/{max_value} ({percent:.2f}%)'

a = Bar.Bar(25, 0).set_prefix(prefix).set_suffix(suffix)


b = Bar.Bar(25, 0).set_bar_width(50).set_fill_character('@').set_empty_character(
    '.').set_bar_prefix('<').set_bar_suffix('>').set_prefix(prefix).set_suffix(suffix)


c = Bar.IncrementalBar(100, 0).set_bar_width(
    10).set_prefix(prefix).set_suffix(suffix)


d = Bar.RaisingIncrementalBar(100, 0).set_bar_width(
    10).set_prefix(prefix).set_suffix(suffix)


e = Bar.PixelBar(100, 0).set_bar_width(
    10).set_prefix(prefix).set_suffix(suffix)


f = Bar.ChargingBar(25, 0).set_prefix(prefix).set_suffix(suffix)


g = Bar.FillingSquaresBar(25, 0).set_prefix(prefix).set_suffix(suffix)


h = Bar.FillingCirclesBar(25, 0).set_prefix(prefix).set_suffix(suffix)

j = Bar.Bar(25, 0).set_bar_prefix('{bigdumb}').set_bar_suffix(
    '!!!').set_bar_prefix_kwargs({'bigdumb': 'LETS G'}).set_fill_character('O')


arr = [a, b, c, d, e, f, g, h, j]

for i in range(len(arr)):
    thing = arr[i]
    print('printing {}:'.format(i))
    print(thing, end='\r')
    while not thing.complete():
        text = (' '*os.get_terminal_size()[0]) + '\r'
        time.sleep(0.2)
        thing.next()
        text += str(thing)
        print(text, end='\r')

    print()