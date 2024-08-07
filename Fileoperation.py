names = "c:/Users/sahea/OneDrive/Desktop/names.txt"
output = "C:/Users/sahea/OneDrive/Desktop/Output.txt"

#Reading File and display
with open(names,'r') as file:
    text = file.read()
    wordCount = len(text.split())
    print(text)
    print("Word count:",wordCount) 

#Writing to file \n(is for a new line)
with open(output,'w') as file:
    line1 = file.write('Careers IT\n')
    line2 = file.write('System Devlopers\n')
    line3 = file.write('Assessor- Mr Masiya')
    file.close()