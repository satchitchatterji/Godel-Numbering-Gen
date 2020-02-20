# Translates Expressions to Godel Numbers and vice versa.
# Base PM numberings based on "Godel's Proof" (Nagel & Newman)

# a hash table might be better?
signs = {'~':1,'v':2,'>':3,'E':4,'=':5,'0':6,'s':7,'(':8,')':9,',':10,'+':11,'*':12,'x':13,'y':17,'z':19}
signs_inv = {1:'~',2:'v',3:'>',4:'E',5:'=',6:'0',7:'s',8:'(',9:')',10:',',11:'+',12:'*',13:'x',17:'y',19:'z'}

def is_prime(n) : 
    if (n == 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True 

def next_prime():
	# generator that yields incremental primes
	i = 1; 
	while True: 
		if(is_prime(i)):
			yield i
		i += 1     
  
def get_primes(strlen):
	# returns list of strlen primes
	arr = []
	i = 2
	for num in next_prime():
		if(len(arr) > strlen):
			break
		arr.append(num)
	return arr

def create_godel(string):
	# creates godel number from expression string
	total = 1
	primes = get_primes(len(string))
	i = 0
	for char in string:
		total*=(primes[i]**signs[char])
		i+=1
	return total

def find_expression(g_no):
	for prime in next_prime():
		if(g_no == 1):
			break
		curcount = 0
		while ((g_no % prime)==0):
			g_no = g_no//prime
			curcount += 1
		if (curcount != 0):
			print(signs_inv[curcount], end = "")

if __name__ == "__main__":
	# main code
	while True:
		# Example: ~(Ex)(x=sy)
		opt = int(input("\nEnter 1 for Exp->Num, Enter 2 for Num->Exp: "))
		if(opt == 1):
			print(create_godel(input("Enter a string: ")))
		else:
			find_expression(int(input("Enter number: ")))
	