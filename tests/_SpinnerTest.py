import os
import time

import better_progress.Spinner as Spinner

a = Spinner.Spinner()

b = Spinner.PieSpinner()

c = Spinner.MoonSpinner()

d = Spinner.LineSpinner()

e = Spinner.PixelSpinner()


arr = [a, b, c, d, e]

for i in range(len(arr)):
    sp = arr[i]
    print('printing {}:'.format(i))
    print(sp, end='')
    for j in range(10):
        text = '\r' + (' ' * os.get_terminal_size()[0]) + '\r'
        time.sleep(0.75)
        sp.next()
        text += str(sp)
        print(text, end='')

    print()
