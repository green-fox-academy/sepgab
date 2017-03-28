# Create a method that decrypts texts/encoded_zen_lines.txt

def decrypt(file_name):
    my_file = open(file_name, "r")
    chars = []
    s=''
    message = ""
    for line in my_file:
        for c in line:
           chars.append(c)
    for i in range(0, len(chars)):
        if chars[i] != ' ' and chars[i] != '\n':
            chars[i] = chr(ord(chars[i]) - 1)
    message = s.join(chars)
    print(message)

decrypt("encoded-lines.txt")
