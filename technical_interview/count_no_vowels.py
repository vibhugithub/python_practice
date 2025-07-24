'''
Count the number of vowels in a given string.
For example, given the input "Artifical intelligence", the output should be 8.
'''
def count_vowels(string):
    vowel='aeiou'
    count=0
    for i in string:
        if i.lower() in vowel:
            count+=1
    print(count)
            
    
count_vowels("Artifical intelligence")