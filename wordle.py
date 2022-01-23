from random_word import RandomWords
import enchant

class Wordle:

	def main(self): # splash screen and primary logic
		secret = self.generate()
		guess_count = 0

		print('    _    _               _ _           ') # obnoxious ASCII art because why not
		print('   | |  | |             | | |          ')
		print('   | |  | | ___  _ __ __| | | ___      ')
		print('   | |/\| |/ _ \| \'__/ _` | |/ _ \    ')
		print('   \  /\  / (_) | | | (_| | |  __/     ')
		print('    \/  \/ \___/|_|  \__,_|_|\___|     ')                            
		print('                                       ')
		print(' ______               _   _            ')
		print(' | ___ \             | | (_)           ')
		print(' | |_/ / __ __ _  ___| |_ _  ___ ___   ')
		print(' |  __/ \'__/ _` |/ __| __| |/ __/ _ \ ')
		print(' | |  | | | (_| | (__| |_| | (_|  __/_ ')
		print(' \_|  |_|  \__,_|\___|\__|_|\___\___(_)')
		print()  
		print('    WELCOME TO WORDLE PRACTICE!')
		print('- The rules are simple. You must guess 5 letter words to discover letters in the secret word.')
		print('- You have unlimited guesses. You will win the game once you guess the complete secret word.')
		print('- There are no repeating letters in the secret word. All 5 letters are unique.')
		print('- If you wish to give up and see the secret word, simply enter \"quit\" as your guess.')
		print('- The letters in your guess will be verified with the following marks: ')
		print('    x --> incorrect, this letter is not in the secret word')
		print('    * --> correct letter but in the wrong position')
		print('    ! --> correct letter and correct position')
		print()

		while 1: 
			guess = self.prompt()
			if guess == 'quit':
				print('Looks like you decided to quit after ' + str(guess_count) + ' guesses. The secret word was: ' + secret + '\n')
				break
			guess_count += 1
			if self.verify(guess, secret) == True:
				print('Total number of guesses was ' + str(guess_count) + '\n')
				break


	def generate(self): # generates a random 5-letter word
		words  = RandomWords()

		while 1:
			secret = words.get_random_word(hasDictionaryDef="true", minCorpusCount=10000, minLength=5, maxLength=5)
			if secret:
				secret = secret.upper()
				break

		for char in secret:
			if len(secret) < 5 or len(secret) != len(set(secret)) or char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				secret = self.generate() # recursive call until secret word is valid format

		return secret
	

	def prompt(self): # captures and validates user input for guessing words
		dictionary = enchant.Dict('en_US')

		while 1:
			guess = input('Enter your guess: ')
			print()
			if guess == 'quit':
				return guess
			elif dictionary.check('guess') and len(guess) == 5:
				guess = guess.upper()
				return guess
			else:
				print('Your guess must be a 5-letter English word! \n')


	def verify(self, guess, secret): # checks if guess is partially or completely correct
		guess_split = [guess[0], ' ', guess[1], ' ', guess[2], ' ', guess[3], ' ', guess[4]]
		status = ['x ', 'x ', 'x ', 'x ', 'x '] 

		# verify each letter in the guess
		for i in range(5):
			if guess[i] == secret[i]:
				status[i] = '! '
			elif guess[i] in secret:
				status[i] = '* '

		# print the guess with spaces
		for i in range(len(guess_split)):
			print(guess_split[i],end='')
			if i == len(guess_split) - 1:
				print()

		# print the status with spaces 
		for i in range(len(status)):
			print(status[i],end='')
			if i == len(status) - 1:
				print('\n')

		# check if guess is 100% correct
		if guess == secret:
			print('You\'ve won! The secret word is ' + secret + '\n')
			return True
		else:
			return False


# driver code:
wordle = Wordle()
wordle.main()
