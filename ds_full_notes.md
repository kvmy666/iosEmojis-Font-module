
# Chapter 1

--- Page 1 ---
Data Structures and 
Algorithms
Applied College

--- Page 2 ---
Table of contents
Course Description
Python for data: 
Understanding data 
structures and 
algorithms
Variables and 
expressions
Flow Control and 
iterations
Data Types and Objects
Classes and Object 
Programming
2

--- Page 3 ---
Course Description
qThis
course
deals
with
the
fundamentals
of
data
structures and algorithms. It includes the following topics:
Python objects, types, and expressions, Python data
types and structures, principles of algorithm design, lists
and pointer structures, stacks and queues, trees, hashing
and symbol tables, graphs, searching, and sorting.
3

--- Page 4 ---
Required Textbook
§ Basant Agarwal, Benjamin Baka. Hands-On 
Data Structures and Algorithms with Python: 
Write complex and powerful code using the 
latest features of Python 3.7. Packt Publishing. 
2nd Ed., 2018.
§ GitHub - PacktPublishing/Hands-On-Data-Structures-
and-Algorithms-with-Python-Second-Edition: Hands-
On Data Structures and Algorithms with Python 
Second Edition, published by Packt
4

--- Page 5 ---
Chapter 1
(Python Objects, Types, 
and Expressions)
Applied College

--- Page 6 ---
Chapter Goals
qObtaining a general working knowledge of data structures and 
algorithms
qUnderstanding core data types and their functions 
qExploring the object-oriented aspects of Python programming 
language
6

--- Page 7 ---
Data Structures and 
Algorithms with Python
In this section: Expressions, Variable Scopes, Data Types.

--- Page 8 ---
qData is a collection of facts and figures. It is also defined as a set of
values in a particular format that refers to a single set of item values.
qData can be managed in different ways, such as a logical or 
mathematical model for a particular organization of data, also called a 
data structure.
qData structure is a specific way of storing and organizing data in the
computer's memory so that these data can be easily retrieved and
efficiently used.
8

--- Page 9 ---
qA data structure is said to be linear if its elements combine to form any
specific order.
§ Arrays
§ Queues
§ Stacks
§ Linked lists
qNon-linear data structures represent data with a hierarchical relationship 
between different elements.
§ Graphs
§ Family of trees and
§ Table of contents
9

--- Page 10 ---
§ Data structures and algorithms are 
two of the core elements of a large 
and complex software project.
§ An algorithm processes and 
produces data. It can be defined as 
a finite set of logic or instructions, 
written in order to accomplish a 
certain predefined task.
§ It can be represented either as an 
informal description using a 
Flowchart or Pseudocode.
10

--- Page 11 ---
qPython is an interpreted programming language, and statements are
executed line by line.
qFor Python, the source code is stored in a file with a .py file extension.
qPython has efficient high-level data structures and an effective object-
oriented programming language.
qPython
is
used
for
web
development
(server-side),
software
development, mathematics, system scripting.
11

--- Page 12 ---
Variables and Expressions
In this section: Expressions, Variable Scopes, Data Types.

--- Page 13 ---
qVariables are labels that are attached to the objects.
qVariables are not objects nor containers for objects; they only act as a
pointer or a reference to the object.
qExample: a variable a points to a list object. A variable b points to this
same list object. When we append an element (8) to this list object, this
change is reflected in both a and b.
13

--- Page 14 ---
qIn python, it is not required to first declare the datatype for the
variables.
qVariables point to an object that can change their type depending on
the kind of values assigned to them.
qExample: the type of a is changed from int to float, depending upon the
value stored in the variable.
14

--- Page 15 ---
qThe variables that are referenced inside a function are 
global implicitly
qWhenever a function executes, a local environment 
(namespace) is created. 
qThis local namespace contains all the variables and 
parameter names that are assigned by the functions. 
qWhenever a function is called, 
1. Python Interpreter first looks into the local namespace 
that is the function itself
2. if no match is found, then it looks at the global 
namespace. 
3. If the name is still not found, then it searches in the built-
in namespace. 
4. If it is not found, then the interpreter would raise a 
NameError exception.
15
Example 1:
Example 2:

--- Page 16 ---
qIf a is assigned a value anywhere inside the function's body, it is assumed to be 
a local variable unless explicitly declared as global. 
qIt can be resolved by accessing the outer scope variable by declaring it as 
global:
16

--- Page 17 ---
Flow Control and iteration
In this section: Execution flow, conditional statements, iterative control

--- Page 18 ---
qPython programs consist of a sequence of statements.
qAll the instructions/statements in the program are executed
in sequence in general.
qthere are two main ways of controlling the flow of program
execution
§ conditional statements
§ loops.
18

--- Page 19 ---
qThe if...else and elif statements control the conditional execution of 
statements. 
qThe general format is a series of if and elif statements followed by a 
final else statement: 
19

--- Page 20 ---
qTwo ways of constructing looping, such as the while and for loop 
statements. 
o A while loop repeats executing statements until a Boolean condition is true. 
o A for loop provides a way of repeating the execution into the loop through a series 
of elements.
20
Example 2: iterating for all the items over the list
Example 1:

--- Page 21 ---
Data Types and Objects
In this section: Strings, Lists, objects, and manipulation method

--- Page 22 ---
qPython contains various built-in data types.
§ Numeric types (int, float, complex, bool), 
§ Sequence types (str, list, tuple, range), 
§ Mapping type (dict), and 
§ Set types.
qIt is also possible to create user-defined objects, such as functions or 
classes. 
qAll data types in Python are objects; each object has a type, a value, 
and an identity.
qThe identity of an object acts as a pointer to the object's location in 
memory.
§ Once an instance of an object is created, its identity and type cannot be changed.
§ Example: greet= "hello world" 
22

--- Page 23 ---
qStrings are immutable sequence objects, with each character representing
an element in the sequence.
qStrings, like all sequence types, support indexing and slicing.
oWe can retrieve any character from a string by using its index s[i].
oWe can retrieve a slice of a string by using s[i:j], where i and j are the start
and end points of the slice.
23

--- Page 24 ---
qWe can use any expression, variable, or operator as an index as long
as the value is an integer:
qExample 1: traversing through a string with a loop.
24
Example 2: Since strings are immutable,
inserting values is performed by creating a
new string.

--- Page 25 ---
25

--- Page 26 ---
qLists can store any number of different data types.
qList can contain nested structures; that is, list can contain other lists.
26
Example: list items contain three other lists:
Example: raising the price of 
flour by 20 percent

--- Page 27 ---
qWe can create a list from expressions using a very common and
intuitive method; that is, list comprehensions.
qIt allows to create a list through an expression directly into the list.
27
Example: the following code creates a list of words and their letter 
count:

--- Page 28 ---
28

--- Page 29 ---
Functions
In this section: User-defined functions, higher-order functions, recursive functions.

--- Page 30 ---
qA function is a block of code which only runs when it is called.
qA function can return data as a result.
qIn Python a function is defined using the def keyword
qTo call a function, use the function name followed by parenthesis.
30

--- Page 31 ---
qSince user-defined functions are objects, they can be included in other
objects, such as lists.
qFunctions can also be used as arguments for other functions.
31

--- Page 32 ---
qFunctions
that
take
other
functions as arguments, or that
return
functions,
are
called
higher-order functions.
qPython 3 contains two built-in
higher order functions: filter() and
map(), which return an iterator.
qThe map() and filter() functions
transform
each
item
into
an
iterable object.
32

--- Page 33 ---
qExample 1: len function is
passed as the key to the
sort function. This way, we
can sort a list of words by
length.
qExample
2:
for
case-
insensitive
sorting.
The
list.sort() method sorts the
existing instance of a list
without copying it.
33

--- Page 34 ---
qRecursion occurs when a function takes one or more calls to itself during
execution.
qDifference between recursion and loop
§ loops execute statements repeatedly through a Boolean condition or through a 
series of elements, 
§ recursion repeatedly calls a function. 
§ iteration loops through a sequence of operations, whereas recursion repeatedly 
calls a function. 
34

--- Page 35 ---
qBase case: To stop a recursive function turning into an infinite loop, we need 
at least one argument that tests for a terminating case to end the recursion.
qRecursive functions are also useful for manipulating recursive data
structures such as linked lists and trees.
35
Base case: (low <= high)

--- Page 36 ---
Classes and Object 
Programming
In this section: Classes and instances, methods, encapsulation, inheritance.

--- Page 37 ---
qClasses are a way to create new kinds of objects and they are central to
object-oriented programming.
qA class defines a set of attributes that are shared across instances of that
class.
qTypically, classes are sets of functions, variables, and properties.
qTo create an instance, a variable must be assigned to a class.
qThe functions defined inside a class are called instance methods.
37

--- Page 38 ---
qIn this example below, an employee has three attributes (owed, name, rate)
and class attribute (numEmployee), which is used to count the number of
employee instances.
§ Class variables, such as numEmployee, share values among all the
instances of the class.
38
Creating instances of the Employee objects

--- Page 39 ---
qThe methods that begin and end with two underscores are called special
methods.
qThe only special method we call in our programs, as common practice, is the
_init_ method, to invoke the initializer of the superclass in the class definitions.
qIn the following code, we create a class that implements the _repr_ method.
This method creates a string representation of an object.
39

--- Page 40 ---
qThere are two types of methods: static methods and class methods.
qStatic methods:
§ A static method is defined within a class using the @staticmethod class
decorator. It does not require an instance of a class to execute.
§ Static methods cannot access the attributes of an instance, so their most
common usage is as a convenience to group utility functions together.
qClass methods
§ A class method operates on the class itself and does not work with the instances.
§ A class method works in the same way that class variables are associated with
the classes rather than instances of that class. Class methods are defined using
the @classmethod decorator and are distinguished from instance methods in the
class.
40

--- Page 41 ---
§ The difference between a static method and a 
class method is that a static method doesn't 
know anything about the class, it only deals with 
the parameters, whereas the class method 
works only with the class, and its parameter is 
always the class itself.
41

--- Page 42 ---
qInheritance allows to inherit the functionality from other classes.
qInheritance allows creating a new class that modifies the behavior of an existing
class.
qInheritance expresses a relationship between an existing (parent/base) class and a
new (derived/child) class, also called subclass.
qA subclass inherits all the features of its parent.
qIf an object of one class is created by inheriting another class, then the object would
have all the functionality, methods, and variables of both the classes; that is, the
parent class and new class.
qInheritance in Python is done by passing the inherited class as an argument in the
class definition. It is often used to modify the behavior of existing methods.
qFor a subclass to define new class variables, it needs to define an __init__()
method
42

--- Page 43 ---
qAn instance of the specialEmployee subclass is identical to an Employee
instance, except for the changed hours() method.
qFor example, in the following code we create a new specialEmployee
class that inherits all the functionalities of the Employee class, and also
change the hours() method:
qNotice that the methods of the base class are not automatically invoked
and it is necessary for the derived class to call them.
43

--- Page 44 ---
44

--- Page 45 ---
Thank you!


---

# Chapter 2

--- Page 1 ---
CHAPTER 2: 
PYTHON DATATYPES AND 
STRUCTURES

--- Page 2 ---
2022
DATA STRUCTURE AND ALGORITHMS 
2
OBJECTIVE OF THIS CHAPTER
Understanding various important built-in data 
types supported in Python 3.7
Exploring various additional collections of high-
performance alternatives to built-in data types

--- Page 3 ---
PYTHON DATA TYPES
2022
DATA STRUCTURE AND ALGORITHMS 
3
q In Python, no need to 
declare the type of a 
variable, unlike many 
programming 
languages.

--- Page 4 ---
NONE TYPE
q Use to show the absence of a value; like null in many
programming languages.
q Objects return None when there is nothing to return.
q Returned by False Boolean expressions.
q Used as a default value in function arguments to detect
whether a function call has passed a value or not.
4

--- Page 5 ---
NUMERIC TYPES
q Python provides the int data type that allows
standard arithmetic operators (+, -, * and / ) to
work on them.
q A Boolean data type has two possible values,
True(1) and False(0).
q Boolean values can be combined with logical
operators such as and, or, and not
5

