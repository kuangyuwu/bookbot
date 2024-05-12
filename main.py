def main() -> None:
    book_path: str = "books/frankenstein.txt"
    text: str = get_book_text(book_path)
    num_words: int = get_num_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    letter_counts: dict[str, int] = count_letters(text)
    a_to_z: list[str] = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    a_to_z.sort(key=lambda c: letter_counts[c], reverse=True)
    for c in a_to_z:
        print(f"The '{c}' character was found {letter_counts[c]} times")
    print("--- End report ---")

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def get_num_words(text: str) -> int:
    words: list[str] = text.split()
    return len(words)

def count_letters(text: str) -> dict[str, int]:
    letter_counts: dict[str, int] = {chr(x): 0 for x in range(ord('a'), ord('z') + 1)}
    for c in text:
        if c.isalpha():
            letter_counts[c.lower()] += 1
    return letter_counts


main()