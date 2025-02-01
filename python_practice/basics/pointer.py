from ctypes import c_int, memmove, addressof, sizeof, cast, POINTER


def replace_val(var, new):
    # Create a c_int
    var = c_int(var)
    print("Original value:", var.value)

    # Create a new value
    new_value = c_int(new)
    print(f"Address of original value: {addressof(var)}")
    print(f"Address of new value value: {addressof(new_value)}")

    # Use memmove to copy the new value
    memmove(addressof(var), addressof(new_value), sizeof(c_int))

    print("Modified value:", var.value)
    print()



def replace_arr(arr, index, new_val):
    # Create a pointer to the specific array element
    ptr = cast(addressof(arr) + index * sizeof(c_int), POINTER(c_int))
    
    # Create a new value
    new_value = c_int(new_val)
    
    print("Original array:", [arr[i] for i in range(5)])

    # Use memmove to copy the new value
    memmove(addressof(ptr.contents), addressof(new_value), sizeof(c_int))

    print("Updated array:", [arr[i] for i in range(5)])

    
def main():
    # Replace var with a new value
    var = 11
    replace_val(var, 99)

    # Replace value at an index in array
    arr = (c_int * 5)(10, 20, 30, 40, 50)
    replace_arr(arr, 2, 99)
    

main()