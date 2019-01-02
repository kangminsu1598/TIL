#f = open('new.txt','w')
#f.write('Hello World')
#f.close()

#with open('new.txt','w') as f:
#    f.write('Hello') 덮어쓰기 write 수정하려면 append


#f = open('new.txt','r')
#data = f.read()
#print(data)
#f.close()

#with open('new.txt','r') as f:
 #   data = f.read()
  #  print(data)



# f = open('add.txt','w', encoding='utf-8')
# for i in range(1,10):
#     data = f'{i}번째 줄입니다. \n'
#     f.append(data)
# f.close

#with open('new.txt','w') as f:
#for i in range(2,10):
#    data = f'{i}번째 줄입니다. \n'
#    f.write(data)


# f = open('menu.txt','w',encoding='utf-8')
# f.writelines(menu)
# f.close()

# with open('menu.txt','w',encoding='utf-8') as f:
#     menu = ['카레\n','돈까스\n','햄버거\n']
#     f.writelines(menu)


#    menu = ['야호\t','이제\t','점심\t','시간\t','이다\t']


# with open('sentence.txt','w',encoding='utf=8') as f:
#     for i in range(1,5):
#         line = f'{i}번 가즈아\t'
#         f.write(line)

with open('new.txt', 'r') as f:
	lines = f.readlines()
	for line in lines:
		print(i.strip())