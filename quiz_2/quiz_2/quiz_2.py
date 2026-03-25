
# problem 1
letter = input("enter a letter: ")
count = 0
for i in "elephant":
    if i == letter:
        count = count + 1
print(count)

# 1. save the number three in a varable 2. ask the user for a number 2. check if the number is three 3. if wrong guess agian 4. if they get it wrong five times they lose  5. less then five they win
# problem 2
count = 0 
number = 3
while count < 5:
    guess = int(input("enter a number: "))
    if guess == number:
        print("you win!")
        break
    else:
        print("try agian")
    count = count + 1


