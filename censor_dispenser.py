import re

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# 1- censor string in text
# I need to split string, loop through
# def censor(text, word):
#    print(text.split(word))
#
# censor(email_two, "learning algorithms")

# the idea is to iterate through CENSOR and if INDEX == " " then CENSORed_ITEM will become " ", otherwise will become "X"
# under for loop I will replace CENSOR by censored_item

def censor_one(input_text, censor):
    censored_item = "" # create empty string before the for loop it will be referenced
    for index in range(0, len(censor)): # need to iterate through each character
       if censor[index] == " ": # if character in censor is equal to " "
           censored_item += " "
       else:
           censored_item += "X"
    input_text = input_text.replace(censor, censored_item) # need to re-define the text replacing with censored_item and retur
    return input_text

print(censor_one(email_one, "learning algorithm"))


# 2- censor words in text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

# iterate through the list items and indexes and check with string


def censor_two(input_text, list):
    for word in list:
        censored_item = "" # need to create to loops, one for the list and the other for the characters of each of the items
        for index in range(0, len(word)): #
           if word[index] == " ":
               censored_item += " "
           else:
               censored_item += "X"
        input_text = input_text.replace(word, censored_item)
    return input_text

print(censor_two(email_two, proprietary_terms))

# string = [text.lower().replace(word, "") for word in proprietary_terms]
# print(string)

# for word in proprietary_terms:
#     if word in text:
#         text.replace(word, "")
#    print(text)

# for word in proprietary_terms:
#     if word in email_two.lower():
#         email_two.replace(word, "")
# print(email_two)


# def terms(items):
#     email_two_split = email_two.split()
#     #print(email_two_split)
#     clean_text = [word for word in email_two_split if word.lower().strip("!") not in items] # strip needs to go on the word
#     print(clean_text)
#     final_text = " ".join(clean_text)
#     print(final_text)
#
# terms(proprietary_terms)

# 3
# ask is to censor a word if it occurs twice AND previous list
#

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


def censor_three(input_text, censored_list, negative_words): # parameters are: text, list and words.
  input_text_words = [] # need to know that will create a new string from a clean list
# first task to convert string into a clean list of words and appending into new empty list
  for x in input_text.split(" "): #creating an input_text list SPLItING by the space " ". cleaning up the existing string and splitting by spaces and new lines
    x1 = x.split("\n") # variable to split and remove the new lines
    for word in x1: # looping through each X1 word and appending to new list.
      input_text_words.append(word)  # now I have a clean list of each word in input_text_words. once cleaned, join into new list
# second to replace each character if word in negative list by "X"
  for i in range(0,len(input_text_words)): #looping through each word on the list
    if (input_text_words[i] in censored_list) == True: # if word (using [i] to reference that index) in censored_list is TRUE
      word_clean = input_text_words[i] # 1. I'm going to create a variable that host that negative word
      censored_word = "" # 2. create an empty string to create space for that character replacement and loop thru to change it
      for x in range(0,len(word_clean)): # for loop of word_clean if word in censored list is TRUE
        censored_word = censored_word + "X" # word_clean characters will be replaced by "X"
      input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
# input_text_word where word_clean (negative) exist will be replaced by censored_word (the one with XXXX)
# second task we look at negative words and censor the the repeat ones

    count = 0
    for i in range(0,len(input_text_words)): # looping through each word
      if (input_text_words[i] in negative_words) == True: #if word in negative words is TRUE
        count += 1 # add 1 to count
        if count > 2: # if count is > than 2
          word_clean = input_text_words[i] # create variable where word_clean is negative word that I'll use in next FOR loop
#          for x in word_clean:
#           word_clean = word_clean.strip(x) # For loop to strip and create a new list of the word_clean characters
          censored_word = "" #create and empty string
          for x in range(0,len(word_clean)): #loop through each element of the word_clean
            censored_word = censored_word + "X" #replace that character with "X"
          input_text_words[i] = input_text_words[i].replace(word_clean, censored_word) #replace negative word IF twice by "X"
  return " ".join(input_text_words) #join everything with " "

print(censor_three(email_three, proprietary_terms, negative_words))


punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]

def censor_four(input_text, censored_list):
  input_text_words = []
  for x in input_text.split(" "):
    x1 = x.split("\n")
    for word in x1:
      input_text_words.append(word)
  for i in range(0,len(input_text_words)):
    checked_word = input_text_words[i].lower()
    for x in punctuation:
      checked_word = checked_word.strip(x) # ???
    if checked_word in censored_list:

      # Censoring the targeted word
      word_clean = input_text_words[i]
      censored_word = ""
      for x in punctuation:
        word_clean = word_clean.strip(x)
      for x in range(0,len(word_clean)):
        censored_word = censored_word + "X"
      input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)

      # Censoring the word before the targeted word
      word_before = input_text_words[i-1]
      for x in punctuation:
        word_before = word_before.strip(x)
      censored_word_before = ""
      for x in range(0,len(word_before)):
        censored_word_before = censored_word_before + "X"
      input_text_words[i-1] = input_text_words[i-1].replace(word_before, censored_word_before)

      # Censoring the word after the targeted word
      word_after = input_text_words[i+1]
      for x in punctuation:
        word_after = word_after.strip(x)
      censored_word_after = ""
      for x in range(0,len(word_after)):
        censored_word_after = censored_word_after + "X"
      input_text_words[i+1] = input_text_words[i+1].replace(word_after, censored_word_after)
  return " ".join(input_text_words)

censor_all = proprietary_terms + negative_words

print(censor_four(email_four, censor_all))

