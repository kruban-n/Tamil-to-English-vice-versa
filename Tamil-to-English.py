from googletrans import Translator

# 1) Initialize
translator = Translator()

# 2) Translate Tamil → English
Text = input("Enter the text in English: ")
result = translator.translate(
    Text,
    src='en',
    dest='ta'
)

print(result.text)
