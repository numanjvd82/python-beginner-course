# Mad Libs Game

print("Welcome to Mad Libs!")


def madLibs():
    adjective = input('Please enter an adjective: ')
    noun = input('Please enter a noun:')
    verb = input('Please enter a verb:')

    print('The ' + adjective + ' ' + noun + ' ' + verb + 's.')
    print('Roses are ' + adjective + '.')
    print(noun + 's are ')
    print('I love ' + noun + '.')


madLibs()
