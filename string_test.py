# 파이썬 과거 단축
#print('일은 영어로 %s, 이는 영어로 %s' % ('one', 'two'))

# pyformat
print('{} {}'.format('one', 'two'))

#name = '강민수'
#e_name = 'Kang'
#print('안녕하세요. {}입니다. My name is {}'.format(name, e_name))

#f-string python 3.6
#print(f'안녕하세요.{name}입니다. My name is {e_name}')

#오늘의 행운의 번호는 ~~ 입니다, f-string 사용

import random
numbers = list(range(1,46))

lotto = random.sample(numbers,6)
lotto.sort()
print(f'오늘의 행운의 번호는 {lotto}입니다')
print("오늘의 행운의 번호는 {}입니다".format(lotto))

name = 'k'
print('안녕하세요'+ name +'입니다.')