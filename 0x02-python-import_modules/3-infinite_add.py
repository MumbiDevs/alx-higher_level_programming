#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Start the sum at 0
    result = 0
    
    # Iterate over arguments starting from the first one
    for arg in sys.argv[1:]:
        # Convert the argument to an integer and add it to the result
        result += int(arg)
    
    # Print the final result
    print(result)
