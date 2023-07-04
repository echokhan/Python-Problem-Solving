## Python-Problem-Solving

:star: **1-Two_Sum**
Intially, using no data structure, but iterating over the list twice. Used the enumerate function, to get both index and element from the list.
The `enumerate` function returns an object of the [enumerate](https://docs.python.org/3/library/functions.html#enumerate) class, which is 
basically, like a list of tuples `[(index, element), (next_index, next_element)]`.
Skipping where the indexes match.
Since, the worst case is where, we might have to iterate across both lists, we have
n: length of nums\
:watch: Time Complexity: O(n*n) = O(n<sup>2</sup>)\
:black_circle: Space Complexity: O(n)

The optimized version of the function involved finding the difference between the target the element.
Initializing the dictionary, if the difference was found in the dictionary {element: index}, then we returned the element of the
index of the value of the dictionary that matched our difference and the current index.
n: length of nums\
:watch: Time Complexity: O(n)\
:black_circle: Space Complexity: O(n)
***********************************************************************************************

:star: **2- containsDuplicate**
My first solution is where I derived the use of a dictionary from the previous problem. There were two overkills in this approach.
Use of a dictionary and finding frequency of occurence of each unique element, within the list. This, I later realised was not required.
It did pass the tests though.

The second solution was a little closer to what was required, and I did not compute the frequency of each unique element in the list.
However, I should also have replaced the dictionary with another data structure, as I had no need of the values in the dictionary, just the keys.

In the third solution, I remembered not using any data structure at all.
Intially, using no data structure, but iterating over the list twice. Used the enumerate function, to get both index and element from the list. I tried to use the same approach, as in the previous problem, keeping it simple.
The enumerate function returns an object of the [enumerate](https://docs.python.org/3/library/functions.html#enumerate) class, which is 
basically, like a list of tuples `[(index, element), (next_index, next_element)]`.
Skipping where the indexes match.
Comparing values and returning `True` in case of a match. Returning false if no return occurs during the loop.
Since, the worst case is where, we might have to iterate across both lists, we have
n: length of nums\
:watch: Time Complexity: O(n*n) = O(n<sup>2</sup>)\
:black_circle: Space Complexity: O(n)

Going back to the use of a data structure, this time, we avoid using a dictionary as we only need the keys (the uniqueness) and not the values for the frequency of each element. Therefore, we use a set, with a similar solution to the second one.

Lastly, we could either collect/append all elements of the list within a set and check for a second occurence, or simply compare length of the set of the list with the length of the list, which would help us determine a duplication of elements. Finding the length of any list is time complexity O(1) [List - Get Length](https://wiki.python.org/moin/TimeComplexity). However, we have another structure (set) using extra space, therefore O(n) as space complexity
n: length of nums\
:watch: Time Complexity: O(1)
:black_circle: Space Complexity: O(n)
***********************************************************************************************