--- Page 6 ---
q
The division operator (/) returns a float type.
q
the floor division operator (//) returns the largest integer value.
q
The operator (**) used to get the power of a number (for example, x ** y
𝑥!).
q
The operator (%) returns the remainder of the division (for example, a% b
returns the remainder of a/b).
q
The comparison operators (<, <=, >, >=, ==, and !=) work with numbers,
lists, and other collection objects and return True if the condition holds.
q
Membership operators (in and not in) test for variables in sequences, such
as lists or strings, e.g: x in y returns True if an x variable is found in y.
6
NUMERIC TYPES

--- Page 7 ---
EXAMPLES
2022
7

--- Page 8 ---
EXAMPLES
8

--- Page 9 ---
q Sequences include string, list, tuple, and range
objects.
q All sequence types have several operations that
return a value rather than change the value.
q the important methods and operations that are
common to all the sequence types
SEQUENCES TYPES

--- Page 10 ---
methods and operations
10
SEQUENCES TYPES

--- Page 11 ---
methods and operations
11
SEQUENCES TYPES

--- Page 12 ---
Tuples :
q Tuples are immutable sequences.
q It is a comma-separated sequence enclose in parentheses e.g.: tuple 
(‘a’, ‘b’, ‘c’).
q Use to set up multiple variables in one line
q Tuples are indexed by integers greater than Zero.
q It is possible to create an empty tuple by writing its name and 
parentheses e.g.: t= tuple().
q Remember to use a trailing comma when creating a tuple with one 
element e.g.: t=('a’,)
q Tuples allow to assign more than one variable at a time e.g.: x,y,z= tpl.
12
SEQUENCES TYPES

--- Page 13 ---
EXAMPLE
13

--- Page 14 ---
MAPPING TYPE
Dictionary:
q Stores data in a mapping of key and value pair
q Dictionary name= { key1: value, key2: value, ….,keyn: valuen}; 
key should be unique, value could be numbers, strings, or 
objects.
q Dictionary could be updated and test for the membership of a 
value e.g.:
q
a= {'Monday':1,'Tuesday':2,'Wednesday':3} # set dictionary a
q
a.update({'Friday':5,'Saturday':6}) #update dictionary 
q
'Wednesday' in a # return true (test for membership using in).
14

--- Page 15 ---
MAPPING TYPE
• Dictionary methods:
15

--- Page 16 ---
EXAMPLE
16

--- Page 17 ---
MAPPING TYPE
qSets :
q Unordered collections of unique items.
q Sets are mutable but, the items inside the set are immutable.
q Used to perform mathematical operations such as intersection, union, 
difference, and complement.
q Types of set objects: 
q immutable frozenset object: 
q can not use add() or clear() methods.
q can use it for a key to a dictionary
q mutable set object: 
q have additional methods such as: addition, removal, discard, and 
clear operations
17

--- Page 18 ---
MAPPING TYPE
Set methods:
18

--- Page 19 ---
MAPPING TYPE
19
Mutable set methods

--- Page 20 ---
EXAMPLE
2022
20
Mutable set

--- Page 21 ---
EXAMPLE
21
Immutable set
ﻋﻧدﻣﺎ ﻧرﯾد اﺿﺎﻓﺔ ﻣﺟﻣوﻋﺔ داﺧل ﻣﺟﻣوﻋﺔ” أو ﺗﺳﺗﺧدﻣﯾﻧﮭﺎ ﻛﻣﻔﺗﺎح ﻓﻲ dict
→اﺳﺗﺧدﻣﻲ frozensetﺑدل set

--- Page 22 ---
ARRAY
22
q The array module defines a data type array that is similar to the
list data type except for the constraint that their contents must be
of a single type of the underlying representation, as is determined
by the machine architecture or underlying C implementation.

--- Page 23 ---
ARRAY
DATA STRUCTURE AND ALGORITHMS 
23
Types of arrays:

--- Page 24 ---
ARRAY
24
qUsing arrays will storing data of the same type unlike lists.
qPerforming operations on arrays that create lists, such as list 
comprehensions, the memory efficiency gains of using an 
array in the first place will be negated.
qTo create a new data object, need to use a generator 
expression to perform the operation.
qArrays created with this module are unsuitable for work that 
requires a matrix of vector operations.

--- Page 25 ---
EXAMPLE
25

--- Page 26 ---
Thank you!


---

# Chapter 3

--- Page 1 ---
CHAPTER 3:
PRINCIPLES OF ALGORITHM 
DESIGN

--- Page 2 ---
Contents
1
• Technical requirements 
2
• An introduction to algorithms
3
• Relation Between Data Structures and Algorithms
4
• Algorithm design paradigms
5
• Recursion and backtracking
6
• Big O notation

--- Page 3 ---
1- Technical Requirements 
qWe will need to install the matplotlib library with Python to plot the 
diagram
qIt can be installed on Ubuntu/Linux by running the following 
commands on the terminal:
opython3 -mpip install matplotlib
qYou can also use the following:
osudo apt-get install python3-matplotlib
• To install matplotlib on Windows: If Python is already installed on the 
Windows operating system, matplotlib can be obtained from the 
following link to install it on Windows:
• https://github.com/ matplotlib/matplotlib/downloads 
• or https://matplotlib.org.

--- Page 4 ---
2- An Introduction To Algorithms
qThe study of algorithms is also important because it trains us to 
think very specifically about certain problems.
q It can help to increase our problem-solving abilities by isolating the 
components of a problem and defining relationships between these 
components. 

--- Page 5 ---
An Introduction to algorithms
qIn summary, there are some important reasons for studying algorithms:
oThey are essential for computer science and intelligent systems
oThey are important in many other domains (computational biology, economics,
ecology, communications, ecology, physics, and so on)
o They play a role in technology innovation
oThey improve problem-solving and analytical thinking

--- Page 6 ---
3- Relation Between Data Structures and Algorithms
There are mainly two important aspects to solve a given problem
Data
Structures
• Firstly, we need an efficient mechanism to
store, manage, and retrieve the data, which is
important to solve a problem
Algorithms
• secondly, we require an efficient algorithm
which is a finite set of instructions to solve
that problem

--- Page 7 ---
4- Algorithm Design Paradigms
qIn general, we can discern three broad approaches to algorithm design.
They are:
oDivide and conquer
oGreedy algorithms
oDynamic programming

--- Page 8 ---
Divide And Conquer
qThe divide and conquer paradigm involves:
o breaking a problem into smaller simple sub-problems,
oand then solving these sub-problems,
oand finally, combining the results to obtain a global optimal solution.
oThis is a very common and natural problem-solving technique, and is,
arguably, the most commonly used approach to algorithm design.

--- Page 9 ---
Divide And Conquer
qSome examples of divide and conquer algorithm paradigms are as 
follows:
o Binary search
o Merge sort 
oQuick sort
oKaratsuba algorithm for fast multiplication 
oStrassen's matrix multiplication 
oClosest pair of points

--- Page 10 ---
Divide and Conquer – long multiplication
qIn the following diagram, we can see that
multiplying two four-digit numbers together
requires 16 multiplication operations, and we
can generalize and say that an n digit number
requires,
approximately,
n2
multiplication
operations:
qThis method of analyzing algorithms, in terms
of the number of computational primitives
such
as
multiplication
and
addition,
is
important because it gives us a way to
understand the relationship between the time
it takes to complete a certain computation and
the size of the input to that computation. I

--- Page 11 ---
Greedy algorithms
qGreedy algorithms often involve optimization and combinatorial
problems.
qIn greedy algorithms, the objective is to obtain the best optimum
solution from many possible solutions in each step, and we try to
get the local optimum solution which may eventually lead us to
obtain the overall optimum solution.
qGenerally, greedy algorithms are used for optimization problems

--- Page 12 ---
Greedy Algorithms
qHere are many popular standard problems where we can use greedy 
algorithms
oKruskal's minimum spanning tree 
oDijkstra's shortest path 
oKnapsack problem
oPrim's minimal spanning tree algorithm 
oTravelling salesman problem

--- Page 13 ---
Greedy Algorithms Example
qEx.1:
Apply the greedy algorithm to the traveling salesperson problem,
where a greedy approach always chooses the closest destination first. This
shortest-path strategy involves finding the best solution to a local problem in
the hope that this will lead to a global solution.
qEx.2: Apply the greedy algorithm to the traveling salesperson problem; it is
an NP-hard problem. In this problem, a greedy approach always chooses the
closest unvisited city first from the current city; in this way, we are not sure
that we get the best solution, but we surely get an optimal solution. This
shortest-path strategy involves finding the best solution to a local problem in
the hope that this will lead to a global solution.

--- Page 14 ---
The Dynamic Programming
qThe dynamic programming approach is useful when our sub-problems
overlap.
qThis is different from divide and conquer.
qRather than breaking our problem into independent sub-problems,
with dynamic programming, intermediate results are cached and can be
used in subsequent operations.
qLike
divide
and
conquer,
it
uses
recursion;
however,
dynamic
programming allows us to compare results at different stages.

--- Page 15 ---
The Dynamic Programming
qThis can have a performance advantage over the divide and conquer
for some problems because it is often quicker to retrieve a previously
calculated result from memory rather than having to recalculate it.
qDynamic programming also uses recursion to solve the problems. For
example,
othe matrix chain multiplication problem can be solved using
dynamic programming.
oThe matrix chain multiplication problem determines the best
effective way to multiply the matrices when a sequence of matrices
is given, it finds the order of multiplication that requires the
minimum number of operations.

--- Page 16 ---
The Dynamic Programming Example
qLet's look at three matrices: P, Q, and R.
qTo compute the multiplication of these three matrices, we have
many
possible
choices
(because
the
matrix
multiplication
is
associative), such as (PQ)R = P(QR).
q So, if the sizes of these matrices are—P is a 20 × 30, Q is 30 × 45, R is
45 x 50, then, the number of multiplications for (PQ)R and P(QR) will
be:
o(PQ)R = 20 x 30 x 45 + 20 x 45 x 50 = 72,000
oP(QR) = 20 x 30 x 50 + 30 x 45 x 50 = 97,500
qIt can be observed from this example that if we multiply using the
first option, then we would need 72,000 multiplications

--- Page 17 ---
5- Recursion and Backtracking
qRecursion is particularly useful for divide and conquer problems;
however, it can be difficult to understand exactly what is happening,
since each recursive call is itself spinning off other recursive calls.
q A recursive function can be in an infinite loop, therefore, it is required
that each recursive function adhere to some properties.
qAt the core of a recursive function are two types of cases:
oBase cases: These tell the recursion when to terminate, meaning the
recursion will be stopped once the base condition is met
oRecursive cases: The function calls itself and we progress towards
achieving the base criteria

--- Page 18 ---
Recursion and Backtracking
qA simple problem that naturally
lends itself to a recursive solution
is calculating factorials.
qThe recursive factorial algorithm
defines two cases: the base case
when n is zero (the terminating
condition), and the recursive case
when n is greater than zero (the
call of the function itself).
qA typical implementation is the
following:
def factorial(n):
# test for a base case
if n==0:
return 1
#make a calculation and a recursive call
else:
f= n*factorial(n-1)
print(f)
return(f)
factorial(4)

--- Page 19 ---
Recursion And Backtracking
qThe following table outlines the key differences between recursion and
iteration:
Recursion
Iteration
The function calls itself. 
A set of instructions are executed repeatedly in 
the loop. 
It stops when the termination condition is 
met. 
It stops execution when the loop condition is 
met. 
Infinite recursive calls may give an error related 
to stack overflow. 
An infinite iteration will run indefinitely until 
the hardware is powered. 
Each recursive call needs memory space. 
Each iteration does not require memory 
storage. 
The code size, in general, is comparatively 
smaller. 
The code size, in general, is comparatively 
smaller. 
Recursion is generally slower than iteration. 
It is faster as it does not require a stack.

--- Page 20 ---
Backtracking 
qBacktracking is a form of recursion that is particularly useful for types of
problems such as traversing tree structures, where we are presented with
a number of options for each node, from which we must choose one.
q Subsequently, we are presented with a different set of options, and
depending on the series of choices made, either a goal state or a dead end
is reached.
qIf it is the latter, we must backtrack to a previous node and traverse a
different branch.
qBacktracking is a divide and conquer method for exhaustive searching.
Importantly, backtracking prunes branches that cannot give a result.

--- Page 21 ---
Backtracking 
qAn example of backtracking is given next. Here, we have used a 
recursive approach to generate all the possible arrangements of a 
given string, s, of a given length, n:
def bitStr(n,s):
if n==1: return s
return [digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1,s)]
print(bitStr(3,'abc'))
['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 
'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']
Notice the double list compression and the two recursive calls within this comprehension. This recursively
concatenates each element of the initial sequence, returned when n =1, with each element of the string
generated in the previous recursive call. In this sense, it is backtracking to uncover previously ungenerated
combinations. The final string that is returned is all n letter combinations of the initial string.

--- Page 22 ---
The Recursive Approach 
qIt turns out that in the case of long multiplication the answer is yes, there are in fact
several algorithms for multiplying large numbers that require less operations.
qOne of the most well-known alternatives to long multiplication is the Karatsuba
algorithm, first published in 1962.
qThis takes a fundamentally different approach: rather than iteratively multiplying
single-digit numbers, it recursively carries out multiplication operations on
progressively smaller inputs.
q Recursive programs call themselves on smaller subsets of the input.
qThe first step in building a recursive algorithm is to decompose a large number into
several smaller numbers.
qThe most natural way to do this is to simply split the number into two halves, the first
half of most-significant digits, and a second half of least-significant digits.
qFor example, our four-digit number, 2345, becomes a pair of two-digit numbers, 23
and 45.

--- Page 23 ---
from math import log10 
import math
def karatsuba(x,y):
#The base case for recursion 
from math import log10 
if x<10 or y<10:
return x*y
#sets n,the number of digits in the highest input number
n=max(int(log10(x)+1), int(log10(y)+1))
#roundsupn/2
n_2=int(math.ceil(n/2.0))
#adds 1 if n is uneven
n=n if n%2 == 0 else n+1
#splits the input numbers
a, b = divmod(x, 10**n_2)
c, d = divmod(y,10**n_2)
#applies the three recursive steps 
ac = karatsuba(a,c)
bd = karatsuba(b,d)
ad_bc = karatsuba((a+b),(c+d))-ac-bd
#performs the multiplication
return (((10**n)*ac) + bd + ((10**n_2)*(ad_bc)))
t= karatsuba(1234,3456)
print(t)
Example:  
Karatsuba 
Algorithm

--- Page 24 ---
6- Big O notation
qThe letter O in big O notation stands for order, in recognition that rates
of growth are defined as the order of a function.
q It measures the worst-case running time complexity, that is, the
maximum time to be taken by the algorithm. We say that one function
T(n) is a big O of another function, F(n), and we define this as follows
qThe function, g(n), of the input size, n, is based on the observation that
for all sufficiently large values of n, g(n) is bounded above by a constant
multiple of f(n).

--- Page 25 ---
Big O Notation
qThe objective is to find the smallest rate of
growth that is less than or equal to f(n).
qWe only care what happens at higher values of
n.
qThe variable n0 represents the threshold below
which the rate of growth is not important.
qThe function T(n) represents the tight upper
bound F(n).
qIn the plot, we can see that T(n) = n 2+ 500 = O(n
2 ), with C = 2 and n0 being approximately 23:

--- Page 26 ---
Big O Notation
• You will also see the notation f(n) = O(g(n)). 
• This describes the fact that O(g(n)) is really a set of functions that 
includes all functions with the same or smaller rates of growth than 
f(n). 
• For example, O(n 2 ) also includes the functions O(n), O(nlogn), and so 
on.

--- Page 27 ---
Big O notation
qIn the following table, we list the most common growth rates(time complexity 
or the complexity class of a function)  in order from lowest to highest. 
Complexity class
Name 
Example operations 
O(1)
Constant
append, get item, set item. 
O(logn)
Logarithmic
Finding an element in a sorted array. 
O(n)
Linear
copy, insert, delete, iteration
nLogn
Linear-logarithmic
Sort a list, merge-sort.
n2
Quadratic
Find the shortest path between two 
nodes in a graph. Nested loops.
n 3
Cubic
Matrix multiplication. 
2 n
Exponential
Towers of Hanoi problem, backtracking

--- Page 28 ---
Thank you!


---

# Chapter 4

--- Page 1 ---
CHAPTER 4:
LISTS AND POINTERS 
STRUCTURE

--- Page 2 ---
Contents
1
• Pointers in Python
2
• Node implementation
3
• Singly linked lists.
4
• doubly Linked List
5
• circularly linked lists

--- Page 3 ---
Pointer Structures VS Arrays
Arrays:
qAn array is a sequential list of data. Being sequential means that each
element is stored right after the previous one in memory.
q If your array is really big and you are low on memory, it could be
impossible to find large enough storage to fit your entire array. This
will lead to problems.
qOf course, the flip side of the coin is that arrays are very fast. Since
each element follows on from the previous one in memory, there is no
need to jump around between different memory locations.

--- Page 4 ---
Pointer structures VS Arrays
Pointer structures:
q pointer structures are lists of items that can be spread out in memory. This is
because each item contains one or more links to other items in the structure.
q The types of these links are dependent on the type of structures we have. If we
are dealing with linked lists, then we will have links to the next (and possibly
previous) items in the structure. In the case of a tree, we have parent-child links
as well as sibling links.
q they don't require sequential storage space.
q they can start small and grow arbitrarily as you add more nodes to the structure.
q However, this flexibility in pointers comes at a cost. We need additional space to
store the address.

--- Page 5 ---
The heart of lists (Nodes)
q Nodes allow us to show how the variables relate to each
other.
q A node is a container of data, together with one or more
links to other nodes. A link is a pointer.
q A simple type of node is one that has only a link to the next
node.
q Consider the example in the following diagram, in which
there are two nodes. The first node has a pointer to the
string (eggs) stored in the memory and another pointer that
stores the address of another node:
q Thus, the storage requirement for this simple node is two
memory addresses. The data attributes of the nodes are
pointers to the strings eggs and ham.

--- Page 6 ---
Finding endpoints
qIf we make the last element point to nothing,
then we make this fact clear.
qIn Python, we will use the special value None
to denote nothing.
qConsider the following diagram. Node B is the
last element in the list, and thus it is pointing
to None:
qThe last node has its next point pointing to
None. As such, it is the last node in the chain of
nodes.

--- Page 7 ---
Node class
qHere is a simple node implementation
of what we have discussed so far:
qThe Next pointer is initialized to None,
meaning that unless you change the
value of Next, the node is going to be an
endpoint.
qIf
your
node
is
going
to
contain
customer data, then create a Customer
class and put all the data there.

--- Page 8 ---
Other node types
qSometimes we want to go from node A to node B,
but at the same time we may need to go from
node B to node A. In that case, we add a Previous
pointer in addition to the Next pointer:
qAs you can see from the preceding diagram, we
have created the Previous pointer in addition to
the data and the Next pointer.
qIt is also important to note that the Next pointer
to B is None, and the Previous pointer in node A
is also None—that is to indicate that we have
reached
the
boundary
of
our
list
at
both
endpoints.

--- Page 9 ---
Introducing lists
qThe list is an important and popular data structure.
There are three kinds of the list:
1. Singly Linked List.
2. Doubly Linked List.
3. Circular Linked List.

--- Page 10 ---
First: Singly linked lists
qA singly linked list is a list with only one pointer between
two successive nodes.
q It can only be traversed in a single direction; that is, you
can go from the first node in the list to the last node, but
you cannot move from the last node to the first node.
qWe can actually use the node class that we created
earlier to implement a very simple singly linked list. For
example, we create three nodes n1, n2, and n3 that
stores three strings:
qNext, we link the nodes together so that they form a
chain:

--- Page 11 ---
Singly linked list class
qA list is a separate concept from a node.
We start by creating a very simple class to
hold our list.
qWe start with a constructor that holds a
reference to the very first node in the list
(that is tail in the following code).
q Since this list is initially empty, we will
start by setting this reference to None:

--- Page 12 ---
The append (insert) operation
qWe encapsulate data in a node so that it has
the next pointer attribute.
qFrom here, we check if there are any existing
nodes in the list (that is, whether self.tail points
to a Node or not).
qIf there is None, we make the new node the
first node of the list; otherwise, we find the
insertion point by traversing the list to the last
node, updating the next pointer of the last
node to the new node.

--- Page 13 ---
Getting the size of the list
qWe add a size member to the
SinglyLinkedList class, initializing it to
0 in the constructor.
qThen we increment the size by one
in the append method:
qThe worst-case running time (time
complexity) is O(1).

--- Page 14 ---
Deleting nodes
qWhen we want todelete a node
that is between two other nodes,
all we have to do is we make the
previous
node
point
to
the
successor of its next node that is to
be deleted.
qThat is, we simply cut the node to
be deleted out of the chain and
point directly to the next node as
shown in the diagram.

--- Page 15 ---
Deleting nodes
qHere is what the implementation
of the delete() method may look
like:
qThe delete operation to remove a
node has the time complexity
O(n).

--- Page 16 ---
Clearing a list
qWe may need to clear a list
quickly; there is a very simple
way to do it.
qWe can clear a list by simply
clearing
the
pointer
head
and tail by setting them to
None:

--- Page 17 ---
Second: Doubly linked lists
qThe
only
difference
between
a
singly linked list and a doubly linked
list is that in a singly linked list, there
is
only
one
link
between
each
successive
node,
whereas,
in
a
doubly linked list, we have two
pointers—a pointer to the next
node and a pointer to the previous
node.

--- Page 18 ---
Second: Doubly linked lists
Singly linked list Vs doubly linked lists:
q A node in a singly linked list can only determine
the next node associated with it. However, there
is no way or link to go back from this referenced
node. The direction of flow is only one way.
q A node in a doubly linked list has the ability not
only to reference the next node but also to
reference
the
previous
node
where
the
direction of the flow is bidirectional.
q Here, node A is referencing node B; in addition,
there is also a link back to node A:
Second: Doubly linked lists

--- Page 19 ---
Second: Doubly linked lists
qThe Python code to create a doubly linked list node includes its initializing
methods, the
prev pointer, the next pointer, and the data instance variables.
When a node is newly created, all these variables default to None:
qThe prev variable has a reference to the previous node, while the next variable
keeps the reference to the next node, and the data variable stores the data.

--- Page 20 ---
Second: Doubly linked lists
Doubly linked list class
qThe doubly linked list class captures the data on which our functions will be
operating. For the size method, we set the count instance variable to 0; it can be
used to keep track of the number of items in the linked list. head and tail will point to
the head and tail of the list when we begin to insert nodes into the list. Consider the
following Python code for creating a class:
qWe adopt a new convention where self.head points to the beginner node of the
list and self.tail points to the latest node added to the list.
qThis is contrary to the convention we used in the singly linked list. There are no
fixed rules as to the naming of the head and tail node pointers.

--- Page 21 ---
Second: Doubly linked lists

--- Page 22 ---
Append operation
q The append operation is used to add an element at the end of a list.
q It is important to check whether the head of the list is None. If it is None, it means
that the list is empty, or else the
list has some nodes and a new node will be
appended to the list.
q If a new node is to be added to the empty list, it should have the head pointing to
the newly created node, and the tail of the list should also point at this newly
created node through head. By the end of these series of steps, the head and tail
will now be pointing to the same node.
q The following
diagram illustrates the head and tail pointers of the doubly
linked list when a new node is added to an empty list:
Second: Doubly linked lists

--- Page 23 ---
Second: Doubly linked lists

--- Page 24 ---
Second: Doubly linked lists

--- Page 25 ---
Second: Doubly linked lists
The delete operation
q The deletion operation is easier in the doubly linked list compared to the singly linked
list.
q
The delete operation in a doubly linked list can encounter four scenarios:
o The search item to be deleted is not found in the list
o The search item to be deleted is located at the start of the list 
o
The search item to be deleted is found at the tail end of the list 
o
The search item to be deleted is located in the middle of the list

--- Page 26 ---
Second: Doubly linked lists

--- Page 27 ---
Second: Doubly linked lists
List search
The search for an item in a doubly linked list is similar to the way we did it
in the singly linked list.

--- Page 28 ---
Third: Circular lists
qA circular linked list is a special case of a
linked list. In a circular linked list, the
endpoints are connected to each other. It
means that the last node in the list points
back to the first node. In other words, we
can say that in circular linked lists all the
nodes point to the next node (and the
previous node in the case of a doubly linked
list) and there is no end node, thus no node
will point to Null.
qConsider the following diagram for the
circular linked list, based on a singly linked
list where the last node C is again connected
to the first node A, thus making a circular
list:

--- Page 29 ---
qThe following diagram shows the
concept of the circular linked list
based on a doubly linked list where
the last node C is again connected
to the first node A through the next
pointer.
qThe node A is also connected to
the
node
C
through,
previous
pointer, thus making a circular list:
Third: Circular lists

--- Page 30 ---
Appending elements
q To append an element to the
circular list in a singly linked
list, we have to just include a
new functionality so that the
newly added or appended node
points back to the tail node
Third: Circular lists

--- Page 31 ---
Third: Circular lists
Deleting an element in a circular list
q To delete a node in a circular list, it looks like we can do it
similarly to how we did in the
case of the append operation—
simply make sure that head points to the tail.
q There is just
a single line that needs to change in the delete
operation.
q It is only when we remove the tail node that we need to make
sure that the head node is updated to point to the new tail node.
This would give us the following implementation
Third: Circular lists

--- Page 32 ---
Third: Circular lists

--- Page 33 ---
Iteration through a circular list
qTo traverse the circular linked list, it is very convenient as we don't need to look
for the starting point.
qWe can start anywhere, and we just need to carefully stop traversing when
we
reach the same node again.
qWe can use the same iter() method, which we discussed at the start of this chapter.
qIt should work for our circular list; the only difference is that we have to mention
an exit condition when we are iterating through the circular list, or otherwise the
program will get stuck in a loop and it will run indefinitely
Third: Circular lists

--- Page 34 ---
Third: Circular lists
Third: Circular lists

--- Page 35 ---
Thank you!


---

# Chapter 5

--- Page 1 ---
CHAPTER 5:
STACKS AND QUEUES

--- Page 2 ---
CONTENTS
1
• Implementing stacks and queues using 
various methods
2
• Some real-life example applications of stacks 
and queues
Contents

--- Page 3 ---
STACKS
2022
DATA STRUCTURE AND ALGORITHMS 
3
qA data structure that stores data,
qSimilar to a stack of plates in a kitchen.
qPut a plate on the top of the stack, remove a plate
from the top too.
qSo, the Last In, The First Out (LIFO) structure.
qThere are two primary operations performed on
stacks: push and pop.
qPeek is an operation use to see the element on top of
the stack without popping it off.

--- Page 4 ---
STACK USAGE
• Tracking of the return address during function calls.
1. It first pushes the address of the current instruction
onto the stack, then jumps to the definition of a
2. Inside function a(), the function b() is called
3. And, the return address of the function b() is pushed
onto the stack
4. Once the execution of the instructions in b() and the
function are complete, the return address is popped off
the stack, which takes us back to function a()
5. When all the instructions in function a are completed,
the return address is again popped off from the stack,
which takes us back to the main function and the print
statement
2022
DATA STRUCTURE AND ALGORITHMS 
4

--- Page 5 ---
STACK USAGE
2022
DATA STRUCTURE AND ALGORITHMS 
5
The values for a, b, c, d will be popped off the stack. The spam element will be
popped off first and assigned to d, then ham will be assigned to c, and so on
• Pass data between functions
the values passed by the functions 14, 'eggs', 'ham', and 'spam' will be pushed onto the 
stack, one at a time

--- Page 6 ---
PUSH OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
6
q used to add an element at the top of the stack.
q To add a new node in the stack:
q check if the stack has items or it is empty
Has elements
Empty stack 
q The
new
node
must
have
its
next
pointer
pointing
to
the
node
that
was
at
the
top
earlier.
q put this new node at
the top of the stack by
pointing self.top to the
newly added node.
q If the new node to be
added
is
the
first
element,
self.top
will
point to this new node.

--- Page 7 ---
2022
DATA STRUCTURE AND ALGORITHMS 
7
IMPLEMENTATION OF THE PUSH 
OPERATION IN STACK

--- Page 8 ---
POP OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
8
The pop operation returns the topmost element of the stack and returns None if the 
stack is empty. 
Has elements
Empty stack 
• The top node has its next attribute pointing to some other node.
1- change the top pointer. 
2- The next node should be at the top. 
self.top to self.top.next.
• The pop operation is not 
allowed on an empty stack. 
• Only one node in the stack, the stack will be empty after the 
pop operation.
- change the top pointer to None.
• Removing such a node results in self.top pointing to None

--- Page 9 ---
2022
DATA STRUCTURE AND ALGORITHMS 
9
IMPLEMENTATION OF THE 
POP OPERATION IN STACK

--- Page 10 ---
PEEK OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
10
qIt returns the top element from
the stack without deleting it
from the stack.
qpeek method just returns the
topmost element; however, pop
method returns and deletes it
from the stack.
q If there is a top element in the
stack, peek returns its data;
otherwise, return None

--- Page 11 ---
QUEUES
2022
DATA STRUCTURE AND ALGORITHMS 
11
q A queue works as follows. The first person to join the queue usually gets served
first, and everyone will be served in the order of how they joined the queue.
q The acronym FIFO best explains the concept of a queue. FIFO stands for first in, first
out.
q When people are standing in a queue waiting for their turn to be served, service is
only rendered at the front of the queue.
q The only time people exit the queue is when they have been served, which only
occurs at the very front of the queue. See the following diagram, where people are
q standing in the queue, and the person in the front would be served first

--- Page 12 ---
QUEUES
2022
DATA STRUCTURE AND ALGORITHMS 
12
q The item added first, read first. 
q Enqueue: adding an element, length or size of the queue +1 
q Dequeue: deleting an element, length or size of the queue -1.
q Adding and Removing Elements from A Queue:

--- Page 13 ---
2022
DATA STRUCTURE AND ALGORITHMS 
13
IMPLEMENTATION OF QUEUE
Implementation 
Method
List Based
Stack Based
Node Based

--- Page 14 ---
LIST BASED QUEUE 
2022
DATA STRUCTURE AND ALGORITHMS 
14
qUse ListQueue class
qset items instant variables to [] in
initialization
method,
to
create
empty queue.
qSet the size of queue to (0).
qThe main operations are enqueue
and dequeue

--- Page 15 ---
THE ENQUEUE OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
15
qUsing insert method of the list class to
insert items at the front of the list.
qadd the items at index 0 in a list; is the
first position.
qIndex 0 is the only place where new data
elements are inserted into the queue.
q The size is increased by 1; self.size += 1
q Shift
method
is
another
way
of
implementing the insert at 0.

--- Page 16 ---
THE DEQUEUE OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
16
qUse to delete items from the queue
q Return and delete the topmost item from the queue.
qUse pop() to pop the last item in the list and saved in the data variable.
qEnqueue operation is inefficient because it should first shift all the elements by one space
Pop operation 

--- Page 17 ---
STACK BASED QUEUE 
2022
DATA STRUCTURE AND ALGORITHMS 
17
q Implementing queue using two
stacks
inbound_stack
and
outbound_stack.
qSet
two
instance
variables
to
create
an
empty
queue
upon
initialization.
qpush
method
for
enqueue
operation
and
pop
method
for
dequeue operation.
qThe inbound_stack to store elements
add to queue.
qNo
other
operation
can
be
performed on this stack.

--- Page 18 ---
THE ENQUEUE OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
18
qAdd items to the queue.
qReceive data to append to the
queue.
qPass
data
to
the
append
method of the inbound_stack in
the queue class.
qthe append method is used to
mimic the push operation, which
pushes elements to the top of
the stack.
qTo
enqueue
data
into
inbound_stack

--- Page 19 ---
THE DEQUEUE OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
19
qDelete elements from the queue.
qCheck
if
the
outbound_stack
is
empty or not.
qIf empty shift elements using pop
operation
from
inbound_stack
to
outbound_stack.
qIf not empty remove elements using
pop
operation
from
outbound_stack.
Shift 
pop

--- Page 20 ---
NODE BASED QUEUE 
2022
DATA STRUCTURE AND ALGORITHMS 
20
q Using a Python list to implement
a queue
qImplement queue using pointer
structures.
qUsing doubly linked list.
qUsing
insertion
and
deletion
operations.
qThe time complexity is O(1).
qA doubly linked list with FIFO kind
of data access is a queue with first
in first out method.

--- Page 21 ---
THE ENQUEUE OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
21
qAdd elements to Queue object by enqueue
method.
qEnqueue method code similar to append
operation of doubly linked list.
qCreate a node and append to tail node.
qIf
queue
empty,
point
self.head
and
self.tail to new created node.
qself.count += 1 to counts elements in the
queue which increase by line.
qIf queue not empty, point new node's
previous pointer to tail of list, and tail's
next pointer to the new node.
qUpdate tail pointer to point to the new
node.

--- Page 22 ---
THE DEQUEUE OPERATION
2022
DATA STRUCTURE AND ALGORITHMS 
22
qRemove elements to Queue object by
dequeue method.
q Remove
first
element
pointed
to
self.head,
qUse if statement
qcurrent initialized and point to self.head.
qIf self.count is 1, => one node in the list.
qTo remove node, pointed to by self.head
qself.head and self.tail set to None.
qIf queue has many nodes, shift pointing
head to next node self.head.
qWhen the count is initially 1 and more
than 1,
oreturn node point to head.
oself.count decreased by 1.

--- Page 23 ---
THANK YOU!


---

# Chapter 6

--- Page 1 ---
CHAPTER 6:
TREES

--- Page 2 ---
Contents
• Tree as a non-linear data structure
2
• Tree terminology
3
• Tree traversal
4
• Binary Trees and Binary search tree
5
• Heaps
6
• Tenary search tree

--- Page 3 ---
TREE AS A NON-LINEAR DATA STRUCTURE
q Tree is a non-linear data structure which organizes 
data in hierarchical structure . It does not store data 
sequentially like array, stack, queue and linked list
q Trees are used for a number of things, such as 
parsing expressions, searches, storing data, 
manipulating data, sorting, priority queues, and so 
on. Certain document  types, such as XML and 
HTML, can also be represented in a tree form

--- Page 4 ---
TREE TERMINOLOGY
q Node: Each circled letter in the preceding diagram represents a node. A 
node is  any data structure that actually stores the data.
q Root node: The root node is the first node from which all other nodes in 
the tree  are attached. In every tree, there is always one unique root node. 
The root node  in our example tree is node A.
q Sub-tree: A sub-tree of a tree is a tree with its nodes being a descendant 
of some  other tree. For example, nodes F, K, and L form a sub-tree of the 
original tree  consisting of all the nodes.
q Degree: The total number of children of the given node is called the 
degree of  that node. A tree consisting of only one node has a degree of 0. 
The degree of  node A in the preceding diagram is 2, the degree of node B 
is 3, the degree of  node C is 3, and similarly, the degree of node G is 1.
q Leaf node: The leaf node does not have any children, and is the terminal 
node of  the given tree. The degree of the leaf node is always 0. In the 
preceding diagram,  the nodes J, E, K, L, H, M, and I are all leaf nodes.

--- Page 5 ---
TREE TERMINOLOGY

--- Page 6 ---
TREE TERMINOLOGY
q Edge: The connection among any given two nodes in the tree is called an edge.  The 
total number of edges in a given tree will be a maximum of one less than the  total 
nodes in the tree. An example edge is shown in the preceding sample tree  structure.
q Parent: A node in the tree which has a further sub-tree is the parent node of that  
sub-tree. For example, node B is the parent of nodes D, E, and F, and node F is  the 
parent of nodes K and L.
q Child: This is a node connected to its parent, and it is the node that is    a descendant 
of that node. For example, nodes B and C are children of node A, while the nodes H, 
G, and I are the children of node C.
q Sibling: All nodes with the same parent are siblings. For example, nodes B and C  are 
siblings, and, similarly, nodes D, E, and F are also siblings.
q Level: The root node of the tree is considered to be at level 0. The children of the  
root node are considered at level 1, and the children of the nodes at level 1 are  
considered at level 2, and so on. For example, the root node is at level 0, nodes B  
and C are at level 1, and nodes D, E, F, H, G, and I are at level 2.
q Height of a tree: The total number of the nodes in the longest path of the tree is  the 
height of a tree. For example, in the preceding example tree, the height of the  tree 
is 4 as the longest paths, A-B-D-J or A-C-G-M or A-B-F-K, all have a total  number of 4 
nodes each.
q Depth: The depth of a node is the number of edges from the root of the tree to  
that node. In the preceding tree example, the depth of node H is 2

--- Page 7 ---
BINARY TREE
qA binary tree is a collection of nodes, where the nodes in the tree can have  
zero, 1, or 2 child nodes. A simple binary tree has a maximum of two children, 
that is, the  left child and the right child
q A tree is called a full binary tree if all the nodes of a binary tree have either 
zero or two  children, and if there is no node that has 1 child. 
q A binary tree is called a complete binary  tree if it is completely filled, with a 
possible exception at the bottom level, which is filled  from left to right
A binary tree node class in Python:
class Node:
def init (self, data): self.data = data  
self.right_child = None  
self.left_child = None

--- Page 8 ---
To test this class, we must first create four nodes n1, n2, n3, and n4:
n1 = Node("root node")
n2 = Node("left child node") 
n3 = Node("right child node")
n4 = Node("left grandchild node")
n1.left_child  =n2 
n1.right_child =n3 
n2.left_child  =n4
BINARY TREE

--- Page 9 ---
Tree traversal
The method to visit all the nodes in a tree is called tree traversal. This can be done either depth-
first search (DFS) or breadth-first search (BFS). We will discuss these two methods in the 
subsequent subsections.
TREE TRAVERSAL
Depth-first traversal
q In depth-first traversal, we traverse the tree, starting from the root, and go deeper into the  tree as 
much as possible on each child, and then continue to traverse to the next sibling. We  use the 
recursive approach for tree traversal. There are three forms of depth-first traversal,  namely, in-
order, pre-order, and post-order.
q In-order tree traversal works as follows. 
§
We start traversing the left sub-tree and call the in order function recursively
§
Next, we visit the root node
§
Finally, we traverse the right sub-tree and call the in order function recursively

--- Page 10 ---
TREE TRAVERSAL
The in-order traversal for this example tree is G–D-H-B-E-
A-C-F.
q The Python implementation of a recursive function to return 
an inorder listing of nodes in  a tree is as follows:
def inorder(self, root_node): 
current = root_node
if current is None: return
self.inorder(current.left_child)  print(current.data)  
self.inorder(current.right_child)

--- Page 11 ---
11
ØPre-order traversal notation
Pre-order tree traversal works as follows. 
1.We start traversing with the root node
2.Next, we traverse the left sub-tree and call the preorder function with the left  
sub-tree recursively
3.Next, we visit the right sub-tree and call the preorder function with the right  
sub-tree recursively
The pre-order traversal for this example tree would be A-B-D-G-H-E-
C-F.
TREE TRAVERSAL

--- Page 12 ---
12
The recursive function for pre-order tree traversal is as follows:
def preorder(self, root_node): current = root_node
if current is None: return
print(current.data) self.preorder(current.left_child) 
self.preorder(current.right_child)
TREE TRAVERSAL
Post-order traversal
If it is not empty, we traverse the tree. Post-order tree traversal works as  follows:
1. We start traversing the left sub-tree and call the postorder function recursively
2.Next, we traverse the right sub-tree and call the postorder function recursively
2.Finally, we visit the root node

--- Page 13 ---
13
TREE TRAVERSAL
The postorder traversal for this example tree would be G-H-D-E-B-F-C-A. 
The implementation of the post-order method for tree traversal is as follows:
def postorder(self, root_node):  current = root_node
if current is None:  return
self.postorder(current.left_child)  self.postorder(current.right_child)
print(current.data)

--- Page 14 ---
q Breadth-firsttraversal
Breadth-first traversal starts from the root of the tree and then visits every 
node on the next  level of the tree. Then, we move to the next level in the 
tree, and so on. This kind of tree  traversal is breadth-first as it broadens the 
tree by traversing all the nodes in a level before  going deep into the tree.
Let's consider the following example tree and traverse it by using the 
breadth-first traversal  method:
TREE TRAVERSAL
Thus, the breadth-first tree traversal for this tree is as follows:4, 2, 8, 1, 3, 5, and 10.

--- Page 15 ---
The Python implementation of breadth-first traversal is as follows:
from collections import deque class Tree:
def breadth_first_traversal(self): list_of_nodes = []
traversal_queue = deque([self.root_node])
We enqueue the root node and keep a list of the visited nodes in the 
list_of_nodes list.  The dequeue class is used to maintain a queue:
while len(traversal_queue) > 0:
node = traversal_queue.popleft() 
list_of_nodes.append(node.data)
if node.left_child: 
traversal_queue.append(node.left_child)
if node.right_child: 
traversal_queue.append(node.right_child)
return list_of_nodes
TREE TRAVERSAL

--- Page 16 ---
Binary trees
A binary tree is one in which each node has a maximum of two children. The nodes in 
the  binary tree are organized in the form of left sub-tree and right sub-tree.
If the tree has a  root, R, and two sub-trees, that is, left sub-tree T1, and right sub-tree 
T2, then their roots are  called left  successor and right  successor, respectively.
The following diagram is an example of a binary tree with five nodes:
BINARY TREE AND BINARY SEARCH TREE

--- Page 17 ---
Binary search trees
A binary search tree (BST) is a special kind of binary tree. It is one of the most important and commonly used
data structures in computer science applications. A binary search tree is a tree that is structurally a binary 
tree, and stores data in its nodes very efficiently. It provides very fast search operations, and other operations 
such as insertion and deletion are also very easy and convenient.
A binary tree is called a binary search tree if the value at any node in the tree is greater than the values in all 
the nodes of its left sub-tree, and less than or equal to the values of all the nodes of the right sub-tree. For 
example, if K1, K2, and K3 are key values in a tree of three nodes (as shown in the following diagram), then it
should satisfy the following conditions:
1.The key values of K2<=K1
2.The key values K3>K1
BINARY TREE AND BINARY SEARCH TREE

--- Page 18 ---
Binary search tree implementation
Let's begin the implementation of a BST in Python. We need to keep track of the root 
node of the tree, so we start by creating a Tree class that holds a reference to the
root node:
class Tree:
def init (self): self.root_node = None
That's all that is needed to maintain the state of a tree. Let's examine the main 
operations on the tree in the next section.
Binary search tree operations
The operations that can be performed on a binary search tree are insert, delete, 
finding min, finding max, searching, and so on.
BINARY TREE AND BINARY SEARCH TREE

--- Page 19 ---
Finding the minimum and maximum nodes
The structure of the binary search tree makes searching a node that has a maximum or a minimum
value very easy.
To find a node that has the smallest value in the tree, we start traversal from the root of the tree and 
visit the left node each time until we reach the end of the tree. Similarly, we traverse the right sub-
tree recursively until we reach the end to find the node with the biggest value in the tree.
For example, consider the following diagram; we move down from node 6 to 3 and then from node 
3 to 1 to find the node with the smallest value. Similarly, to find the maximum value node from the 
tree, we go down from the root to the right-hand side of the tree, then go from node 6 to node 8 
and then node 8 to node 10 to find the node with the largest value. Here is an example BST tree:
The Python implementation of the method that returns the minimum node is as
follows:
def find_min(self):
current = self.root_node while
current.left_child:
current = current.left_child
return current
BINARY TREE AND BINARY SEARCH TREE

--- Page 20 ---
Inserting nodes
One of the most important operations to implement on a binary search tree is to insert data 
items in the tree. As we have already discussed, regarding the properties of the binary 
search tree, for each node in the tree, the left child nodes should contain the data less than 
their own value and the right child nodes should have data greater than their value. So, we 
have to ensure that the property of the binary search tree satisfies whenever we insert an 
item in the tree.
For example, let's create a binary search tree by inserting data items 5, 3, 7, and 1 in the tree. 
Consider the following:
1.Insert 5: We start with the first data item, 5. To do this, we will create a node with its
data attribute set to 5, since it is the first node.
2.Insert 3: Now, we want to add the second node with value 3 so that data value 3.is
compared with the existing node value, 5, of the root node:
BINARY TREE AND BINARY
SEARCH TREE

--- Page 21 ---
Since the node value 3 is less than 5, it will be placed in the left sub-tree of node 5. 
Our BST will look as follows:
3. Insert 7: To add another node of value 7 to the tree, we start from 
the root node with value 5 and make a comparison:
Since 7 is greater than 5, the node with value 7 is placed to the right of this root.
4. Insert 1: Let's add another node with value 1. Starting from the root of the tree, we
make a comparison between 1 and 5:
This comparison shows that 1 is less than 5, so we go to the left node of 5, which is the 
node with a value of 3:
BINARY TREE AND BINARY SEARCH TREE

--- Page 22 ---
When we compare 1 with 3, since 1 is less than 3, we move a level below node 3 and to its left.
However, there is no node there. Therefore, we create a node with the value 1 and associate it with
the left pointer of node 3 to obtain the following structure. Here, we have the final binary search tree
of 4 nodes:
The Python implementation of the insert method to add the nodes in the BST is given as  
follows:
def insert(self, data): node = Node(data)
if self.root_node is None: self.root_node = node
else:
current = self.root_node parent = None
while True:
parent = current
if node.data < parent.data: current = current.left_child 
if current is None:
parent.left_child = node return
else:
current = current.right_child if current is None:
parent.right_child = node return
BINARY TREE AND BINARY SEARCH TREE

--- Page 23 ---
Deleting nodes:
Another important operation on a BST is the deletion or removal of nodes. There are  
three scenarios that we need to cater for during this process. The node that we want to 
remove might have the following:
No children: If there is no leaf node, directly remove the node
One child: In this case, we swap the value of that node with its child, and then 
delete the node
Two children: In this case, we first find the in-order successor or predecessor, 
swap the value with it, and then delete that node
In the preceding example, node A has no children, so we will simply delete it from its parent,
that is, node Z.
On the other hand, when the node we want to remove has one child, the parent of that node is 
made to point to the child of that particular node. Let's take a look at the following diagram,
where we want to delete node 6 who has one child, that is, node 5:
BINARY TREE AND BINARY SEARCH TREE

--- Page 24 ---
Searching the tree
A binary search tree is a tree data structure in which all the nodes follow the property that all the nodes 
in the left sub-tree of a node have lower key values, and have greater key values in its right sub-tree. 
Thus, searching for an element with a given key value is quite easy. Let's consider an example binary 
search tree that has nodes 1, 2, 3, 4, 8, 5, and 10, as shown in the following diagram:
Here is the implementation of the searching method in a binary search tree:
def search(self, data): current = self.root_node 
while True:
if current is None: return None
elif current.data is data:  return data
elif current.data > data:  current = 
current.left_child
else:
current = current.right_child
BINARY TREE AND BINARY SEARCH TREE

--- Page 25 ---
A heap data structure is a specialization of a tree in which the nodes are ordered 
in a specific way. Heaps are divided into max heaps and min heaps.
HEAPS
In a max heap, each parent node value must always be greater than or equal to its It
children. follows that the root node must be the greatest value in the tree.
Consider the following diagram for the max heap, where all the nodes have greater 
values compared to their children:

--- Page 26 ---
In a min heap, each parent node must be less than or equal to both its children. As a 
consequence, the root node holds the lowest value. Consider the following diagram 
for the min heap, where all the nodes have smaller values compared to their 
children:
HEAPS
Heaps are used for a number of different things. For one, they are used to 
implement priority queues. There is also a very efficient sorting algorithm, called 
heap sort, that uses heaps

--- Page 27 ---
A ternary tree is a data structure where each node of the tree can 
contain up to 3 children. It  is different compared to the binary 
search tree in the sense that a node in a binary tree can have a 
maximum of 2 children, whereas a node in the ternary tree can 
have a maximum of 3 children. The ternary tree data structure is 
also considered a special case of the trie data  structure. In trie 
data structure, each node contains 26 pointers to its children 
when we use trie data structure to store strings in contrast to the 
ternary search tree data structure, where we have 3 pointers to 
its children. The ternary search tree can be represented as follows:
TENARY SEARCH TREE

--- Page 28 ---
28
Each node stores
q A character in it. It has the equal pointer that points to 
a node that stores a value equal to the current node
q It has the left pointer that points to a node that stores a value smaller 
than the current node
q It has the right pointer that points to a node that stores a value greater 
than the current node
q Each node has a flag variable that keeps track of whether that node is the 
end of a string or not
TENARY SEARCH TREE

--- Page 29 ---
To better understand the ternary search tree data structure, we will demonstrate it 
through an example where we insert the strings PUT, CAT, SIT, SING, and PUSH to an 
empty ternary tree, as shown in the following diagram:
TENARY SEARCH TREE
Inserting a value into a ternary search tree is quite similar to how we do it in a binary search tree. 
In the ternary search tree, we follow these steps to insert a string in the ternary search tree:
q Since the tree is empty initially, we start by creating the root node with the first character, 
P, and then we create another node for the character U, and finally the character T.

--- Page 30 ---
qNext, we wish to add the word CAT. First, we compare the first 
character C with  the root node character, P. Since it does not 
match, and it is smaller than the root node, we create a new 
node for the character C on the left-hand side of the root 
node. Furthermore, we create the nodes for characters A and 
T.
qNext, we add a new word, SIT. First, we compare the first 
character, S, with the root node character, P. Since it does not 
match, and character S is greater than character P, we create 
a new node on the right-hand side for the character S. 
Furthermore, we create nodes for characters I and T.
TENARY SEARCH TREE

--- Page 31 ---
31
q Next, we insert a new word, SING, into the ternary search 
tree. We start by comparing the first character, S, to the 
root node. Since it does not match, and the character S is 
greater than the root node P, we look at the next character 
to the right-hand side, that is, S. Here, the character 
matches, so we compare the next character, which is I; this 
also matches.
q Next, we compare the character N, to the character T in 
the tree. Here, the characters do not match, so we move to 
the left- hand side of node T. Here, we create a new node 
for the character N. Furthermore, we create another new 
node for the character G.
TENARY SEARCH TREE

--- Page 32 ---
32
q Then, we add a new node, PUSH, in the ternary search tree.
First, we compare the first character of the word, that is, P, 
to the root node. Since it matches, we look at the next 
character in the ternary tree. Here, the character U also 
matches with the next character of the word. So, we look at 
the next character of the word, that is, S. It doesn't match 
with the next character in the tree, which is T. Therefore, we 
create a new node for the character S to the left-hand side of 
node T since character S is smaller than T. Next, we create 
another node for the next character, H.
TENARY SEARCH TREE

--- Page 33 ---
THANK YOU!


---

# Chapter 7

--- Page 1 ---
CHAPTER 7:
HASHING AND SYMBOL 
TABLES

--- Page 2 ---
Contents
• Hashing
2
• Hash tables

--- Page 3 ---
HASHING AND SYMBOL TABLES
❑If we have an address book entry, let's say at index number
56, that number doesn't tell us much.
❑There is nothing to link a particular contact with number
56. It is difficult to retrieve an entry from the list using the
index value.
❑In this chapter, we are going to look at a data structure that
is better suited to this kind of problem: a dictionary.
✓A dictionary uses a keyword instead of an index number,
and it stores data in (key, value) pairs.
❑So, if that contact was called James, we would probably use
the keyword James to locate the contact.
❑That is, instead of accessing the contact by calling contacts
[56], we would use contacts james.

--- Page 4 ---
HASHING AND SYMBOL TABLES
✓Dictionaries are a widely used data structure, often built
using hash tables.
✓As the name suggests, hash tables rely on a concept called
hashing.
✓A hash table data structure stores the data in key/value
pairs, where keys are obtained by applying a hash
function to it.
✓It stores the data in a very efficient way so that retrieval
can be very fast. We will discuss all the related issues in this
chapter.

--- Page 5 ---
✓Hashing is a concept in which, when we give data of an
arbitrary size to a function, we get a small simplified value.
✓This function is called a hash function. Hashing uses a hash
function that maps the given data to another range of data, so
that a new range of data can be used as an index in the hash
table.
✓More specifically, we will use hashing to convert strings into
integers.
✓In our discussions in this chapter, we are using strings to
convert into integers, however, it can be any other data type
which can be converted into integers.
✓Let's look at an example to better understand the concept. We
want to hash the expression hello
world, that is, we want
to get a numeric value that we could say represents the string.
HASHING

--- Page 6 ---
✓We can obtain the unique ordinal value of any character by using
the ord() function. For
example, the ord('f') function gives
102.
✓Further, to get the hash of the whole string, we could just sum the
ordinal numbers of each character in the string. See the following
code snippet:
>>> sum(map(ord, 'hello world')) 
1116
✓The obtained numeric value, 1116, for the whole hello
world
string is called the hash of
the string. Consider the following
diagram to see the ordinal value of each character in the string that
results in the hash value 1116:
HASHING

--- Page 7 ---
➢The preceding approach is used to obtain the hash value for a given string
and seems to work fine. However, note that we could change the order of
the characters in the string and we would have got the same hash; see the
following code snippet where we get the same hash value for the world
hello string:
>>> sum(map(ord, 'world hello'))
1116
✓Again, there would be the same hash value for the gello xorld string,
as the sum of the ordinal values of the characters for this string would
be the same since g has an ordinal value that is one less than that of h,
and x has an ordinal value that is one greater than that of w. See the
following code snippet:
>>> sum(map(ord, 'gello xorld'))
1116
Look at the following diagram, where we can observe that the hash value for
this string is again, 1116:
HASHING

--- Page 8 ---
8
Perfect hashing functions
➢A perfect hashing function is the one by which we get a unique
hash value for a given string (it can be any data type( In practice,
most of the hashing functions are imperfect and face collisions.
➢This means that a hash function gives the same hash value to
more than one string; that is undesirable because a perfect hash
function should return a unique hash value to a string.
➢Normally, hashing functions need to be very fast, so trying to
create a function that gives us a unique hash value for each string
is normally not possible.
✓Hence, we accept this fact and we know that we may get some
collisions, that is, two or more strings may have the same hash
value. Therefore, we try to find a strategy to resolve the collisions
rather than trying to find a perfect hash function.
HASHING

--- Page 9 ---
➢To avoid the collisions of the previous example, we could,
for example, add a multiplier, so that the ordinal value of
each character is multiplied by a value that continuously
increases as we progress in the string.
➢Next, the hash value of the string is obtained by adding
the multiplied ordinal value of each character.
➢To better understand the concept, refer to the
following
diagram:
HASHING

--- Page 10 ---
✓The implementation of this concept is shown in
the following function:
def myhash(s): 
  mult = 1
 hv = 0
 for ch in s:
  hv += mult * ord(ch) 
  mult += 1
  return hv
✓We can test this function on the strings that we
used earlier, shown as follows:
for item in ('hello world', 'world hello', 'gello xorld'):
 print("{}: {}".format(item, myhash(item)))
✓Running this program, we get the following output:
% python hashtest.py
hello
world:
6736
world
hello:
6616
gello
xorld:
6742
HASHING

--- Page 11 ---
11
✓We can see that, this time, we get different hash values 
for these three strings. 
✓Still, this is not a perfect hash. Let's try the strings, ad 
and ga:
% python hashtest.py
 
 ad: 297
 ga: 297
✓We still get the same hash value for two different strings.
✓ Therefore, we need to devise a strategy for resolving 
such collisions.
✓ We shall look at that shortly, but first, we will study an 
implementation of a hash table.
HASHING

--- Page 12 ---
➢A hash table is a data structure where elements are accessed
by a keyword rather than an
index number, unlike in lists
and arrays. In this data structure, the data items are stored in
key/value pairs similar to dictionaries.
➢A hash table uses a hashing function in order to find
an
index position where an element should be stored and
retrieved.
➢This gives us fast
lookups since we are using an index
number that corresponds to the hash value of the key.
➢Each position in the hash table data structure is often called a
slot or bucket and can store an element.
➢So, each data item in the form of (key,
value) pairs
would be stored in the
hash table at a position that is
decided by the hash value of the data.
HASH TABLES

--- Page 13 ---
HASH TABLES
➢For example, the hashing function maps the input string 
names to a hash value; the hello 
world string is  
mapped to a hash value of 92, which finds a slot position in 
the hash table. Consider the following diagram:

--- Page 14 ---
✓To implement the hash table, we start by creating a class to
hold hash table items. These need to have a key and a value
since our hash table is a {key-value} store:
HASH TABLES
✓This gives us a very simple way to store items. Next, we 
start working on the hash table class itself. As usual, we 
start off with a constructor:

--- Page 15 ---
✓We will now initialize a list containing 256 elements in the
code.
✓These are the positions where the elements are to be
stored—the slots or buckets.
✓So, we have 256 slots to store elements in the hash table.
✓Finally, we add a counter for the
number of actual hash
table elements we have:
HASH TABLES

--- Page 16 ---
Implementation of the hash function: 
Storing elements in a hash table
✓To store the elements in the hash 
table, we add them to the table 
with the put() 
function and 
retrieve them with the get() 
function.
✓ First, 
we 
will 
look 
at 
the  
implementation of the put() 
function. We start by embedding 
the key and the value into  the 
HashItem 
class 
and 
then 
compute the hash value of the 
key.
✓Here is the implementation of the 
put function to store the elements 
in the hash table:
HASH TABLES

--- Page 17 ---
✓For example the hello world key string is already stored in the
table, and there is a collision when a new string, world
hello, gets the same hash value of 92. Take a look at the
following diagram:
HASH TABLES

--- Page 18 ---
✓One way of resolving this kind of
collision is to find another free slot
from the position of the collision; this
collision resolution process is called
open addressing.
✓We can do this by linearly looking for
the next available slot by adding 1 to
the previous hash value where we get
the collision.
✓We can resolve this conflict by adding
1 to the sum of the ordinal values of
each character in the key string, which
is further divided by the size of the
hash table to obtain the hash value.
✓
This systematic way of visiting each
slot
is
a
linear
way
of
resolving
collisions and is called linear probing.
HASH TABLES

--- Page 19 ---
Retrieving elements from the hash table
✓To retrieve the elements from the hash table, the value stored
corresponding to the key would be returned.
✓Here, we will discuss the implementation of the retrieval
method—the get() method. This method would return the
value stored in the table corresponding to the given key.
✓First of all, we compute the hash of the given key corresponding
to the value that is to be retrieved. Once we have the hash
value of the key, we look up the hash table at the position of
the hash value.
✓If the key item is matched with the stored key value at that
location, the corresponding value is retrieved.
HASH TABLES

--- Page 20 ---
✓If that does not match, then we add 1 to the  sum of the ordinal 
values of all the characters in the string, similar to what we did at 
the time of storing the data, and we look at the newly obtained 
hash value.
✓ We keep looking until we get our key element or we check all 
the slots in the hash table.
HASH TABLES

--- Page 21 ---
✓To test our hash table, we create HashTable and store a few elements in it,
then try to retrieve them.
✓We will also try to get() a key that does not exist. We also use the two
strings, ad and ga, which had the collision and returned the same hash
value by our hashing function. .
o As you can see, looking up the worst key 
returns None, since the key does not exist. 
o The ad and ga keys also return their 
corresponding 
values, 
showing 
that 
the 
collision between them is properly handled.
HASH TABLES

--- Page 22 ---
✓To grow the size of the hash table, we compare the size and the count in
the table.
✓size is the total number of the slots and count denotes the number of
slots that contains elements.
✓
So, if count is equal to size, that means we have filled up the table. The
load factor of the hash table is generally used to expand the size of the
table; that gives us an indication of how many available slots of the table
have been used.
✓The load factor of the hash table is computed by dividing the number of
used slots by the total number of slots in the table. It
is defined as
follows:
GROWING A HASH TABLES

--- Page 23 ---
✓The collision resolution mechanism we used in our example
was linear probing, which is an
example of an open
addressing strategy.
✓Linear probing is simple since we use a fixed
number of
slots.
✓There are other open addressing strategies as well, however,
they all share the idea that there is an array of slots.
✓When we want to insert a key, we check whether the
slot
already has an item or not. If it does, we look for the next
available slot.
OPEN ADDRESSING

--- Page 24 ---
✓Chaining is another method to handle the problem of collision in hash
tables.
✓It solves this problem by allowing each slot in the hash table to store a
reference to many items at the position of a collision.
✓So, at the index of a collision, we are allowed to store many items in the
hash table.
✓Observe the following diagram—there is a collision for the strings, hello
world and world hello. In the case of chaining, both items are allowed to
store at the location of the 92 hash value using a list. Here is the example
diagram to show collision resolution using chaining:
CHAINING

--- Page 25 ---
CHAINING
✓In chaining, the slots in the hash table 
are initialized with empty lists:
✓When an element is inserted, it will be 
appended to the list that corresponds 
to that  element's hash value. That is, 
if you have two elements that both 
have a hash value of 1075,  both of 
these elements would be added to the 
list that exists in the 1075%256=51 
slot of the  hash table:
✓The preceding diagram shows a list of 
entries with hash value 51.

--- Page 26 ---
✓Chaining then avoids conflict by allowing multiple elements to
have the same hash value.
✓Hence, there is no limit on the number of elements that can be
stored in a hash table, whereas, in the case of linear probing,
we had to fix the size of the table, which we need to later grow
when the table is filled up, depending upon the load factor.
✓Moreover, the hash
table can hold more values than the
number of available slots, since each slot holds a list that can
grow.
CHAINING

--- Page 27 ---
27
HASH TABLES
✓However, there is a problem in chaining—it becomes inefficient 
when a list grows at a particular hash value location. 
✓As a particular slot has many items, searching them can get 
very slow since we have to do a linear search through the list 
until we find the element that has the key we want. 
✓This can slow down retrieval, which is not good, since hash 
tables are 
meant to be efficient. The following diagram 
demonstrates a linear search through list items until we find a 
match:

--- Page 28 ---
28
✓So, there is a problem of slow retrieval of items when a
particular position in a hash table has many entries.
✓This problem can be resolved using another data structure in
place of
using a list that can perform fast searching and
retrieval. There is a nice choice of using binary search trees
(BSTs), which provide fast retrieval, as we discussed in the
previous chapter.
✓We could simply put an (initially empty) BST in each slot as 
shown in the following diagram:
HASH TABLES

--- Page 29 ---
➢Symbol tables are used by compilers and interpreters to keep track
of the symbols that have been declared and to keep information
about them. Symbol tables are often built using hash tables since it
is important to efficiently retrieve a symbol from the table.
Let's look at an example. Suppose we have the following Python code:
name = "Joe" age = 27
✓Here, we have two symbols, name and age. They belong to a
namespace, which could be
main
, but it could also be the name of a module if you placed
it there.
✓Each symbol has a value; for example, the name symbol has the
value, Joe, and the age symbol has the value, 27. A symbol table
allows the compiler or the interpreter to look up these values. So,
the name and age symbols become keys in the hash table. All of
the other information associated with them become the value of
the symbol table entry.
SYMBOL TABLES

--- Page 30 ---
✓It's not only variables
that are symbols, but
functions and classes
are
also
treated
as
symbols, and they will
also be added to the
symbol table so that,
when any one of them
needs to be accessed,
they
are
accessible
from the symbol table.
✓For
example,
the
greet()
function
and two variables are
stored in the symbol
table in the following
diagram:
SYMBOL TABLES

--- Page 31 ---
✓In Python, each module that is loaded has its own
symbol table.
✓The symbol table is given the name of that module. This
way, modules act as namespaces.
✓We can have multiple
symbols of the same name as
long as they exist in different symbol tables, and we can
access them through the appropriate symbol table.
✓See the following example, showing
multiple symbol
tables in a program:
SYMBOL TABLES

--- Page 32 ---
THANK YOU!


---

# Chapter 8

--- Page 1 ---
CHAPTER 8:
GRAPHS

--- Page 2 ---
1
• Terminology
2
• Undirected Graphs
3
• Directed Graphs
4
• Weighted  - Implementing Graphs
5
• Graph Representation
Contents
6
• Graph Traversals

--- Page 3 ---
Graphs - Terminology
◼
Like trees, graphs are made up of nodes and the connections between those 
nodes
◼
In graph terminology, we refer to the nodes as vertices and refer to the 
connections among them as edges
◼
Vertices are typically referenced by a name or label
◼
Edges are referenced by a pairing of the vertices (A, B) that they connect
3
Undirected
Directed (Digraph)
Weighted
3

--- Page 4 ---
Graphs - Terminology (cont…)
◼Two vertices are said to be adjacent  if there is an edge connecting 
them
◼Adjacent vertices are sometimes referred to as neighbors
◼Loop: When an edge from a node is incident on itself, that edge 
forms a loop For example, {v1, v1}
◼A path is a sequence of edges that connects two vertices in a graph
◼The length of a path in is the number of edges in the path (or the 
number of vertices minus 1)
◼Degree of a vertex: The total number of edges that are incident on a 
given vertex is called the degree of that vertex
◼Leaf vertex (also called pendant vertex): A vertex or node is called a 
leaf vertex or pendant vertex if it has exactly one degree

--- Page 5 ---
Undirected Graphs
5
◼
An undirected graph is a graph where the pairings representing the edges 
are unordered
◼
We will define an Undirected Graph ADT as a collection of vertices
V = {v1, v2, ..., vn}
The number of vertices is denoted by
|V| = n
Associated with this is a collection E of unordered pairs {vi, vj} termed edges 
which connect the vertices
◼
An undirected graph:
5

--- Page 6 ---
◼An edge in an undirected graph can be traversed in either direction
◼An undirected graph is considered complete if it has the maximum 
number of edges connecting vertices
◼There are a number of data structures that can be used to 
implement abstract undirected graphs
Adjacency matrices
Adjacency lists
6
Undirected Graphs (cont…)
6

--- Page 7 ---
◼Consider this collection of vertices 
V = {v1, v2, ..., v9}
 
where |V| = n  = 9
7
Undirected Graphs (cont…)
7

--- Page 8 ---
◼Associated with these vertices are |E| = 5 edges
E = {{v1, v2}, {v3, v5}, {v4, v8}, {v4, v9}, {v6, v9}}
The pair {vj , vk} indicates that both vertex vj is adjacent to vertex vk 
and vertex vk is adjacent to vertex vj 
8
Undirected Graphs (cont…)
8

--- Page 9 ---
◼Example: given the |V| = 7 vertices
V = {A, B, C, D, E, F, G} 
◼and the |E| = 9 edges
 
    E = {{A, B}, {A, D}, {A, E}, {B, C}, {B, D}, {B, E}, {C, E}, {C, F}, {D, E}}
9
Undirected Graphs (cont…)
9

--- Page 10 ---
Undirected Graphs - Degree
◼The degree of a vertex is defined as the number of adjacent vertices
 
degree(A) = degree(D) = degree(C) = 3
 
degree(B) = degree(E) = 4
 
degree(F) = 1
 
degree(G) = 0
◼Those vertices adjacent to a given vertex are its neighbors
10
10

--- Page 11 ---
Undirected Graphs - Connectedness (cont…)
◼An example of an undirected graph that is not 
connected:
11
11

--- Page 12 ---
Directed Graphs
◼A directed graph, sometimes referred to as a digraph, 
is a graph where the edges are ordered pairs of 
vertices
◼This means that the edges (A, B) and (B, A) are 
separate, directional edges in a directed graph
12
12

--- Page 13 ---
◼In a directed graph, the edges on a graph are be 
associated with a direction
Edges are ordered pairs (vj, vk) denoting a connection from 
vj to vk 
The edge (vj, vk) is different from the edge (vk, vj)
◼Streets are directed graphs:
In most cases, you can go two ways unless it is a one-way 
street
13
Directed Graphs (cont…)
13

--- Page 14 ---
Directed Graphs (cont…)
◼A directed graph with
vertices A, B, C, D
edges (A, B), (A, D), (B, C), (B, D) and (D, C)
14
14

--- Page 15 ---
Directed Graphs - In and Out Degrees
◼The degree of a vertex must be modified to consider both cases:
The out-degree of a vertex is The total number of edges that goes 
out from a vertex in the graph is called the outdegree of that vertex
The in-degree of a vertex is The total number of edges that come 
into a vertex in the graph is called the indegree of that vertex
◼In this graph:
 
in_degree(v1) = 0 
out_degree(v1) = 2
 
in_degree(v5) = 2 
out_degree(v5) = 3
15
15

--- Page 16 ---
Directed Graphs - Sources and Sinks
◼Some definitions:
Source vertex: Vertices with an in-degree of zero are 
described as sources
Sink vertex:Vertices with an out-degree of zero are 
described as sinks
Isolated vertex: A node or vertex is called an 
isolated vertex when it has a degree of zero
◼In this graph:
Sources: v1, v6, v7 
Sinks: 
v2, v9 
16
16

--- Page 17 ---
Weighted Graphs
◼
A weighted graph, sometimes called a network, is a graph with weights (or costs) 
associated with each edge
◼
The weight of a path in a weighted graph is the sum of the weights of the edges in 
the path
◼
Weighted graphs may be either undirected or directed
◼
For weighted graphs, we represent each edge with a triple including the starting 
vertex, ending vertex, and the weight (Boston, New York, 120)
17
17

--- Page 18 ---
◼A weight may be associated with each edge in a graph
This could represent distance, energy consumption, cost, etc.
Such a graph is called a weighted graph
◼Pictorially, we will represent weights by numbers next to the edges
18
Weighted Graphs (cont…)
18

--- Page 19 ---
◼The length of a path within a weighted graph is the sum of all of the 
edges which make up the path
The length of the path (A, D, G) in the following graph is 5.1 + 3.7 = 8.8
19
Weighted Graphs (cont…)
19

--- Page 20 ---
Implementing Graphs
◼
Strategies for implementing graphs:
◼
Adjacency lists
use a set of graph nodes which contain a linked list storing the edges within 
each node
for weighted graphs, each edge would be stored as a triple including the 
weight
◼
Adjacency matrices
use a two dimensional array
each position of the array represents an intersection between two vertices in 
the graph
each intersection is represented by a boolean value indicating whether or not 
the two vertices are connected
20
20

--- Page 21 ---
adjacency matrix
adjacency list
Graph Representation
21

--- Page 22 ---
◼
Adjacency Matrix uses a 2-D array of dimension |V|x|V| for edges. 
(For vertices, a 1-D array is used)
◼
The presence or absence of an edge, (v, w) is indicated by the entry 
in row v, column w of the matrix.
◼
For an unweighted graph, boolean values could be used.
◼
For a weighted graph, the actual weights are used.
Adjacency Matrix Representation
22

--- Page 23 ---
◼An undirected graph and it's adjacency matrix:
23
◼A directed graph and its adjacency matrix:
Adjacency Matrix Representation (cont…)
23

--- Page 24 ---
◼
This involves representing the set of vertices adjacent to each vertex as 
a list.  Thus, generating a set of lists.
◼
This can be implemented in different ways.
◼
In the following representation: 
Vertices as a one dimensional array
Edges as an array of linked list (the emanating edges of vertex 1 will be in the 
list of the first element, and so on, …
1
2
3
4
vertices
•
•
•
•
edges
•
1,2
•
1,3
Null
•
2,3
•
2,4
Null
•
4,1
•
4,3
Null
•
4,2
Empty
Adjacency List Representation
24

--- Page 25 ---
Graph traversals Algorithms
◼There are a number of a common algorithms that may 
apply to undirected, directed, and/or weighted graphs
◼These include
various traversal algorithms breadth-first search (BFS) and 
depth-first search (DFS). 
25
25

--- Page 26 ---
Graph Traversals
◼Traversals of graphs are also called searches
◼There are two main types of graph traversal algorithms
breadth-first: behaves much like a level-order traversal of a tree
◼Breadth-first requires a queue
depth-first: behaves much like the preorder traversal of a tree
◼Depth-first requires a stack
◼One difference: there is no root node present in a graph
◼Graph traversals may start at any vertex in the graph
26
26

--- Page 27 ---
◼In this method, We start visiting the first node, A, and then add all its 
adjacent vertices, B, C, and E, to the queue. Here, it is important to 
note that there are multiple ways of adding the adjacent nodes to the 
queue, since there are three nodes, B, C, and E, that can be added 
in the queue as either BCE, CEB, CBE, BEC, or ECB, each of which 
would give us different tree traversal results
Breadth-First Traversal
27

--- Page 28 ---
Breadth-First Traversal (cont…)
◼The A node is visited as shown:
◼Once we have visited the A vertex, next, we visit its first adjacent 
vertex, B, and add those adjacent vertices that are not already 
added in the queue or not visited. In this case, we have to add the D 
vertex to the queue:
28
28

--- Page 29 ---
Breadth-First Traversal (cont…)
◼
Now, after visiting the B vertex , we visit the next vertex from the 
queue—the C vertex. And again, add those of its adjacent vertices that 
have not already been added in the queue. In this case, there are no 
unrecorded vertices left, so there is no need to do anything
◼
After visiting the C vertex, we visit the next vertex from the queue, the E 
vertex:
29
29

--- Page 30 ---
a
b c
f
b
c
f
e     g
e
g
d
h
d
h
30
Breadth-First Traversal (cont…)
30
Similarly, after visiting the E vertex, we visit 
the D vertex in the last step: 

--- Page 31 ---
31
Breadth-First Traversal (cont…)
31
graph = dict()  
graph['A'] = ['B', 'G', 'D']  
graph['B'] = ['A', 'F', 'E']  
graph['C'] = ['F', 'H']  
graph['D'] = ['F', 'A']  
graph['E'] = ['B', 'G']  
graph['F'] = ['B', 'D', 'C']  
graph['G'] = ['A', 'E']  
graph['H'] = ['C']  
from collections import deque
def breadth_first_search(graph, root): 
    visited_vertices = list() 
    graph_queue = deque([root]) 
    visited_vertices.append(root) 
    node = root 
    while len(graph_queue) > 0: 
        node = graph_queue.popleft() 
        adj_nodes = graph[node] 
        remaining_elements = set(adj_nodes).difference(set(visited_vertices)) 
        if len(remaining_elements) > 0: 
            for elem in sorted(remaining_elements): 
                visited_vertices.append(elem) 
                graph_queue.append(elem) 
    return visited_vertices 
print(breadth_first_search(graph, 'A'))

--- Page 32 ---
◼In this method, After visiting a vertex v, which is adjacent to 
w1, w2, w3, ...;  Next we visit one of v's adjacent vertices, w1 
say.  Next, we visit all vertices adjacent to w1 before coming 
back to w2, etc. The stack data structure is used to implement 
the DFS algorithm. 
◼We start by visiting the A node, and then we look at the 
neighbors of the A vertex, then a neighbor of that neighbor, 
and so on. Let's consider the following graph in the context of 
DFS:
Depth-First Traversal
32

--- Page 33 ---
After visiting the A vertex, we visit one of its 
neighbors, B, as shown

--- Page 34 ---
Depth-First Traversal (cont…)
◼
After visiting the B vertex, we look at another neighbor of A, that is, S, as there 
is no vertex connected to B which can be visited. Next, we look for the 
neighbors of the S vertex, which are the C and G vertices. We visit C as 
follows: 
34
34

--- Page 35 ---
After visiting the C node, we visit its neighboring vertices, D and E: 
 
 
35
Depth-First Traversal (cont…)
35

--- Page 36 ---
Similarly, after visiting the E vertex, we visit the H and F vertices, as shown in the following 
graphs: 
36
Depth-First Traversal (cont…)
36

--- Page 37 ---
THANK YOU!


---

# Chapter 9

--- Page 1 ---
CHAPTER 9:
PRINCIPLES OF 
ALGORITHM DESIGN

--- Page 2 ---
Contents
• Introduction to searching 
2
• Linear search

--- Page 3 ---
Searching algorithms are categorized into two 
broad types: 
1. The searching algorithm applied to list of 
items that are already sorted; that is, applied 
to the ordered set of items.
2. The searching algorithm applied to unordered 
set of items, which are not sorted. 
INTRODUCTION TO SEARCHING 

--- Page 4 ---
❑A linear search simply examines each item in the 
search pool, one at a time, until either the target is 
found or until the pool is exhausted.
❑This approach does not assume the items in the 
search pool are in any particular order.
LINEAR SEARCH

--- Page 5 ---
Problem: Given an array arr[] of n elements, write a function to search a 
given element x in arr[].
LINEAR SEARCH - IMPLEMENTATION 
Examples
Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}, 
x = 110;
Output : 6 Element x is present at index 6 
 Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170} 
x = 175; 
Output : -1 Element x is not present in arr[].
 
A simple approach is to do a linear search:
❑Start from the leftmost element of arr[] and one by one compare x 
with each element of arr[]
❑If x matches with an element, return the index.
❑If x doesn’t match with any of the elements, return -1.

--- Page 6 ---
# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
#  print arr.index(x)
# If you want to implement Linear Search in python
# Linearly search x in arr[]
# If x is present then return its location
# else return -1
def search(arr, x):
for i in range(len(arr)):
if arr[i] == x:
return i
return -1
LINEAR SEARCH - IMPLEMENTATION 

--- Page 7 ---
# This is similar to the above one, with the only difference
# being that it is using the recursive approach instead of iterative.
def search(arr, curr_index, key):
 
if curr_index == -1:
 
 
return -1
 
if arr[curr_index] == key:
 
 
return curr_index
 
return search(arr, curr_index-1, key)
RECURSIVE APPROACH:

--- Page 8 ---
❑A binary search is a search strategy used to find 
elements within a sorted array or list; thus, the binary 
search algorithm finds a given item from the given 
sorted list of items.
 
❑It is a very fast and efficient algorithm to search an 
element, and the only drawback is that we need a 
sorted list. 
❑The worst-case running time complexity of a binary 
search algorithm is O(log n) whereas the linear search 
has O(n).
BINARY SEARCH

--- Page 9 ---
BINARY SEARCH

--- Page 10 ---
BINARY SEARCH

--- Page 11 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]

--- Page 12 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Find approximate midpoint

--- Page 13 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Is 7 = midpoint key?  NO.
 

--- Page 14 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Is 7 < midpoint key? YES.
 

--- Page 15 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Search for the target in the area before midpoint.
 

--- Page 16 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Find approximate midpoint

--- Page 17 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Target = key of midpoint? NO.

--- Page 18 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Target < key of midpoint? NO.

--- Page 19 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Target > key of midpoint? YES.

--- Page 20 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Search for the target in the area after midpoint.
 

--- Page 21 ---
BINARY SEARCH
[ 0 ]
[ 1 ]
Example: sorted array of integer keys.  Target=7.
3
6
7
11
32
33
53
[ 2 ]
[ 3 ]
[ 4 ]
[ 5 ]
[ 6 ]
Find approximate midpoint.
Is target = midpoint key?  YES.

--- Page 22 ---
BINARY SEARCH IMPLEMENTATION
# Python code to demonstrate working
# of binary search in library
from bisect import bisect_left
def BinarySearch(a, x):
 
i = bisect_left(a, x)
 
if i != len(a) and a[i] == x:
 
 
return i
 
else:
 
 
return -1
a = [1, 2, 4, 4, 8]
x = int(4)
res = BinarySearch(a, x)
if res == -1:
 
print(x, "is absent")
else:
 
print("First occurrence of", x, "is present at", res)
First occurrence of 4 is present at 2 

--- Page 23 ---
BINARY SEARCH IMPLEMENTATION (NEW CODE) 
def binary_search(ordered_list, term):
    size_of_list = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = size_of_list
    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)//2
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1
store = [2, 4, 5, 12, 43, 54, 60, 77]
a = binary_search(store, 2)
print("Index position of value 2 is ",a)

