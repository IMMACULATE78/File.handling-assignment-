# file_read_write.py

def modify_text(text):
    # Example modification: Convert text to uppercase
    return text.upper()

try:
    with open("input.txt", "r") as infile:
        content = infile.read()

    modified_content = modify_text(content)

    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("File has been read, modified, and written successfully.")

except FileNotFoundError:
    print("The input file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
