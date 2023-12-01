import argparse

"""
By: Bielzao
"""


# Function to generate words without symbol
def genSimpleWords(words, wordlist):
    word_plus = words[0]
    used = 1

    for word in words:
        for i in range(0, 6):
            wordlist.append(f"{word_plus + str(i)}")

        if used < len(words):
            word_plus += words[used]

        used += 1


# function to generate words with symbol
def genSymbolWords(words, wordlist, sb):
    word_plus = words[0]
    used = 1

    for word in words:
        for i in range(0, 6):
            wordlist.append(f"{word_plus + sb +str(i)}")

        if used < len(words):
            word_plus += words[used]

        used += 1


# function to generate company standard passwords.
def genStandardPass(words, wordlist, sb, company):
    word_plus = words[0]
    used = 1

    for word in words:
        for i in range(0, 6):
            wordlist.append(f"{word_plus + str(i) + sb + company}")

        if used < len(words):
            word_plus += words[used]

        used += 1


# function to save the wordlist
def saveWordlist(wordlist):
    file = open("wordlist.txt", "w")

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
    parser.add_argument(
        "-w",
        "--words",
        help="Specify password words (without spaces) Ex: word1,word2",
    )
    parser.add_argument("-s", "--symbol", help="Specify password symbol (@#$!*&)")
    parser.add_argument("-c", "--company", help="Specify the company. Output: user123@company")
    parser.add_argument("-a", "--append", help="Specify existing wordlist. Ex: wordlist.txt")

    args = parser.parse_args()

    if args.words:
        words = args.words.split(",")
        sb = args.symbol

        genSimpleWords(words, wordlist)
        if args.symbol:
            genSymbolWords(words, wordlist, sb)

        if args.company:
            company = args.company
            genStandardPass(words, wordlist, sb, company)

        if args.append:
            wordlist_file = args.append
            appendWordlist(wordlist, wordlist_file)
            print("[+] Wordlist was updated.")

            return

        saveWordlist(wordlist)

        print("[+] Wordlist saved")


if __name__ == "__main__":
    main()
