 def countPrimeNumbers(numbers):
    count = 0
    for elements in numbers:
        if(elements == 0 or elements == 1):
            continue
        else:
            for i in range(2,elements//2+1):
                if(elements % i == 0):
                    break
            else:
                count = count +1
    return count

if __name__ == '__main__':
    numbers=[]
    count=int(input())
    for i in range(count):
        numbers.append(int(input()))
    print(countPrimeNumbers(numbers))
