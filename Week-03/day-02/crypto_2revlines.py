# Create a method that decrypts texts/reversed_zen_lines.txt

def decrypt(file_name):
    my_file = open(file_name, "r")
    lines = []
    s=''
    message = ""
    for line in my_file:
        chars = []
        for c in line:
           chars.append(c)
        lines.append(s.join(chars[::-1]))
    message = s.join(lines)
    print(message)

decrypt("reversed-lines.txt")
