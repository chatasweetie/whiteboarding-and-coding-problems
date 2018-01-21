#Pyramid Array

Write the method #present_in_pyramid? that takes a value and a pyramid array and returns true if the value is in the pyramid array. 
The beginning of a pyramid array has ascending numbers, the end has descending numbers. 

Example: 
```ruby
p_array = [ 1, 3, 4, 5, 7, 9, 7, 5, 5, 3, 0, -10]   
present_in_pyramid?(0, p_array) #=> true    
present_in_pyramid?(100, p_array) #=> false    
```

Don’t use the language's array lookup methods. Yes, you can loop over the whole array, but how can you make it more efficient than that?


###Solutions 

- [Jessica's Solution V1 - Python2.7](https://github.com/chatasweetie/whiteboarding-and-coding-problems/blob/master/questions/pyramid_array/solution/pyramid_array.py)
- [Jessica's Solution V2 - Python2.7](https://github.com/chatasweetie/whiteboarding-and-coding-problems/blob/master/questions/pyramid_array/solution/pyramid_array_index.py)