--- Page 24 ---
THANK YOU!


---

# Chapter 10

--- Page 1 ---
CHAPTER 10:
SORTING

--- Page 2 ---
Contents
• Sorting Techniques

--- Page 3 ---
CHAPTER GOALS
❑In this chapter, we'll study some of the most important and
popular sorting techniques, including the following:
oBubble sort
oInsertion sort
oSelection sort
oQuick sort
oHeap sort
❑In this chapter, we compare different sorting algorithms by
considering their asymptotic behavior. Some of the algorithms
are relatively easy to develop, but may perform poorly, whereas
other algorithms are slightly more complex to implement, but
show good performance in sorting the list when we have a long
lists.
3

--- Page 4 ---
SORTING ALGORITHMS
❑Sorting means arranging all the items in a list in ascending order of their
magnitude.
❑We will be discussing some of the most important sorting algorithms,
which each have different performance attributes with respect to runtime
complexity.
❑Sorting algorithms are categorized by their memory usage, complexity,
recursion,
and
whether
they
are
comparison-based,
among
other
considerations.
❑Some of the algorithms use more CPU cycles, and, as such, have bad
asymptotic values.
❑Other algorithms chew on more memory and other computing resources
as they sort a number of values.
❑Another consideration is how sorting algorithms lend themselves to being
expressed recursively, iteratively, or both.
❑There are algorithms that use comparison as the basis for sorting
elements. An example of this is the bubble sort algorithm. Examples of a
non-comparison sorting algorithm are the bucket sort and pigeonhole sort
algorithms.
4

