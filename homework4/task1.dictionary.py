information_string = ' name=Amanda=sssss&age=32&&salary=1500&currency=euro '

information_string = information_string.replace(' ','').replace('=sssss','').replace('&&', '&')

final_dictionary = {}

for element in information_string.split('&'):
    pair = element.split('=')
    key = pair[0]
    value = pair[1]
    final_dictionary[key] = value

print(final_dictionary)
