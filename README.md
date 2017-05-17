# Determine the number of bits to flip to convert int a to int b.

## Constraints
* Can we assume A and B are always ints? - Yes
* Is the output an int? - Yes
* Can we assume A and B are always the same number of bits? - Yes
* Can we assume the inputs are valid (not None)? - No
* Can we assume this fits memory? - Yes


## Algorithm
We can use the xor operator to determine the bit differences between a and b

* Set count to 0
* Set c to a xor b
* Loop while c != 0:
    * Increment count if the LSB in c is a 1
        * We can check this by using a mask of 1
    * Right shift c by 1
* Return the count