--- Page 5 ---
BUBBLE SORT ALGORITHMS
❑Given an unordered list, we compare adjacent elements in the list, and
after each comparison, place them in the right order of magnitude. This
works by swapping adjacent items if they are not in the correct order. The
process is repeated n-1 times for a list of n items.
❑In each such iteration, the largest element is arranged in the end. For
example, in the first iteration, the largest element would be placed in the
last position of the list, and again, the same process will be followed for
the remaining n-1 items.
❑In the second iteration, the second largest element will be placed at the
second-to-last position in the list, and the process will then be repeated
until the list is sorted.
❑Let's take a list with only two elements, {5, 2}, to understand the concept
of the bubble sort,
❑as shown in the following diagram:
5
Bubble sort is the simplest sorting algorithm that 
works by repeatedly swapping the adjacent 
elements in case they are unordered in n-1 passes.

--- Page 6 ---
BUBBLE SORT ALGORITHMS
❑To sort this list, we simply swap the values into the right
positions, with 2 occupying index 0 and 5 occupying index 1.
To effectively swap these elements, we need to have a
temporary storage area:
❑Implementation of the bubble sort algorithm starts with
the swap method, illustrated in the preceding diagram.
❑First, element 5 will be copied to a temporary location,
temp. Then, element 2 will be moved to index 0. Finally, 5
will be moved from temp to index 1. At the end of it all, the
elements will have been swapped.
6

