def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_words(text)
    letter_frequency = dict(sorted(letter_records(text).items(), key=lambda item: item[1], reverse=True))
    
#     print(text)
#     print(total_words)
#     print(letter_records(text))

    for record in letter_frequency:
        if record.isalpha():
            print(f"The '{record}' was found {letter_frequency[record]} times")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text_string):
    words = text_string.split()
    
    return len(words)


def letter_records(text_string):
    lowered_text = text_string.lower()
    record = {}
    
    for char in lowered_text:
        if char in record:
            record[char] += 1
        else:
            record[char] = 1
            
    return record


main()
