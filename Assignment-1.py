#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ASSIGNMENT_1


# In[5]:


#1. In the below elements which of them are values or an expression? eg:- values can be
#integer or string and expressions will be mathematical operators.

* - expression
'hello'- String
-87.8 - int
(-, expression)
+  - expression
6  -  int


# In[ ]:


# 2. What is the difference between string and variable?

variable  is  to store a value in a memory location and to manipulate it if needed.

String consists of group of characterstics and it is written in in single or double quotes.


# In[ ]:


#3. Describe three different data types.

1. List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.
 Items separated by commas are enclosed within brackets [ ].

2. Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
It is defined within parentheses () where items are separated by commas.

3. String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings.


# In[ ]:


#4. What is an expression made up of? What do all expressions do?

An expression is a combination of values, variables, operators, and calls to functions.
Expressions need to be evaluated. If you ask Python to print an expression, the interpreter evaluates the expression and displays the result.


# In[ ]:


#5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
A statement is an instruction that the Python interpreter can execute.There are different types of statements like for while if .

An expression is a combination of values, variables, operators, and calls to functions.


# In[6]:


# 6. After running the following code, what does the variable bacon contain?
bacoon =22
bacoon+1


# In[7]:


# 7. What should the values of the following two terms be?
'spam' + 'spamspam'


# In[8]:


'spam'*3


# In[ ]:


# 8. Why is eggs a valid variable name while 100 is invalid?
Because variable names cannot begin with a number.


# In[ ]:


# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

str()
int()
float()


# In[ ]:


# 10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
This expression causes an error because in this line 'I have eaten' and 'burritos' are strings, while 99 is treated as integer. In order to fix the error and print 'I have eaten 99 burritos.', 99 needs to be in quotes ''  to treat it as a string.

