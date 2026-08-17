from googletrans import Translator

#Initialising object
translator = Translator()

Text = input("Enter the text in English: ")

#translating from English to Tamil
result = translator.translate(
    Text,
    src='en',
    dest='ta'
)

#printing the translated text from object 'result'
print(result.text)
