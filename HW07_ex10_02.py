# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(list1):
	
	#for item in list1:
	if isinstance(list1,list):   # checks if each item is a list itself
		return [capitalize_nested(s) for s in list1]

			#list2.append(capitalize_nested(s) for s in item) # capitalizes just the first letter
	else:
			# list2.append(item.capitalize())
			 # append imp here to store all the elements in the list and not just the last one
		return list1.capitalize()

	

def main():
	
	
	pass
	

if __name__ == '__main__':
    main()
