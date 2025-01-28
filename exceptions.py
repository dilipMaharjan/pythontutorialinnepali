try:
    f = open("nonexistent_file.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    if 'f' in locals() and not f.closed:
        f.close()