--- Page 7 ---
BUBBLE SORT EXAMPLE
7

--- Page 8 ---
8
BUBBLE SORT EXAMPLE

--- Page 9 ---
BUBBLE SORT ALGORITHMS
❑The implementation of the bubble sort algorithm would work in a
double-nested loop, where the inner loop repeatedly compares
and swaps the adjacent elements in each iteration for a given list,
and the outer loop keeps track of how many times the inner loop
should be repeated. The implementation of the inner loop is as
follows:
❑The bubble sort is an inefficient sorting algorithm that provides
worst-case and average case runtime complexity of O(n2), and a
best-case complexity of O(n). Generally, the bubble sort algorithm
should not be used to sort large lists. However, on relatively small
lists, it performs fairly well.
9

--- Page 10 ---
INSERTION SORT ALGORITHMS
❑The idea of swapping adjacent elements to sort a list of items can
also be used to implement the insertion sort. An insertion sorting
algorithm maintains a sub-list that is always sorted, while the
other portion of the list remains unsorted.
❑We take elements from the unsorted sub-list and insert them in
the correct position in the sorted sub-list, in such a way that this
sub-list remains sorted.
❑In insertion sorting, we start with one element, assuming it to be
sorted, and then take another element from the unsorted sub-list
and place it at the correct position (in relation to the first element)
in the sorted sub-list. This means that our sorted sub-list now has
two elements. Then, we again take another element from the
unsorted sub-list, and place it in the correct position (in relation to
the two already sorted elements) in the sorted sub-list.
❑We repeatedly follow this process to insert all the elements one
by one from the unsorted sub-list into the sorted sub-list.
10

