import pandas as pd

# TODO 1. Create a dictionary in this format:
df = pd.read_csv('nato_phonetic_alphabet.csv')
nato = {row.letter: row.code for (index, row) in df.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato_code():
    user_input = input("Type word: ").upper()
    try:
        reference = [nato[letter] for letter in user_input]
    except KeyError:
        print('Sorry, Only type letters')
        nato_code()
    else:
        print(reference)


nato_code()
