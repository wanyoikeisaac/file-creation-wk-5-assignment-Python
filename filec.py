# File Creation
try:
    with open('my_file.txt', 'w') as file:
        file.write('This is the first line.\n')
        file.write('This is the second line.\n')
        file.write('This is the third line.\n')
        file.write('This is the fourth line with a number: {}\n'.format(4))
        file.write('This is the fifth line with a number: {}\n'.format(5))
        file.write('This is the sixth line with a number: {}\n'.format(6))
except FileNotFoundError:
    print("FileNotFoundError: The specified file could not be found.")
except PermissionError:
    print("PermissionError: Permission denied.")
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        print("File contents:")
        print(file.read())
except FileNotFoundError:
    print("FileNotFoundError: The specified file could not be found.")
except PermissionError:
    print("PermissionError: Permission denied.")
finally:
    print("File reading completed.")

# File Appending
try:
    with open('my_file.txt', 'a') as file:
        file.write('\nThis is the first appended line.\n')
        file.write('This is the second appended line.\n')
        file.write('This is the third appended line.\n')
except FileNotFoundError:
    print("FileNotFoundError: The specified file could not be found.")
except PermissionError:
    print("PermissionError: Permission denied.")
finally:
    print("File appending completed.")