--- Page 11 ---
INSERTION SORT ALGORITHMS
11

--- Page 12 ---
INSERTION SORT ALGORITHMS
12

--- Page 13 ---
INSERTION SORT ALGORITHMS
❑The while loop traverses the list backward, guided by two
conditions: first, if search_index > 0, then it means that there are
more elements in the sorted portion of the list; second, for the
while loop to run, unsorted_list[search_index-1] must be greater
than the insert_value variable. The unsorted_list[search_index-1]
array will do either of the following things:
❑Point to the element, just before the unsorted_list[search_index],
before the while loop is executed the first time
❑Point to one element before unsorted_list[search_index-1] after the
while loop has been run the first time
❑The insertion sorting algorithm is considered stable, in the sense
that it does not change the relative order of elements that have
equal keys. It also only requires no more memory than that
consumed by the list, because it does the swapping in-place.
❑Insertion
sorting
algorithm
gives
a
worst-case
runtime
complexity of O(n2), and a best-case complexity O(n).
13

--- Page 14 ---
SELECTION SORT ALGORITHMS
❑Another popular sorting algorithm is the selection sort.
❑The selection sorting algorithm begins by finding the smallest
element in the list, and interchanges it with the data stored at the
first position in the list.
❑Thus, it makes the sub-list sorted up to the first element. Next,
the second smallest element, which is the smallest element in the
remaining list, is identified and interchanged with the second
position in the list.
❑This makes the initial two elements sorted. The process is
repeated, and the smallest element remaining in the list should be
swapped with the element in the third index on the list. This
means that the first three elements are now sorted. This process is
repeated for (n-1) times to sort n items.
14

