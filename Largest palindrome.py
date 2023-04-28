def is_palindrome(n):
    return str(n) == str(n)[::-1] #checks if the num is a palindrome

max_palindrome = 0

for n1 in range(100, 1000):
    for n2 in range(100, 1000): 
        r = n1 * n2           #for each num with 3-digits in the first loop, he'll multiply by another the 3-digits numbers
        if is_palindrome(r) and r > max_palindrome:
            max_palindrome = r
            print(n1, n2)

print("The largest palindrome made from the product of two three-digit numbers is:", max_palindrome)
