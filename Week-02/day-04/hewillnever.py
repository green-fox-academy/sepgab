# Things are a little bit messed up
# Your job is to decode the notSoCrypticMessage by using the hashmap as a look up table
# Assemble the fragments into the out variable

out = "";
notSoCrypticMessage = [1, 12, 1, 2, 11, 1, 7, 11, 1, 49, 1, 3, 11, 1, 50, 11]

hashmap = [
    {7: "run around and desert you"},
    {50: "tell a lie and hurt you"},
    {49: "make you cry,"},
    {2: "let you down"},
    {12: "give you up,"},
    {1: "Never gonna"},
    {11: "\n"},
    {3: "say goodbye"}
]
draft = out.split()
message = []

for i in range(0, len(notSoCrypticMessage)-1, 1):
    message.append(str(notSoCrypticMessage[i]))

print(message)

for value in range(0, len(message)-1, 1):
    message[value] = hashmap[value[value]]

print(message)
