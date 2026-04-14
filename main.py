def linear_search(elements:list,target:int) -> bool:
	for element in elements:
		if target == element:
			return True
	return False


if __name__ == "__main__":
	lst_element = [0,1,10,100,1_1000,10_000,100_000,1_000_000]
	for el in lst_element:
		elements = list(range(el))
		target = el-1
		result = linear_search(elements, target)
		print(f"Element {target} found in list: {result}")
