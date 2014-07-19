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

The initial change.util.combinations function was completely recursive. It would recurse in the subtraction
from the total amount, and in traversing the list of input integers. I like solutions like these
because if the language supports something like Tail Recursion, it can optimize away the
seemingly inefficient, yet more elegant code

This is a problem in cases where you have something like this:
```
    coins = [1, 5, 10, 25]
    change = 1000
```
The final combination of ways to make change is a list of 1's in this case,
and it would recurse 1000 times to perform this. It's easily optimized out by taking advantage of python's
[1] * 1000, and then remove that total sum from the input to the next call to helper() removes basically
997 calls to that function (1000 - 3 attempts via 5, 10, 25 being tried first).

Therefore the combinations function can take an input of 1000 unique integers. There is no currency
I know of that has support for this # of unique denominations.

I thought about trying a more efficient approach to ```ChangeMaker.count_change(#)```, but due to the
recursion limit in python, combinations only recurses 1000 times, and realistically will only be called
~10 times in a real world scenario?

Please put up the code on your GitHub account and provide a README on how to run your program along with the time and space complexity discussion mentioned above.

Also, please write this in Python 2.7, if possible -- we are part of the 98% that use it. ;)

Thanks! We really look forward to seeing what you come up with.

Also, please feel free to ask me any questions.
