# Python - More Data Structures: Set, Dictionary

### Task 101 - square_matrix_map
Write a function that computes the square value of all integers of a matrix using map

Prototype: `def square_matrix_map(matrix=[]):`
- matrix is a 2 dimensional array
- Returns a new matrix:
- Same size as matrix
- Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You have to use map
- You are not allowed to use for or while
- Your file should be max 3 lines

GitHub repository: *holbertonschool-higher_level_programming*
Directory: *python-more_data_structures*
File : [101-square_matrix_map.py](https://github.com/jgnacio/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/101-square_matrix_map.py "101-square_matrix_map.py")


### How does this return work
``` Python
    return list(map(lambda l: list(map(lambda s: s ** 2, l)), matrix))
```
***or rather... why does it work?***

---

First lets get the return out of the way and see what else is going on.

1.  The **constructor** type list():
	- `list(` ~~map(lambda l: list(map(lambda s: s ** 2, l)), matrix)~~ `)`

	The `list()` is a type constructor that coverts the map object in to a list in this case.

1.  The **map** function:
	- `map(  function , iterables, ...)`
	python map function allows you to process and modify the elements in an iterable without using an explicit for loop.
	
	The function argument can be passed any function that you have declared or already implemented in python, for example the function to calculate the absolute value of a number:
	``` Python
		numbers = [-20, -1, -507]
		absolute_list = list(map(abs, number))
		print(absolute_list)
		# Output: '[20, 1, 507]'
	```
	you dont need to use the parentheses after abs, the map function passes the elements of the list to the function.
	In this case:
	- Function is: `lambda l: list(map(lambda s: s ** 2, l))`
	which we cover below...

 	You can pass in as many iterables as you need after specifying the first one In this case:
	- Iterables is: `matrix`
	So I only need a single iterable, a list like this one:
	`matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
	which is the one with which I am going to return squared values of all elements of the nested list.
	
 	Ok the iterables are ready
but... what about the function?

1.  The **lambda** function:
	- `lambda arguments : expression`
	A lambda is a minimalistic unnamed function that you can use inside another function or even in variables. The advantage is that you dont have to declare the lambda function.
	```Python
		number = lambda x: x ** 2
		print(number(-5))
		# Output: 25
	```
	You can pass as many arguments as you want but only one expression like this:
	``` Python
	number = lambda x, y: (x * y) / 2 #Calculate the area of a triangle
	print(number(3, 19))
	# Output: 28.5
	```

 ok ok but... why a map inside a list  in the lambda function?
	
The reason is because it is a nested list so if you try to do something like this:
``` Python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_Matrix = list(map(lambda L: L ** 2, matrix))
print(new_Matrix)
```
we will encounter an error of this type:

`TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'`

but what happened?...
The interpreter does not understand because it takes an element of the matrix that is a list, and tries to calculate the square of the list, which for the interpreter is not very logical.
	
What we have to do, is to obtain each element of the "sub lists" with map and inside this map then calculate the square.
The result is:
``` python
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	new_Matrix = list(map(lambda l: map(lambda s: s ** 2, l), matrix))
	print(new_Matrix)
```

And that would be all, wouldnt it?
lets see the output:

`[<map object at 0x0000020E3AC9A890>, <map object at 0x0000020E3AC9A830>, <map object at 0x0000020E3AC9A7A0>]`

**what?** but what are all these objects?
	
The answer is not very clear to me, but roughly speaking, the map function returns what are map objects, which can be constructed as a list or as a set.

that is the reason why I put the list() after the map function
``` python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_Matrix = list(map(lambda l: list(map(lambda s: s ** 2, l)), matrix))
print(new_Matrix)
#Output: '[[1, 4, 9], [16, 25, 36], [49, 64, 81]]'
```
And that's the way i solved task 101 in my holby python adventure😁
