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
