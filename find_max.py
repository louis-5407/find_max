import Math_class  

def main():
	b_list = [-1, 1]
	math = Math_class.Math(b_list)
	print("在陣列中", math.list, "哪個最大？")

	math.find_max(b_list)


main()


			