## Question 18:
#### **Write a program to verify whether a candidate is eligible to appear for an exam or not. The minimum and maximum age of person appearing for the exam is 21 and 35, respectively.**

***
Some Reference about if-else statement:
### if-else Statement

If-Else statements in Python are part of conditional statements, which decide the control of code. Conditional statements in Python languages decide the direction(Control Flow) of the flow of program execution.

Python control flow statements are as follows:

1) The if statement
2) The if-else statement
3) The nested-if statement
4) The if-elif-else ladder

**Python if statement**<br>
The if statement is the most simple decision-making statement. It is used to decide whether a certain statement or block of statements will be executed or not.<br>
#### _Syntax:_
```
if condition:
   # Statements to execute if
   # condition is true
```

**Python If-Else Statement**<br>
The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition is false it won’t. But if we want to do something else if the condition is false, we can use the else statement with the if statement to execute a block of code when the if condition is false. 
#### _Syntax:_
```
if (condition):
    # Executes this block if
    # condition is true
else:
    # Executes this block if
    # condition is false
```

**Nested-If Statement in Python**<br>
A nested if is an if statement that is the target of another if statement. Nested if statements mean an if statement inside another if statement.
Also, Python allows us to nest if statements within if statements. i.e., we can place an if statement inside another if statement.
#### _Syntax:_
```
if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here
```

**Python if-elif-else Ladder**<br>
Here, a user can decide among multiple options. The if statements are executed from the top down.
As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the ladder is bypassed. If none of the conditions is true, then the final “else” statement will be executed.
#### _Syntax:_
```
if (condition):
    statement
elif (condition):
    statement
.
.
else:
    statement
```
