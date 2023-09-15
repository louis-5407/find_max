def find_max(a_list):
	if not a_list:
		max_ = 0
	else:
		max_ = a_list[0]

	for n in a_list:
		if n > max_:
			max_ = n

	print(max_)

def main():
	b_list = [-1]
	find_max(b_list)

main()


			