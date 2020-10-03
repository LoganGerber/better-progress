import os
import time

import Bar

prefix = '{remaining:02d} remaining'
suffix = '{current_value}/{max_value} ({percent:.2f}%)'

a = Bar.Bar(25, 0).prefix(prefix).suffix(suffix)


b = Bar.Bar(25, 0).bar_width(50).fill_character(
    '@').empty_character('.').bar_prefix('<').bar_suffix('>').prefix(prefix).suffix(suffix)


c = Bar.IncrementalBar(100, 0).bar_width(10).prefix(prefix).suffix(suffix)


d = Bar.RaisingIncrementalBar(100, 0).bar_width(
    10).prefix(prefix).suffix(suffix)


e = Bar.PixelBar(100, 0).bar_width(10).prefix(prefix).suffix(suffix)


f = Bar.ChargingBar(25, 0).prefix(prefix).suffix(suffix)


g = Bar.FillingSquaresBar(25, 0).prefix(prefix).suffix(suffix)


h = Bar.FillingCirclesBar(25, 0).prefix(prefix).suffix(suffix)

j = Bar.Bar(25, 0).bar_prefix(
    '{bigdumb}').bar_suffix('!!!').bar_prefix_kwargs({'bigdumb': 'LETS G'}).fill_character('O')


arr = [a, b, c, d, e, f, g, h, j]

for i in range(len(arr)):
    thing = arr[i]
    print('printing {}:'.format(i))
    print(thing, end='\r')
    while not thing.complete:
        text = (' '*os.get_terminal_size()[0]) + '\r'
        time.sleep(0.2)
        thing.next()
        text += str(thing)
        print(text, end='\r')

    print()
