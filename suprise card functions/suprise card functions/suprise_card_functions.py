import random
suprise_crd = [1,2,3,4,5,6,7,8]
pick_crd = random.choice(suprise_crd)
print(pick_crd)

def sup_crd_func(pick_crd):
	if pick_crd == 1:
		print("a")

	elif pick_crd == 2:
		print("b")

	elif pick_crd == 3:
		print("c")

	elif pick_crd == 4:
		print("d")

	elif pick_crd == 5:
		print("e")

	elif pick_crd == 6:
		print("f")

	elif pick_crd == 7:
		print("g")

	elif pick_crd == 8:
		print("h")

sup_crd_func(pick_crd)
