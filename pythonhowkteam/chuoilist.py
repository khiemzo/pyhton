print('khiêm thiện bùi', end='')
print('khiem',"123",'####',sep='---------')

from time import sleep

your_name = "Henry"
your_great = "Hello! My name is "

for a in your_great + your_name:
    print(a, end='', flush=True)
    sleep(0.6)
print()
