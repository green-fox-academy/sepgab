# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" to the StringBuilder (quote) between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

words = quote.split()
words.insert(3, "always takes longer than")
quote = ' '.join(words)

print(quote)
