def find_max(a_list):
	max_ = a_list[0]

	for n in a_list:
		if n > max_:
			max_ = n

	print(max_)

def main():
	b_list = []
	find_max(b_list)

main()


			