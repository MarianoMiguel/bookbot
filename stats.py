def words_in_document(document):
    return len(document.split())

def get_character_counts(document):
    dictionary = {}
    for character in document:
        if character.lower() in dictionary:
            dictionary[character.lower()] += 1
        else:
            dictionary[character.lower()] = 1

    return dictionary

def sort_on(items):
    return items["num"]
    
def get_sorted_character_counts(document):
    dictionary = get_character_counts(document)
    listing = []

    for key in dictionary:
        if key.isalpha():
            print("is alpha", key)
            listing.append({ "char": key, "num": dictionary[key] })
    
    listing.sort(reverse=True, key=sort_on)
    return listing