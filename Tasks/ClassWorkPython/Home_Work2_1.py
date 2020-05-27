# 1
def findText(some_text,find_text):
    result = some_text.count(find_text)
    print(result)

text = input("Enter text: ")
findtext = input("Some text what u want to find in the text: ")
findText(text,findtext)

# 2
text = input("Enter some text > ")    
upperText = text.upper()
print(upperText)      

# 3

text = input("Enter some text > ")    
replaceText = text.replace("i","&")
print(replaceText)      