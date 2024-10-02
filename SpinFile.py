#Assignment 4 Martin Cheng 1 person https://github.com/UtahSoC-Sullivan/A4-MCheng
import string
from Spinner import Spinner


def clean_text(text):
    # Convert the text to lowercase and remove punctuation
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))


def main():
    # Read the essay text from a file
    with open('essay.txt', 'r') as essay_file:
        original_text = clean_text(essay_file.read())

    print("Original:", original_text)

    # Initialize the Spinner with the synonym file
    spinner = Spinner('synonyms-simplified.txt')

    # Spin the text three times and print the results
    for i in range(1, 4):
        changed_text = spinner.spin_text(original_text)
        print(f"Option {i}:", changed_text)


if __name__ == "__main__":
    main()
