kahani = ''
while True:
    line = input('>>>')
    if len(kahani) == 0 and len(line) == 0:
        print('Please enter a story')
        continue        
    if not line:
        break
    kahani += line + '\n'
    
print("The story is: ")
print(kahani)
print('⭐⭐⭐⭐⭐')