def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def binary_to_text(binary_str):
    text_result = ''.join(chr(int(binary, 2)) for binary in binary_str.split(' '))
    return text_result



print("1.Text To Binary")
print("2.Binary to Text")
opt = input("Enter choice: ")
if opt == "1":
    input_text = input("Enter text: ")
    binary_representation = text_to_binary(input_text)
    print(f'Text to Binary: {binary_representation}')
elif opt == "2":
    input_Binary = input("Enter Binary code: ")
    converted_text = binary_to_text(input_Binary)
    print(f'Binary to Text: {converted_text}')
else:
    print("Invalid input!")
