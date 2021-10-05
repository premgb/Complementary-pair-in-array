###################################################################################################
#                      find complementary pair in an array of integers                            #
###################################################################################################

import itertools
import sys

#function to verify if user has entered valid input
def verify_input(str_arr, K):	
	A = list()
	for num in str_arr.split(' '):
		try:
			A.append(int(num))
		except ValueError:
			print("Array can only have integer(s)")
			sys.exit(1)

	try:
		K = int(K)
	except ValueError:
		print("K value can only be a valid integer")
		sys.exit(1)

	return A, K


#function to identify complementary pair indices
def complementary_pair(A, K):
	#pair_values = list((val_i,val_j) for (val_i,val_j) in list(itertools.combinations(A, 2)) if val_i+val_j==K)
	
	pair_indices = list((i,j) for ((i,val_i),(j,val_j)) in list(itertools.combinations(enumerate(A), 2)) if val_i+val_j==K)
	return pair_indices


if __name__ == "__main__":
    #ask user to enter array of integer(s) & K value
	str_arr = input("Enter an array of integer(s) separated by space: ")
	K = input("Enter K value: ")
	
	A, K = verify_input(str_arr, K)

	print("{}-Complementary pair indices in this array are: {}"
		.format(K, complementary_pair(A, K)))