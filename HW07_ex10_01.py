# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(list1):
	sum1=0
	
	for item1 in list1:
		if isinstance(item1,list):
			sum1+=nested_sum(item1)
		else:
			sum1 = sum1 + item1
	

	return sum1


def main():
	pass

	print nested_sum([9,8,7,[6,4],[7,8]])
if __name__ == '__main__':
    main()