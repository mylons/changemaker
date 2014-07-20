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
built in data structures instead of built types. Also, since the logic of the combinations function
is geared towards a list input of integers, and a sum to achieve, it seems pretty specific to the 
change problem. It is written in a way that the function could be graduated to it's own
module/class, etc.

#### Recursion 
I decided to do this recursively, because it's an interview question. You have to show off a little bit,
if you can. This in turn exposed something I rarely run into in python, the recursion limit! Also, this 
is one of those classic problems that lends itself well to a recursive solution. IFF the problem statement
required a large number of coins as input, would I have considered doing it iteratively.

The initial combinations function was completely recursive ( https://github.com/mylons/changemaker/commit/97b3d9de257e9987c1932e27afc8015df3686c86 ). It would recurse in the subtraction
from the total amount, and in traversing the list of input integers. I like solutions like these
because if the language supports something like Tail Recursion, it can optimize away the
seemingly inefficient, yet more elegant code.

This is a problem in cases where you have something like this:
```
    coins = [1, 5, 10, 25]
    change = 1000
```
The final combination of ways to make change is a list of 1's in this case,
and it would recurse 1000 times to perform this. It's easily optimized out by taking advantage of python's
[1] * 1000, and then remove that total sum from the input to the next call to ```_combinations()``` removes basically
997 calls to that function (1000 - 3 attempts via 5, 10, 25 being tried first).

Therefore the combinations function can take an input of ~500-900 unique integers, depending on the change to calculate. 
There is no currency I know of that has support for this number of unique denominations. Therefore, I'm assuming
this is OK. 

Python doesn't support Tail Recursion, and maybe never will: http://neopythonic.blogspot.com.au/2009/04/tail-recursion-elimination.html

The official advice is to move to an iterative solution if you're traversing large lists. Doing that would allow
this solution to expand, but it would expand outside of the problem domain, in my opinion. Sort of like over optimizing
for the sake of optimization.
#### Run Time and Efficiency
The run time of ```ChangeMaker.count_change(amount)``` is, at the worst case, O(n^2), where n is the number of coins. 
I say this because, count_change loops over the coins, and for each coin calls combinations, which in turn iterates
over each coin. So, there is some set of inputs (like using the max number of coins, and then the max amount of change) 
that will force this behavior, but n^2 is an upper bound, and 
even then the number of executions is somewhere in the ballpark of <1,000,000 due to the recursion limit.

I thought about trying a more efficient approach to ```ChangeMaker.count_change(#)```, but due to the
recursion limit, combinations can only recurse 1000 times, and realistically will only be called
~10 times in a real world scenario?

I also copy the ```ChangeMaker._coins``` list in the call to ```_combinations()```. The reason for this
is that you can use the list as a stack in the ```_combinations()``` function which makes 
managing handling the coins much simpler. This, again, shouldn't be a huge cost because the list is only
going to be <1000 integers. 

The space requirements will grow linearly with the amount of change to return.

I thought empirical testing would be interesting to see how the memory grows.  
```
>>> import sys
>>> cm = ChangeMaker([i for i in range(1, 998)])
>>> a = cm.change(900)
>>> sys.getsizeof(a)
7992
>>> a = cm.change(450)
>>> sys.getsizeof(a)
3768
>>> 3768.0 / 7992.0 
0.47147147147147145
```
It seems to grow slightly less than linear! 



