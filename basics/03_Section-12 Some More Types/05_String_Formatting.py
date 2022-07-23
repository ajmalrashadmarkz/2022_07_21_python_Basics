'''
    String Formatting: string.format(value1, value2...)
                       "my numbers: {0}, {1}, {2}".format(li[2],li[1],li[0])


        insert the values inside the string's placeholder
            example-[values]: li =  [10,20,30,40]
        placeholder is defined using curly brackets: {}.
            example: "my numbers: {0}, {1}, {2}"
        format() method returns the formatted string.
            example: .format(li[2],li[1],li[0])
'''

#Example of String Formatting - Print the 30,20,10
li =  [10,20,30,40]
newstring = "my numbers: {0}, {1}, {2}".format(li[2],li[1],li[0])
print(newstring)