old_list = [0,-2,5,4,12,-8,0,-56,45,100]
new_list = list()
#new_list = [i for i in old_list if i<=0]

#or
for i in old_list:
	if i<=0:
		new_list.append(i)

arr = map(int, raw_input().split())[:3]
print(type(arr))
print(arr)

print(new_list)
