# String Concatenation

# To peform String Concatenation by using + operator
str1 = "Hello"
str2 = " World"
result = str1+str2
print(result)
# To peform String Concatenation by using += operator
result = "Hello"
result += " World"
print(result)
# To perform String concatenation by using join method
strings = ["Hello"," World"]
result.join(strings)
print(result)
# To peform String concatenation using f-string.
str1 = "Hello"
str2 = " World"
result = f"{str1}{str2}"
print(result)
# To peform String concatenation using format strings
str1 = "Hello"
str2 = " World"
result = "{}{}".format(str1,str2)
print(result)
# To peform String concatenation using % operator
str1 = "Hello"
str2 = " World"
result = "%s%s" % (str1, str2)
print(result)
# To peform String concatenation by using comma(,)
str1 = "Hello"
str2 = "World"
print(str1,str2)
