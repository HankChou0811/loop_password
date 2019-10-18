password = 'a123456'
i = 3
while i > 0:
	pwd = input('please enter the password:')
	if pwd == password:
		print('LOGIN IN!!')
		break
	else:
		i = i - 1
		print('wrong password,', i ,'times left')
		


