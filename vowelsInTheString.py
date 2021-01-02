 def countVowels(inp):
    count = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for character in inp:
        if character in vowels:
            count = count + 1
    return count

if __name__=='__main__':
    inp = input()
    output = countVowels(inp)
    print(output) 
