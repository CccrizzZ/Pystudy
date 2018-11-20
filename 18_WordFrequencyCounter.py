import requests
from bs4 import BeautifulSoup
import operator

# Main function
def start(url):
    word_list = []
    # Connect to the url
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    # Traverse HTML code
    for post_text in soup.findAll("a", {"class": "result-title hdrlnk"}):
        # Pull out the text
        content = post_text.string
        # Convert all word to lower case and split the word
        words = content.lower().split()
        for each_word in words:
            # Append all word to the list
            word_list.append(each_word)

    clean_up_list(word_list)


# Clean up function
def clean_up_list(word_list):
    clean_word_list = []
    # Traverse word_list
    for word in word_list:
        symbols = "!@#$%^&*()_+\{}:<>?-=[];,./'"
        # Traverse symbols
        for i in range(0, len(symbols)):
            # replace(a, b) replace a with b
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


# Dictionary function
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        # If the word exist in the Dictionary then add 1
        # If the word don't exist then add the word to the dictionary and set the count to 1
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # Sorted(sorting target, sorting method)
    # Operator deal with python's built in data
    # itemgetter(x) go through the dictionary, pass in 0 sort by key, pass in 1 sort by value
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print (key,value)





start("https://losangeles.craigslist.org/search/sss?query=cl550&sort=rel")
