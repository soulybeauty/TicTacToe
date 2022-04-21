import random as r 

### Start here: common variables;



block_values = {
        1 : "_ ",
        2 : "_ ",
        3 : "_ ",
        4 : "_ ",
        5 : "_ ",
        6 : "_ ",
        7 : "_ ",
        8 : "_ ",
        9 : "_ "
    }


combinations = (
    [1,2,3],[1,4,7],[1,5,9],
    [2,5,8],[3,6,9],[3,5,7],
    [4,5,6],[7,8,9]
)


user1_blocks = []
user2_blocks = []


available_blocks = [1,2,3,4,5,6,7,8,9]


### check functions;
def check(a):

  global available_blocks
    
  try:

    available_blocks.remove(a)
    return 1

  except:

    return 0


### user inputs

def user_inputs_1():

	global available_blocks
    
	try:

		user_1 = int(input("\nEnter a block number (Player 1): \n"))
	
		
		if user_1 not in available_blocks:

			print("\nTaken! or don't use block number out of index!\n")
			print(f"\nYou can input : {available_blocks}")
			user_1 = user_inputs_1()

		else:

			available_blocks.remove(user_1)
			
	except:

		print("Enter valid input!\n")
		user_1 = user_inputs_1()
		
	return user_1

def user_inputs_2():

	global available_blocks

	try:

		user_2 = int(input("\nEnter a block number (PLayer2): \n"))

		if user_2 not in available_blocks:

			print("\nTaken! or don't use block number out of index!\n")
			print(f"\nYou can input : {available_blocks}\n")
			user_2 = user_inputs_2()

		else:

			available_blocks.remove(user_2)
		
	except:

		print("\nEnter valid input!\n")
		user_2 = user_inputs_2()
		
	return user_2



def visual(a = None, b = None):

	global block_values 

	visual_game_part = ""

	if b == None:

		block_values[a] = "X "
		
	elif b == None and a == None:

		block_values = block_values

	else:

		block_values[b] = "O "
		
	for x in range(1,10):

		visual_game_part += f"{block_values[x]}\n" if x!=0 and x%3==0 else  f"{block_values[x]}"
		
	return print(visual_game_part, sep='/n')

    
    
def combinator(a,n):

	def factorial(n):

		if n == 0:

			result = 1

		else:

			a = list(range(1,n+1))
			result = 1
			
			for x in a:

				result *= x
			
		return result

	results = []
	tester = []
	
	combinezon  = ((factorial(len(a)))/((factorial(n))*(factorial(len(a)-n))))
	
	while len(results) != combinezon:

		for x in range(n):

			sample =  r.choice(a)

			if sample in tester:

				continue

			else:

				tester.append(sample)
				
		while len(tester) != n:

			sample = r.choice(a)
			
			if sample not in tester:

				tester.append(sample)

			else:

				continue
				
				
		tester = sorted(tester)
		
		
		if tester not in results:
			
			results.append(tester)
			
			
			
		tester = []
		
		
	return results
        

def drawn_checker():
	if len(available_blocks) == 0:
		print("Drawn!")
		return True
	else:
		return False
		

def game_winner_checker(user):

	global user1_blocks, user2_blocks, combinations
	
	if user == 1:

		user = user1_blocks
	else:

		user = user2_blocks
		
	if len(user) < 3:

		return False
		
	else:
		sample =  combinator(user,3)
		
		
	for x in sample:

		if x in combinations:

			return True

	return False
        


def game():

	if drawn_checker():
		return False


	global user1_blocks, user2_blocks
	user_1 = user_inputs_1()
	user1_blocks.append(user_1)
	
	visual(a = user_1)

	if game_winner_checker(1):

		print("\n\n\nGame Ended! User 1 WON!!!\n\n")

		return False

		
	user_2 = user_inputs_2()
	user2_blocks.append(user_2)
	visual(b = user_2)

	if game_winner_checker(2):

		print('\n\n\n\nGame Ended! User 2 WON!!!')

		return False
	
			
	return True


def game_controller():

	global block_values, cleared_blocks, available_blocks1,winner_boolean
	available_blocks = [1,2,3,4,5,6,7,8,9]
	
	block_values = {
        1 : "_ ",
        2 : "_ ",
        3 : "_ ",
        4 : "_ ",
        5 : "_ ",
        6 : "_ ",
        7 : "_ ",
        8 : "_ ",
        9 : "_ "
    }
		
		
	visual()
	while game() == True:
		
		game()
		

			
			
	return "Game Ended!"
    

game_controller()