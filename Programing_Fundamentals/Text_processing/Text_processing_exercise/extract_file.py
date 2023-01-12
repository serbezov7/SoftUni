some_text = input().split("\\")
file_name, extension = some_text[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {extension}")