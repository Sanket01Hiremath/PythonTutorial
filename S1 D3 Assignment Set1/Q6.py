#Count 
def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count

# Example usage:
text = "Sanket"
vowels, consonants = count_vowels_and_consonants(text)
print("Number of vowels:", vowels)        # Output: 2
print("Number of consonants:", consonants)  # Output: 4
