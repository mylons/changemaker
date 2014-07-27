## Usage
#### Checkout and setup with virtualenv
* Written against python 2.7.5
* You can, of course, skip the virtualenv stuff if you just want to install the packages
```
git clone https://github.com/mylons/changemaker.git
cd changemaker
virtualenv --python=python2.7 venv
source venv/bin/activate
pip install -r requirements.txt
py.test tests.py
```
#### Interactive session
```
~/changemaker(branch:master) » python
Python 2.7.5 (default, Feb 19 2014, 13:47:28)
[GCC 4.8.2 20131212 (Red Hat 4.8.2-7)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from change.util import ChangeMaker
>>> cm = ChangeMaker([5, 25, 10, 1])
>>> cm.change(8)
[[5, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
```


## Problem Statement: Change Maker

* Implement a class named ChangeMaker that takes a list of coin denominations in the constructor:
```
>>> cm = ChangeMaker([25, 10, 5, 1])
```
* In ChangeMaker, write two functions called change() and count_change() 
  * Each of which takes as an argument the amount to be changed. 
  * The first function, change(), returns the combinations of the coins that can be used to sum up
    to the amount:
```
>>> cm.change(8)
[[5, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
```
* With the coin denominations 25, 10, 5, and 1, the amount 8 can be made up of one 5 and three 1's, or eight 1's. There are only two ways to make up an amount of 8 with those denominations. 
* Order does not matter in the results, so [5, 1, 1, 1] and [1, 5, 1, 1] are not two different combinations.
* If the amount given can not be made using the denominations, return an empty list []:
```
>>> cm = ChangeMaker([25, 10, 5])
>>> cm.change(8)
[]
```
* The second function, count_change(), returns only the number of such combinations:
```
>>> cm = ChangeMaker([25, 10, 5, 1])
>>> cm.count_change(8)
2
>>> cm = ChangeMaker([25, 10, 5])
>>> cm.count_change(8)
0
```
* The solution should be generalized to work with any denominations of coins (i.e., not typical currency denominations):
```
>>> cm = ChangeMaker([2, 1])
>>> cm.change(3)
[[2, 1], [1, 1, 1]]
>>> cm.count_change(3)
2
>>> cm.change(4)
[[2, 2], [2, 1, 1], [1, 1, 1, 1]]
>>> cm.count_change(4)
3
```
* Assume that the ChangeMaker class will always be given lists of positive integers without any repeated elements,
* Also assume that the amount to be changed will always be an integer >= 0.
* Attempt to provide as efficient a solution as possible, and discuss the time and space complexity.

## Discussion on run time and complexity

#### General Design
I chose to be minimalistic in my approach to this. The problem states returning primitives and 
built in data structures instead of built types. 

#### Recursion 
I decided to do change() recursively, because it's an interview question, you have to show off a little bit.

The initial combinations function was completely recursive, and actually a greedy implementation:
 ( https://github.com/mylons/changemaker/commit/97b3d9de257e9987c1932e27afc8015df3686c86 ). 
It would recurse in the subtraction from the total amount, and in traversing the list of input integers. I like 
solutions like these because if the language supports something like Tail Recursion, it can optimize away the
seemingly inefficient, yet more elegant code. However, a greedy implementation wont satisfy an exhaustive list of all
change combinations.

Python also doesn't support Tail Recursion, and maybe never will: http://neopythonic.blogspot.com.au/2009/04/tail-recursion-elimination.html

The official advice is to move to an iterative solution if you're traversing large lists. Doing that would allow
this solution to expand, but it would expand outside of the problem domain, in my opinion. Sort of like over optimizing
for the sake of optimization.


#### Algorithm, Run Time and Efficiency Discussion
The current implementation of ```_combinations()``` will attempt to generate every possible combination of coins, 
with repeats, until the sum of the amount to change is achieved. Once such a solution exists, it's yielded. I chose to
use generators to assist in the recursion limits in python, and to use less of a memory footprint in the 
```_combinations()``` function. ```change()``` will still create all of the solution lists, in the worst case. 
This solution is potentially O(N^2*M), due to the complexity of generating all of the lists. The first for loop 
yielding coin_combo's is going to create the base case (eventually):
a list of [1, 1,...1], and every other possibility of a repeated coin list. 
There are some early iteration termination cases that should reduce the search space: 
* sum of the current list of coins is the desired amount
* sum has exceeded the current amount
* there are no more coins to attempt (worst case)

The memory required is going to be proportional to the depth of the recursion. Each recursive call to helper copies the
coin list, and also creates a new list in the first call. The recursion is going to be exponential as pointed out above,
therefore the memory will be too.

The run time of ```ChangeMaker.count_change(amount)``` is, at the worst case, O(N*M). The function iterates over each 
coin (N), and then over a range from coin value to the end of the list, which is amount + 1 and (M). There is no extra
space required in memory, except amount + 1 integers.

I decided on a more efficient approach to ```ChangeMaker.count_change(#)```, due to the
limitations of the existing ```change()``` function. change() can't realistically be used for very very large amounts
of change, but count_change() can, so long as O(N*M) is acceptable run time.
