def perm(list):
	if len(list) != 1:
		pWord = perm(list[1:])
		res = []
		for i in pWord:
			for j in range(len(i) + 1):
				res.append(i[:j] +  list[0] + i[j:])
		return res
	elif(len(list) == 1):		
		return [list]


print(perm('abc'))