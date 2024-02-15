def sort_on(dict):
    return dict["count"]

book_location = "./books/frankenstein.txt"

with open(book_location) as f:
    book = f.read()
    wordcount = len(book.split())
    lettercount = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        lettercount[letter] = 0

    for letter in book.lower():
        if letter in lettercount:
            lettercount[letter] += 1

    report = []
    for letter in lettercount:
        report += [{"letter": letter, "count": lettercount[letter]}]
    report.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_location} ---")
    print(f"{wordcount} words found in the document")
    print("")
    for entry in report:
        print(f"The {entry["letter"]} character was found {entry["count"]} times")
    print("--- End report ---")
