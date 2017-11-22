#Cocktail Sort

Cocktail Sort is a variation of Bubble sort. The Bubble sort algorithm always traverses elements from left and moves the largest element to its correct position in first iteration and second largest in second iteration and so on. Cocktail Sort traverses through a given array in both directions alternatively.


## Algorithm:

Each iteration of the algorithm is broken up into 2 stages:

The first stage loops through the array from left to right, just like the Bubble Sort. During the loop, adjacent items are compared and if value on the left is greater than the value on the right, then values are swapped. At the end of first iteration, largest number will reside at the end of the array.

The second stage loops through the array in opposite direction- starting from the item just before the most recently sorted item, and moving back to the start of the array. Here also, adjacent items are compared and are swapped if required.


Example : Let us consider an example array (5 1 4 2 8 0 2)

First Forward Pass:
(5 1 4 2 8 0 2) → (1 5 4 2 8 0 2), Swap since 5 > 1
(1 5 4 2 8 0 2) → (1 4 5 2 8 0 2), Swap since 5 > 4
(1 4 5 2 8 0 2) → (1 4 2 5 8 0 2), Swap since 5 > 2
(1 4 2 5 8 0 2) → (1 4 2 5 8 0 2)
(1 4 2 5 8 0 2) → (1 4 2 5 0 8 2), Swap since 8 > 0
(1 4 2 5 0 8 2) → (1 4 2 5 0 2 8), Swap since 8 > 2

After first forward pass, greatest element of the array will be present at the last index of array.

First Backward Pass:
(1 4 2 5 0 2 8) → (1 4 2 5 0 2 8)
(1 4 2 5 0 2 8) → (1 4 2 0 5 2 8), Swap since 5 > 0
(1 4 2 0 5 2 8) → (1 4 0 2 5 2 8), Swap since 2 > 0
(1 4 0 2 5 2 8) → (1 0 4 2 5 2 8), Swap since 4 > 0
(1 0 4 2 5 2 8) → (0 1 4 2 5 2 8), Swap since 1 > 0

After first backward pass, smallest element of the array will be present at the first index of the array.

Second Forward Pass:
(0 1 4 2 5 2 8) → (0 1 4 2 5 2 8)
(0 1 4 2 5 2 8) → (0 1 2 4 5 2 8), Swap since 4 > 2
(0 1 2 4 5 2 8) → (0 1 2 4 5 2 8)
(0 1 2 4 5 2 8) → (0 1 2 4 2 5 8), Swap since 5 > 2

Second Backward Pass:
(0 1 2 4 2 5 8) → (0 1 2 2 4 5 8), Swap since 4 > 2

Now, the array is already sorted, but our algorithm doesn’t know if it is 
completed. The algorithm needs to complete this whole pass without any swap to know it is sorted.
(0 1 2 2 4 5 8) → (0 1 2 2 4 5 8)
(0 1 2 2 4 5 8) → (0 1 2 2 4 5 8)


[Cocktail Sort Pseudocode](cocktail_sort_pseudocode.png)


###Solutions
[Amelia's Explanation](https://github.com/adowns01/Intro-to-Whiteboarding-DBC/blob/master/solutions/cocktail_sort_solution_amelia.md)
