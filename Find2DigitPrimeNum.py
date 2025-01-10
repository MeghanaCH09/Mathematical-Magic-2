start = 10
end = 99

for num in range(start, end + 1):
    c = 0  
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            c += 1 
            break 
    
    if c == 0:
        print(num) 
