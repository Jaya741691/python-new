# Question 1: The String Manipulator
# Write a function string_analysis(text) that takes a string as input.
# The function should count the number of uppercase letters, lowercase letters, and
# digits in the string. Return these values as a dictionary.


def string_analyst(text):
    final={"uppercase":0,"lowercase":0,"digits":0}
    for char in text:
        if char.isupper():
            final["uppercase"]+=1
        elif char.islower():
            final["lowercase"]+=1
        elif char.isdigit():
            final["digits"] += 1
    return final


k=string_analyst("JayaSimha1322")
print(k)