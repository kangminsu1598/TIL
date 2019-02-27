data = int(input())
# 300s 60s 10s
a_push = (data // 300)
bc_data = (data % 300)

b_push = 0
while bc_data >= 60:
    bc_data = bc_data - 60
    b_push += 1

c_push = 0
while bc_data >= 10:
    bc_data = bc_data - 10
    c_push += 1

if bc_data != 0:
    print('-1')
else:
    print(f'{a_push} {b_push} {c_push}')

