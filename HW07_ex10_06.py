# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(list1):
	for i in range(len(list1)-1):

		if list1[i] > list1[i+1]:
			return False
		
	return True

def main():
	pass


if __name__ == '__main__':
    main()