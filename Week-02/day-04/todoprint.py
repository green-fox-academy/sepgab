# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todoText = " - Buy milk\n"
words = todoText.split('\n')
words.insert(0, "My todo:")
words.insert(2, " - Download games")
words.insert(3, "    - Diablo")
todoText = '\n'.join(words)

print(todoText)
