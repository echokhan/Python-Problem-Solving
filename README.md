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
:watch: Time Complexity: O(1)\
:black_circle: Space Complexity: O(n)
***********************************************************************************************

:star: **3- ValidAnagram**
The overall approach of my first solution was in the right direction. Unfortunately, rather than just comparing the length of each string, I proceeded to add each string's letters to separate dictionaries and compared the keys. 
Similarly, rather than just using a count method in the string, I iterated over the string and incremented until I found the frequency of each letter, which I used later to compare for each respective letter.

A better form of my solution was just comparison of the length of strings and using a set find the unique elements and compare the frequency of each using [str.count()](https://python-reference.readthedocs.io/en/latest/docs/str/count.html#:~:text=str.%20count(sub%5B%2C%20start%5B%2C%20end%5D%5D)) method.

Of course, a very elegant solution here is just sorting each string and comparing them. The time-complexity will then depend on the sorting algorithm that we use. The average case time complexity of Tim sort (the algo in sorted() function) is O(n log n).

The first one has Time complexity of O(s), considering we have to iterate over entire set of any one of the strings. 
s: length of set of string\
n: length of string\
:watch: Time Complexity: O(s)\
:black_circle: Space Complexity: O(n)
***********************************************************************************************

:star: **4- Group Anagrams**
The first approach was to derive from the previous problem of (ValidAnagrams)[https://github.com/echokhan/Python-Problem-Solving/blob/main/3-%20ValidAnagram.py]. However, using that along with my unoptimized code, the solution passed 111/118 test cases before a time limit error. I was going through the entire list, in a nested for loop comparing each string with the other, which might was extremely inefficient, on top of the approach to find anagrams by comparing frequency of each letter.

A better form of my solution was just collecting each string in a list of keys, which were created using a sorted string. A big help was the use of (defaultdict)[https://docs.python.org/3/library/collections.html#collections.defaultdict:~:text=Using%20list%20as%20the%20default_factory%2C%20it%20is%20easy%20to%20group%20a%20sequence%20of%20key%2Dvalue%20pairs%20into%20a%20dictionary%20of%20lists%3A]. This default value, helped avoid adding additional checks. After all strings were added to values in the dictionary, we appending each as a list to create a list of lists. The sort, using tim sort had a time-compexity of nlogn, where n is the length. This would result in a time complexity of O(m*nlogn), where m is the total number of strings in the list.

Another solution, which was apparently supposed to be faster, was very simlar to the above. The same collection of keys from the list of strings. However, rather than using a sorted function, and getting a tuple, we tried to create a list of frequency of each letter, by finding relative unicode for each letter. Of course, this list was converted later to tuple. The runtime of the above timesort solution was lesser. The time-complexity of this solution is O(m*n).
***********************************************************************************************

:star: **5- topKFrequent**
Finding the frequency was a straightforward approach of finding the frequency of each element in the list (nums). After that, we have two lists, which we can zip together either using the function (zip())[https://docs.python.org/3/library/functions.html#zip] or creating a list of tuples based on similar indices.
In my solution, I used a lamba function as key to sort the list tuples and then extract the first element from the tuple (nums element), while restricting till k elements.
The second solution, was an interpretation of neetcode. There were two main things to be done.
The first was finding frequency of each element in the list (nums) using a dictionary. The second was creation of count_array which was to be a list of sublists/buckets each of which was to be populated by the elements of list(nums), at positions/indices which were the same as the frequency of the element values in nums.
Then we iterate over the count_array in a descending order, ignoring the empty buckets and collecting values in count_array, returning the topK elements depending on the value of k.
***********************************************************************************************

:star: **6- productExceptSelf**
The first approach was to simply find product of all elements, skipping the element on position i.
This was unoptimized. O(n2)

Then we tried to find product of elements, slicing the lists as per the position i. Again, it was unoptimized. O(n2)

Then, I saw how everyone on leetcode and neetcode was using two different iterations to populate lists (left_pass (prefix)
and right_pass(suffix)), finding cumulative products and multiplying both for each position i. This was O(3n) = O(n),
which was a little more optimized. I understood why we were doing this, however, frankly, it was a tricky one for me.
I think of it like this. 
Given `nums = [a, b, c, d]`
Then answer or the resulting list would be `[b*c*d, a*c*d, a*b*d, a*b*c]`
The left_pass, after left to right iteration gives `[1, a, a*b, a*b*c]`
The right_pass, after right to left iteration gives `[b*c*d, c*d, d, 1]`
Produt of left_pass[i] and right_pass[i] would give us the above result. So cumulative product does make sense in this way.
***********************************************************************************************