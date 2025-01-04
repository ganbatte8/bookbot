def count_chars(text):
    counts = {}
    for c in text:
        lc = c.lower()
        if lc in counts:
            counts[lc] += 1
        else:
            counts[lc] = 1
    return counts

def get_book_text(filepath):
    text = None
    with open(filepath) as f:
        text = f.read()  # entire text
    return text

def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    book_words = book_text.split()
    word_count = len(book_words)
    char_counts = count_chars(book_text)

    sorted_char_counts = dict(sorted(char_counts.items(), key=(lambda item:item[1]), reverse=True))

    print(f"word_count:{word_count}")

    for k,v in sorted_char_counts.items():
        if 'a' <= k[0] <= 'z':
            print(f"{k}:{v}")

main()

