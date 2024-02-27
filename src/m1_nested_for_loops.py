# Received assistance from Josh

###############################################################################
# Done: 1. (3 pts)
#
#   For this _TODO_, write a block of code that uses a nested for loop to print
#   the following output:
#
#   Outer: 1
#   Inner: 1
#   Inner: 2
#   Inner: 3
#   Outer: 2
#   Inner: 1
#   Inner: 2
#   Inner: 3
#
#   Notice how the outer loop will repeat twice and the inner loop will repeat
#   3 times. Do NOT "hard-code" the numbers that should print. You should use the indexes of the
#   for loops to determine what number to print.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

for x in range(2):
    print(f"Outer: {x+1}")

    for y in range(3):
        print(f"Inner: {y+1}")


###############################################################################
# Done: 2. (4 pts)
#
#   For this _TODO_, write a function called many_triangles() that takes two
#   parameters:
#       - num_of_triangles    <-- int
#       - size                <-- int
#
#   where *num_of_triangles* is the number of triangles of stars that get printed and *size* is the size of each triangle.
#
#   So, if the function is called like this:
#   
#       many_triangles(2, 3)
#
#   it would print this:
#
#   *
#   **
#   ***
#   *
#   **
#   ***
#
#   Notice how this time we are creating triangles, we do *NOT* have a blank line as the first line of the triangle.
#
#   Also, write a line of code that calls your function with whatever numbers you would like.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def many_triangles(num_of_triangles, size):
    for x in range(num_of_triangles):
        for y in range(size):
            print((y+1) * "*")
many_triangles(2,3)

