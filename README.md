# Simplicity Wordlist

A simple script to help you create a wordlist

### Usage
python3 simplicity_word.py -w word1,word2 -s <symbol> -c <company> -a <existing_wordlist>

### Options
```
usage: simplicity_word.py [-h] [-w WORDS] [-s SYMBOL] [-r RANGE] [-c COMPANY] [-a APPEND]

options:
  -h, --help            show this help message and exit
  -w WORDS, --words WORDS
                        Specify password words (without spaces) Ex: word1,word2
  -s SYMBOL, --symbol SYMBOL
                        Specify password symbol (@#$!*&)
  -r RANGE, --range RANGE
                        specify the range of numbers to use in the password. Format: 0-0 (default
                        0-10)
  -c COMPANY, --company COMPANY
                        Specify the company. Output: user123@company
  -a APPEND, --append APPEND
                        Specify existing wordlist. Ex: wordlist.txt
```

### Basic Usage

Simple wordlist, without company name

```bash
python3 simplicity_word.py -w word1,word2 -s "@"
```


With company name

```bash
python3 simplicity_word.py -w word1,word2 -s "@" -c "redteamcompany"
```

updating an existing wordlist

```bash
python3 simplicity_word.py -w word1,word2 -s "@" -c "redteamcompany" -a "wordlist.txt"
```

specifying a range of numbers
```bash
python3 simplicity_word.py -w word1,word2 -s "@" -c "redteamcompany" -a "wordlist.txt" -r 0-10
```
---
If you have any questions, you can contact me!
I'm not a professional programmer, so ignore errors in the code if you have them! :smile:

*God bless*
