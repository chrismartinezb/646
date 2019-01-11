#This is the max sub array problem, in which as stated in the README file ask us to retrive the maximum sum of consecutive numbers within a given array.

#Let us read the input first from the shell command, to make it easier we are going to use sys.argv to read the first argument given in shell, so we import the
#necessary module
import sys
#We use the open function to read our txt file from the 1st argument we pass in shell.
with open(sys.argv[1], 'r') as f:
	#We use split function for readability so we split by the commas
    contents = f.read().split()
#We use a list comprehension to accomplish 2 things: 1 create a list so is easier to work with the numbers and 2 transform the str numbers into int so we
#can perform operations with this list of numbers.
l = [int(i) for i in contents]    

#We could tackle this problem using brute force: checking all the possible consecutive sums and returning the biggest, but that can be unefficient since probably
#our self driving cars is going to output a lot of int per second so we will approach this problem using the famouse Kadene's algorithm.


#----------------------------------------------------------KADANE'S ALGORITHM-------------------------------------------------------------------------------------------#
#The main idea behind kadene's algorith is that when iterating through our list, the current greatest sum is going to be either our current index or our the
#current element + the previus max sum.


#Lets define our function 'kadane', it will take a list of int as an input.
def kadane(L):
	'''Takes a list of integers L as input and outputs the max consecutive sum
	of a sub array within list L:

	list=[3 ,-5 ,1 ,2 ,-1 ,4 ,-3 ,1 ,-2] the return will be 6, for the sub array: 1+2 +(-1)+4 = 6

	 '''

	#We need to keep track of both current and local max sum, we will set them both to the first index of our list and then update.
	max_curr = L[0]
	max_glob = L[0]
	#We will check each element of our list starting from the 2nd one (idx 1) since there is no previus one to the first (idx 0) and we already set our 
	#max_curr and glob_curr to that index.
	for i in range(1,len(L)-1):
		#Check if the current element is bigger than the current element plus the previus biggest sum and set the biggest as the max_curr.
		max_curr = max(L[i],max_curr+L[i])
		#Check if the max_curr is bigger than then max_glob, if so we set the max_curr as our new global
		if max_curr > max_glob:
			max_glob = max_curr
    #After iterating through out the list, we can safely print our biggest sum. 			
	return(max_glob)

    		
#Lets define thw next function: Kadene_01 who takes as input 3 values L= a list of numbers, values= an interger that restricts the maximum length of the subsequence
#or difference= it is also and int the restricts the length of the substring but if passed, instead of the sum of the values we want to find the highest sum of the absolute values of the 
#differences of neighboring pairs and.

def kadane_01(L,values=None,differenece=None):

	curr = 0
	global_ = 0

	if values:
		values = int(values)
		for i in range(0, len(L) - 1):
			curr = kadane(L[i : i + values])
			if curr > global_:
				global_ = curr
		return global_		

	if differenece:
		differenece = int(differenece)
		L=[abs(L[i] - (L[i + 1])) for i in range(0, len(L) - 1)]
		for i in range(0, len(L) - 1):
			curr=kadane(L[i : i + differenece])
			if curr > global_:
				global_ = curr
		return global_		



if sys.argv[2] and sys.argv[3] == 'values':
	values=sys.argv[2]
	print(kadane_01(l,values=values))
if	sys.argv[2] and sys.argv[3] == 'differences':
	differenece=sys.argv[2]
	print(kadane_01(l, differenece = differenece))
else:
	print('Error: Passed argument not correct, please entry an int followed by a string: "differences" or "values"')