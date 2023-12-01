import sys, argparse

"""
By: Bielzao
"""

# Function to generate words without symbol
def genSimpleWords(words, wordlist, start_range, end_range):
	word_plus = words[0]
	used = 1

	for word in words:
		for i in range(start_range, end_range+1):
			wordlist.append(f"{word_plus + str(i)}")

		if used < len(words):
			word_plus += words[used] 

		used+=1


# function to generate words with symbol
def genSymbolWords(words, wordlist, sb, start_range, end_range):
	word_plus = words[0]
	used = 1

	for word in words:
		for i in range(start_range, end_range+1):
			wordlist.append(f"{word_plus + sb +str(i)}")

		if used < len(words):
			word_plus += words[used] 

		used+=1


# function to generate company standard passwords.
def genStandardPass(words, wordlist, sb, company, start_range, end_range):
	word_plus = words[0]
	used = 1

	for word in words:
		for i in range(start_range,end_range+1):
			wordlist.append(f"{word_plus + str(i) + sb + company}")

		if used < len(words):
			word_plus += words[used] 

		used+=1


# function to save the wordlist
def saveWordlist(wordlist):
	file = open('wordlist.txt', 'w')

	for w in wordlist:
		file.write(f"{w}\n")

	file.close()


# function to append a new wordlist to a existent one
def appendWordlist(wordlist, wordlist_file):
	file = open(wordlist_file, "a")

	for w in wordlist:
		file.write(f"{w}\n")

	file.close()


def main():
	wordlist = []

	parser = argparse.ArgumentParser()
	parser.add_argument("-w","--words", help="Specify password words (without spaces) Ex: word1,word2",)
	parser.add_argument("-s", "--symbol", help="Specify password symbol (@#$!*&)")
	parser.add_argument("-r", "--range", help="specify the range of numbers to use in the password.\
		Format: 0-0 (default 0-10)")
	parser.add_argument(
	    "-c", "--company", help="Specify the company. Output: user123@company")
	parser.add_argument("-a", "--append", help="Specify existing wordlist. Ex: wordlist.txt")

	args = parser.parse_args()

	if args.words:
		words = args.words.split(",")
		sb = args.symbol

		# checks if a range has been specified
		if args.range:
			number_range = args.range.split('-')
			start_range, end_range = number_range

			# prevents other data from being entered that is not a number
			try:
				start_range = int(start_range)
				end_range = int(end_range)

				if start_range > end_range:
					start_range,end_range = end_range, start_range
			except ValueError:
				print("[ERROR] Use only numbers")
		else:  # if no range was specified, enter the default
			start_range = 0
			end_range = 10

		genSimpleWords(words,wordlist, start_range, end_range)
		if args.symbol:
			genSymbolWords(words, wordlist, sb, start_range, end_range)
		
		if args.company:
			company = args.company
			genStandardPass(words,wordlist, sb, company, start_range, end_range)


		if args.append:
			wordlist_file = args.append
			appendWordlist(wordlist, wordlist_file)
			print("[+] Wordlist was updated.")

			return

		saveWordlist(wordlist)

		print("[+] Wordlist saved")


if __name__ == '__main__':
	main()