def no_vowels(string):
    newstring = string
    vowels = 'aeiou'
    for vowel in vowels:
        if vowel in string:
            newstring = newstring.replace(vowel, '')

    return newstring

if __name__=='__main__':
    my_string = "this is an example"
    print(no_vowels(my_string))
    my_string = "abcdefghijklmnopqrstuvwxyz"
    print(no_vowels(my_string))