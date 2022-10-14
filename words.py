def print_upper_words(words):
    """ Prints uppercased words on a seperate line
    
    print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'])
    should print "HELLO", "HEY", "YO", and "YES"
    """
    for word in words:
        print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])


def print_upper_words_with_e(words):
    """ Prints uppercased words on a seperate line that start with a lowercased or uppercased "e"
    
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

print_upper_words_with_e(['eagle','emmanuel', 'East', "sam"])

def print_upper_words_start(words, must_start_with):
    """Prints uppercased words on a seperate line that start specific letter """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words_start(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})