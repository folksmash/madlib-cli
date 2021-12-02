import re

SPEECH_TYPES = 'Adjective|Noun|Verb|Adverb'

welcome_message = """Welcome to Jordans mad libs. Follow along with the prompts to complete your story!"""

instruction = """To play please provide words in the following order an adjective, an adjective, and a noun"""

#takes in a path to text file and returns stripped string of the file's contents
def read_template(r):
    try:
        with open(r, 'r') as file:
            content = file.read()
        return content
    except:
        raise FileNotFoundError

#takes in a template string and returns a string with language parts removed and a separate list of those language parts. 
def parse(contents):
    required_words = re.findall(SPEECH_TYPES, contents)
    stripped_template = re.sub(SPEECH_TYPES, '', contents)
    return stripped_template, tuple(required_words)


#takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.
def merge(text,word):
    merged_words = text.format(*word)
    return merged_words


# def play_game():
#     game_start = input(">")
#     if game_start == "yes":
#         print('great')
# print(welcome_message, instruction)

# # call the functions

# play_game()