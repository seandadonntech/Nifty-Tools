from requests import get

response = get('https://alvinwan.com/coding101/cipher.json')
mapping = response.json()

def cipher(original):
    text = ""
    for letter in original:
        if letter in mapping:
            new_letter = mapping[letter]
        else:
            new_letter = letter  # If the letter is not  in the mapping, keep it unchanged
        text = text + new_letter
    return text

text = input("text or secret: ")
result = cipher(text)
print(result)
