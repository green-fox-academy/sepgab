# Create a method that decrypts texts/reversed_zen_lines.txt

def decrypt(file_name):
    my_file = open(file_name, "r")
    chars = []
    s=''
    message = ""
    for line in my_file:
       for c in line:
           chars.append(c)
    message = s.join(chars[::-1])
    print(message)

decrypt("reversed-lines.txt")
