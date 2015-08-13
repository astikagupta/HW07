def func1():
	fo = open("roster.txt","r")
	list2=[]
	list2=fo.readlines()
	
	for i in list2:
		print(i.strip())
	for line in fo:
		print "ho"
		x=line.strip()
		print x

def main():
	func1()

main()