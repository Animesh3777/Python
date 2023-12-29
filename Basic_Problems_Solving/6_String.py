message = "Hello Hi"
print(message)
hey=message.replace('Hello',"Hey")
print(hey)
print(message)

name = "Animesh"
greet = "{},{} Welcome".format(message, name)
print(greet)

welcome = f'{message},{name} Welcome'
print(welcome)
person = {"name": "Animesh", "age": 25}
print(person)
intro = "My name is {}, and i am {} years old".format(person['name'], person['age'])
print(intro)

tag='h1'
text='This is a headline'
sentence = "<{0}>{1}</{0}>".format(tag,text)
print(sentence)
