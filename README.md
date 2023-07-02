# Python-Problem-Solving
:star: **1-Two_Sum**
Intially, using no data structure, but iterating over the list twice. Used the enumerate function, to get both index and element from the list.
This function returns an object of the [enumerate](https://docs.python.org/3/library/functions.html#enumerate) class, which is 
basically, like a list of tuples `[(index, element), (next_index, next_element)]`.
Skipping where the indexes match.
Since, the worst case is where, we might have to iterate across both lists, we have
n: length of nums
\n:watch: Time Complexity: O(n*n) = O(n<sup>2</sup>)
\n:black_circle: Space Complexity: O(n)

The optimized version of the function involved finding the difference between the target the element.
Initializing the dictionary, if the difference was found in the dictionary {element: index}, then we returned the element of the
index of the value of the dictionary that matched our difference and the current index.
n: length of nums
\n:watch: Time Complexity: O(n)
\n:black_circle: Space Complexity: O(n)
***********************************************************************************************