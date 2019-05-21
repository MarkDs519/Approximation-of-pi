# imported math library for pi and square root function
import math


def basel(precision):
	"""
	Function to calculate value of pi using Basel method. Function takes precision as an input and ouputs x as closest
	value of pi in accordance with precision and 'n' number of steps used to find 'x'
	:param precision: the precision
	:return: value of pi close to precision as output and number of steps
	"""

	# number of steps
	n=0
	# multiplying factor. different from iteration
	i=1
	previousValue=0
	# n is 1 here. set value for while loop condition
	x= math.sqrt(6*1)
	# iterate until we find the proper approximation as intended
	while precision < abs(math.pi - x):
		# calculating using basel method. Separated each opeartion to prevent and reduce error
		previousValue = previousValue+(1/(i*i))
		x = math.sqrt(6*previousValue)
		#increment step number and multiplying denominator factor
		n=n+1
		i=i+1
	# value of pi close to precision as output
	return (x,n)


def taylor(precision):
	"""
	Function uses Taylor expansion theorem to find value of pi. It takes precision as an input and ouputs x as closest
	value of pi in accordance with precision and 'n' number of steps used to
	find 'x'
	:param precision:
	:return: value of pi close to precision as output and number of steps
	"""
	# a list of all the terms
	list_of_terms = []
	# number of steps
	n = 0
	# the approximation
	x = 0
	# iterate until we find the proper value for x
	while precision < abs(math.pi - x):
		# calculating the term
		term = (-1) ** n / (2 * n + 1)
		list_of_terms.append(term)
		x = 4 * (sum(list_of_terms))
		n = n + 1

	return (x, n)


def wallis(precision):
	"""
	Function uses Wallis' method to find value of pi. It takes precision as an input and ouputs x as closest
	value of pi in accordance with precision and 'n' number of steps used to find 'x'
	:param precision:
	:return: value of pi close to precision as output and number of steps
	"""
	#initialize values
	i=1 #multiplying factor. different from iteration
	n=0 #number of steps
	previousValue=1
	x = 2*previousValue #n is 1 here. set value for while loop condition
	while precision < abs(math.pi - x):
		#calculating using wallis' method. Separated each opeartion to prevent or reduce error
		previousValue = previousValue*((2*i) * (2*i)) / (((2*i)-1)*((2*i)+1))
		x=2*previousValue
		#increment step and multiplying integer
		i=i+1
		n=n+1

	return (x,n)

def spigot(precision):
	"""
	Function uses Spigot method to find value of pi. It takes precision as an input and ouputs x as closest
	value of pi in accordance with precision and 'n' number of steps used to find 'x'
	:param precision:
	:return: value of pi close to precision as output and number of steps
	"""
	#initialization of parameters
	# number of steps
	n=2
	# the initial numerators and denominators are harcoded
	numerator = 2
	denominator = 5
	productValue= 1/3
	# initial sum
	sumValue = 1+(1*productValue)
	# calculating the first sum
	x = 2*sumValue
	while precision < abs(math.pi - x):
		#calculating using spigot method. Separated each opeartion to prevent or reduce error and simplicity
		previousValue = (productValue*(numerator/denominator))
		sumValue = sumValue + previousValue
		x=2*sumValue
		#increment required arguments
		productValue = previousValue   # the new product will be the calculated multiplication of the terms
		numerator += 1
		denominator += 2
		n += 1

	return (x, n)  #value of pi close to precision as output


def race(precision, arrayFunction):
	"""
	This function checks which algorithm took how much steps for
	estimating value of pi. It then provides the output in ascending order. The precision is in float format.
	The list of functions is kept as a list of strings for comparison between methods
	:param precision:
	:param arrayFunction: list of functions
	:return: sorted list of
	"""
	list_of_integer_pairs = []
	for i in range(len(arrayFunction)):
		#check which element in the array belongs to which method and then add the index and the number of steps in the
		# list. Note: we are adding 1 to the index only for visualization as in the assignment results given
		if arrayFunction[i] == "wallis":
			approximation, num_steps = wallis(precision)
			list_of_integer_pairs.append((i+1, num_steps))
		elif arrayFunction[i] == "basel":
			approximation, num_steps = basel(precision)
			list_of_integer_pairs.append((i+1, num_steps))
		elif arrayFunction[i] == "taylor":
			approximation, num_steps = taylor(precision)
			list_of_integer_pairs.append((i+1, num_steps))
		else:
			approximation, num_steps = spigot(precision)
			list_of_integer_pairs.append((i+1, num_steps))

	#now that we have our data, we sort the list in ascending order. That is why the list was made. To make sorting easy
	sorted_list = selection_sort(list_of_integer_pairs)

	return sorted_list

def selection_sort(list_of_elements):
	"""
	This function iterates over the elements in the list and sorts out the elements in ascending order
	:param list_of_elements: array of elements
	:return: sorted array of elements
	"""

	i = 0
	# iterate over the list
	while i < len(list_of_elements):
		# set the minimum index
		minimum_index = i
		# set the pointer to the next element
		j = i+1
		# iterate and check element at j with the chosen element at i
		while j < len(list_of_elements):
			# if the chosen element is > element at j, then change the index for swap
			if list_of_elements[minimum_index][1] > list_of_elements[j][1]:
				minimum_index = j
			j += 1
		# perform the swap
		list_of_elements[i], list_of_elements[minimum_index] = list_of_elements[minimum_index], list_of_elements[i]
		i += 1
	return list_of_elements

	#function open. This functions prints the output from our function
#in a format that is easy for regular humans(users) to comprehend
def print_results(array2):
	"""
	print the number of the algorithm and the number of steps it took
	:param array2:
	:return:
	"""
	for i in range(len(array2)):
		#print as per stated format in question
		print("Algorithm " + str(array2[i][0]) + " finished in " + str(array2[i][1]) + " steps ")

# ask for user input
precision = float(input("Enter precision values: "))

list_of_algorithms = []
algorithms = input("Enter the name of the algorithm you want to use: ")
list_of_algorithms.append(algorithms)
while True:
    prompt_more_algorithms = input("Do you want add any other algorithm? y or n: ")
    if prompt_more_algorithms == "y":
        algorithms = input("Enter the name of the algorithm you want to use: ")
        list_of_algorithms.append(algorithms)
    else:
        break

print("List of algorithms: ", list_of_algorithms)
#print("wallis: ", wallis(0.01))
print("basel: ", basel(precision))
#print("taylor: ", taylor(0.2))
#print("spigot: ", spigot(0.1))
race_result = race(precision, list_of_algorithms)
print("race result: ", race_result)
print("")
print_result = print_results(race_result)