--- Page 15 ---
SELECTION SORT ALGORITHMS
❑First Iteration
15
❑Second Iteration

--- Page 16 ---
SELECTION SORT ALGORITHMS
❑The selection sorting algorithm gives worst-case and best-case
runtime complexities of O(n2).
16

--- Page 17 ---
QUICK SORT ALGORITHMS
❑The quick sort algorithm is very efficient for sorting. The quick sort
algorithm falls under the divide and conquer class of algorithms,
similar to the merge sort algorithm, where we break (divide) a
problem into smaller chunks that are much simpler to solve
(conquer).
❑The concept behind quick sorting is partitioning a given list or
array. To partition the list, we first select a pivot. All the elements in
the list will be compared with this pivot. At the end of the
partitioning process, all elements that are less than the pivot will
be to the left of the pivot, while all elements greater than the pivot
will lie to the right of the pivot in the array.
❑For the sake of simplicity, we'll take the first element in an array as
the pivot. This kind of pivot selection degrades in performance,
especially when sorting an already sorted list. Randomly picking the
middle or last element in the array as the pivot does not improve
the performance of the quick sort.
17

--- Page 18 ---
QUICK SORT ALGORITHMS
❑We partition an unsorted array into two sub-arrays, in such a way
that all the elements on the left side of that partition point (also
called a pivot) should be smaller than the pivot, and all the
elements on the right side of the pivot should be greater.
❑After the first iteration of the quick sort algorithm, the chosen
pivot point is placed in the list at its correct position.
❑After the first iteration, we obtain two unordered sub-lists, and
follow the same process again on these two sub-lists.
❑Thus, the quick sort algorithm partitions the list into two parts
and recursively applies the quick sort algorithm on these two sub-
lists to sort the whole list.
18

