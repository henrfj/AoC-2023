""""
Collect stars to find the snow-problem.

Being launched in a Trebuchet: Fix calibration document


"""


# Open the file in read mode
file = open('input.txt', 'r')

# Loop through each line in the file
s = 0
for line in file:
    # Initialize the pointers
    first = None
    last = None
    for l in line:
        try:
            if first==None:
                first = int(l)
            else:
                last = int(l)
        except ValueError:
            pass
        
    if last==None:
        last = first

    a = int(str(first)+str(last))
    print(a)
    s += a
    
print("final sum", s)
# Close the file
file.close()