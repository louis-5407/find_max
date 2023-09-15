	
class Math():
	def __init__(self, list):
		self.list = list

	def is_empty_array(self, arr):
		if not arr:
			return True
		else:
			return False

	def find_max(self, a_list):
		result = self.is_empty_array(a_list)

		if result:
			max_ = 0
		else:
			max_ = a_list[0]

		for n in a_list:
			if n > max_:
				max_ = n

		print(max_)

def main():
	b_list = [-1, 1]
	math = Math(b_list)
	print("在陣列中", math.list, "哪個最大？")

	math.find_max(b_list)


main()


			