--- Page 19 ---
QUICK SORT ALGORITHMS
❑We start by choosing a pivot point with which all the items are to
be compared, and at the end of the first iteration, this value will be
placed in its correct position in the ordered list.
❑Next, we use two pointers, a left pointer, and a right pointer. The
left pointer initially points to the value at index 1, and the right
pointer points to the value at the last index. The main idea behind
the quick sort algorithm is to move the items that are on the
wrong side of the pivot value.
❑So, we start with the left pointer, moving from in a left-to-right
direction, until we reach a position where the item has a greater
value than the pivot value. Similarly, we move the right pointer
toward the left until we find a value less than a pivot value.
❑Next, we swap these two values indicated by the left and right
pointers. We repeat the same process until both pointers cross
each other; in other words, when the right pointer index indicates
a value less than that of the left pointer index.
19

--- Page 20 ---
EXAMPLE
20

--- Page 21 ---
EXAMPLE
❑It can be observed that after the
first iteration of the quick sort
algorithm, the pivot value 45 is
placed at its correct position in
the list.
❑Now we have two sub-lists:
oThe sub-list to the left of the
pivot value, 45, has values of
less than 45.
oAnother sub-list to the right of
the pivot value contains values
greater than 45.
❑We will apply the quick sort
algorithm recursively on these
two sub-lists, and repeat it until
the whole list is sorted.
21

--- Page 22 ---
HEAP SORT ALGORITHMS
❑In Chapter 8, Graphs and Other Algorithms, we implemented a
binary heap data structure. Our implementation always made
sure that, after an element had been removed or added to a
heap, the heap order property was maintained, by using the
sink() and arrange() helper methods.
❑The heap data structure can be used to implement a sorting
algorithm called the heap sort. As a recap, let's create a simple
heap with the following items:
22
In heap sort, after deleting the last minimum element, the array will contain elements in decreasing sorting order

--- Page 23 ---
HEAP SORT ALGORITHMS
❑The heap, h, is created and the
elements in the unsorted_list are
inserted. After each method call to
insert, the heap order property is
restored by the subsequent call to
the float method. After the loop is
terminated, element 4 will be at the
top of our heap.
❑The number of elements in our heap
is 10. If we call the pop method on
the h heap object 10 times, and store
the actual elements being popped,
we end up with a sorted list. After
each pop operation, the heap is
readjusted
to
maintain
the
heap
order property.
❑The heap_sort method is as follows:
23

--- Page 24 ---
SEARCHING ALGORITHMS COMPARISONS
❑A comparison of the complexities of different sorting algorithms
is given in the following table:
24

--- Page 25 ---
THANK YOU!


---
