password = 'a123456'
i = 3
while i >= 0:
	i = i - 1
	pwd = input('please enter the password:')
	if pwd == password:
		print('LOGIN IN!!')
		break
	elif i > 0:
		print('wrong password,', i ,'times left')
	else:
		print('wrong password, account automatic locks')
		break

