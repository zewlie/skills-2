# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    # Split string into words and create an empty dictionary.
    words = input_string.split(' ')
    words_dict = {}

    # If word in words_dict, increment the value up by one;
    # if word not in words_dict, set the value to 1.
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    return words_dict


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    # Create a dictionary to work with, and a compiled list to return.
    weird_dict = {}
    compiled_list = []

    # Merge the two provided lists into one.
    list1.extend(list2)

    # Create a dictionary wherein each key's value is the full list of items.
    for item in list1:
        weird_dict[item] = list1

    # Remove the value corresponding to the key from each key's list of values.
    for key in weird_dict.keys():
        weird_dict[key].remove(key)

        # If any remaining value in the key's value list is equivalent to the
        # key, append it to compiled_list.
        for item in weird_dict[key][:]:
            if key == item:
                compiled_list.append(key)

    return compiled_list


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    # Create a dictionary that'll hold all the items in list1 as keys,
    # and a list of all items in list2 as values.
    # Create a second dictionary to hold keys from the first dictionary
    # that hold values equivalent to the keys themselves.
    item_dict = {}
    unique_dict = {}

    # Build the dictionaries.
    for item in list1:
        item_dict[item] = list2

        for sub_item in item_dict[item]:
            if item == sub_item:
                unique_dict[item] = None

    return unique_dict.keys()


    # list1.extend(list2)

    # for item in list1:
    #     if item_dict[item]:
    #         item_dict[item] += 1
    #     else:
    #         item_dict[item] = 1

    # for item in item_dict:
    #     if item_dict[item] >= 2:
    #         unique_list.append(item)



    return unique_list

    # FIX


def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    # Create separate lists for positive and negative numbers in input_list.
    pos_num = []
    neg_num = []

    # Create a dictionary to work in and a list for the pairs we'll return.
    comparison_dict = {}
    pairs_sum_zero = []

    # Put positive numbers from input_list into their own list, and
    # put negative numbers into another list. 
    # Include zero in both lists.
    for item in input_list:
        if item >= 0:
            pos_num.append(item)
        if item <= 0:
            neg_num.append(item)

    # Build comparison_dict: each positive number is a key; 
    # the value for each key is the list of negative numbers.
    for item in pos_num:
        comparison_dict[item] = neg_num

    # If the sum of a positive number (key) and an item in the list of
    # negative numbers (value) is 0, append a list containing both numbers to
    # the pairs_sum_zero list.
    # Reminder: 0 is treated both as a positive number and a negative number.
    for key in comparison_dict.keys():
        for item in comparison_dict[key]:
            if key + item == 0:
                pairs_sum_zero.append([key, item])

    return pairs_sum_zero


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # Create a dictionary and add each item in words as a key with a value of
    # None. Return the keys only.
    words_dict = {}

    for word in words:
        words_dict[word] = None

    return words_dict.keys()


def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    # Create an empty string for the encoded string;
    # Create a dictionary containing the cipher.
    new_text = ""
    cipher = {'e':'p', 'a':'d', 't':'o', 'i':'u'}

    # Check if each character in the phrase corresponds to a key in the cipher.
    # If it does, add the key value's character to new_text.
    # If it doesn't, add the character to new_text unaltered.
    for char in phrase:
        if char in cipher:
            new_text = new_text + cipher[char]
        else:
            new_text = new_text + char

    return new_text


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    # Create a dictionary to work in and a list to store tuples.
    word_lengths_dict = {}
    word_lengths_tuples = []

    # Build the dictionary; each word length in characters will be a key,
    # and each value will be a list of corresponding words.
    # Check if there's already a key for each word's length; if not, create
    # an empty list so that the words will append properly.
    for word in words:
        if len(word) not in word_lengths_dict:
            word_lengths_dict[len(word)] = []

        word_lengths_dict[len(word)].append(word)

    # Turn each dictionary item into a tuple.
    # Append each tuple to the word_lengths_tuples list.
    for key in word_lengths_dict:
        word_lengths_tuples.append((key, word_lengths_dict[key]))

    return word_lengths_tuples


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    # Split phrase into a list of words
    words = phrase.split()

    # Create an empty string for new text and build the cipher dictionary.
    new_text = ""
    cipher = {"sir": "matey",
              "hotel": "fleabag inn",
              "student": "swabbie",
              "boy": "matey",
              "madam": "proud beauty",
              "professor": "foul blaggart",
              "restaurant": "galley",
              "your": "yer",
              "excuse": "arr",
              "students": "swabbies",
              "are": "be",
              "lawyer": "foul blaggart",
              "the": "th'",
              "restroom": "head",
              "my": "me",
              "hello": "avast",
              "is": "be",
              "man": "matey"
              }

    # Check if each word is in the cipher as a key;
    # if it is, append the corresponding value + a space to new_text.
    # If it isn't, append the unaltered word to new_text.
    for word in words:
        if word in cipher.keys():
            new_text = new_text + cipher[word] + " "
        else:
            new_text = new_text + word + " "

    # Strip out any blank space on either end of new_text.
    new_text = new_text.strip()

    return new_text

# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    no_spaces_text = ""
    most_common_letter = []
    letter_counts = {}

    # Create a list of words from input_string, splitting on spaces.
    words_list = input_string.split()

    # Strip commas and periods from each word and add it to no_spaces_text.
    for word in words_list:
        word = word.strip(",.")
        no_spaces_text = no_spaces_text + word

    # Build the letter_counts dictionary.
    # Go through each character in no_spaces_text;
    # if it's already in letter_counts as a key, increment its value up by 1.
    # If it's not already in letter_counts as a key, set its value to 1.
    for char in no_spaces_text:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    # Find the highest value for letter counts in the phrase.
    top_count = max(letter_counts.values())

    # Find the character(s) -- key(s) -- with the highest letter count.
    # Append each to the most_common_letter list.
    for key in letter_counts:
        if letter_counts[key] == top_count:
            most_common_letter.append(key)

    # Sort the most common letters alphabetically.
    most_common_letter.sort()

    return most_common_letter


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    # Create a dictionary to work in and a list to hold tuples.
    word_lengths_dict = {}
    tuples_list = []

    # Check if there's already a key for each word's length; if not, create
    # an empty list so that the words will append properly.
    for word in words:
        if len(word) not in word_lengths_dict:
            word_lengths_dict[len(word)] = []

        word_lengths_dict[len(word)].append(word)

    # Create tuples from key, value pairs.
    # Sort both the keys and items with the value lists.
    for key in word_lengths_dict:
        tuples_list.append(tuple(sorted((key, sorted(word_lengths_dict[key])))))

    return tuples_list


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
