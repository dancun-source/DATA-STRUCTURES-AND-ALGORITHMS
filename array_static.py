# 1. LINEAR - STATIC (Fixed Size)
# Classification: Linear -> Static
import array as arr

# In systems, static arrays have a fixed size and type at declaration.
# Here we use the 'i' typecode for signed integers.
static_array = arr.array('i', [10, 20, 30, 40, 50])

print("--- Static Data Structure (Array) ---")
print(f"Array elements: {static_array}")
print(f"Memory address info: {static_array.buffer_info()}")
