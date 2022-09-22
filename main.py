# fork this challenge to your own repl
#share this challenge with another person in the room.

#Day 3 Python Challenge

# The task is as follows: You are going to create a program that first asks the user to enter text. It can be any text, an entire article, a paragraph, a sentence, a poem, whatever you want. Then the program will ask the user to enter three random letters. From that moment on, our code is going to process that information and result in five different types of analysis:
inputed_text = input("Give us a text: ")

first=input("Give us a word: ")

second=input("Give us another word: ")

third=input("Give us a third word: ")


# 1. How many times each of those letters they have chosen appears. To achieve this, I advise you to store those letters in a list, and then use a method of strings that allows you to count how many times a substring appears within the string. One thing to keep in mind is that when searching for letters, there can be upper and lower case and this will affect the result. So, to make sure that absolutely all letters are counted, you should pass both the original text and the letters to be searched to lowercase.
text1 = inputed_text
text_lower = text1.lower()
list = text_lower.split()

first_word = list.count(first)
print(f'There are {first_word} similar words like your first chosen word')

second_word = list.count(second)
print(f'There are {second_word} similar words like your second chosen word')

third_word = list.count(third)
print(f'There are {third_word} similar words like your third chosen word')

# 2. How many words are in the whole text? To achieve this part, remember that there is a string method that allows us to transform it into a list. And then there is a function that allows us to find out the length of a list.
length = len(list)
print(f'There are over {length} words in the text')




# 3. What are the first and last letters of the text? Here, we will clearly use indexing.
first_letter = 
last_letter = list.pop()
print()
print(last_letter)
# 4. The system will show us how the text would look like if we inverted the order of the words.::-1 Is there any method that allows us to invert the order of a list? And another one that allows us to join these elements with spaces in between?

# 5. The system will tell us if the word “python” is inside the text. This part can be a bit complicated to imagine, but I'll give you a hint: you can use Booleans to make your enquiry and a dictionary to find ways to express your answer.
