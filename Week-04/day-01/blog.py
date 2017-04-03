class BlogPost:
    def __init__(self, author, title, text, date):
        self.author_name = str(author)
        self.title = str(title)
        self.text = str(text)
        self.publication_date = str(date)

class Blog:
    def __init__(self, num=10):
        self.set = []

    def add(self, blogpost):
        self.set.append(blogpost)

    def delete(self, num):
        self.set.remove(self.set[int(num-1)])

    def update(self, num, blogpost):
        self.set.remove(self.set[int(num-1)])
        self.set.append(blogpost)

    def __str__(self):
        result = ""
        for i in range(0, len(self.set)):
            result += str(i+1) + ". Author: " + str(self.set[i].author_name) + "\n   Title: " + str(self.set[i].title) + "\n   Text: " + str(self.set[i].text) + "\n   Publication date: " + str(self.set[i].publication_date) + "\n"
        return result

blogpost_1 = BlogPost('John Doe', 'Lorem Ipsum', 'Lorem ipsum dolor sit amet.', '2000.05.04.')

blogpost_2 = BlogPost('Tim Urban', 'Wait but why', 'A popular long-form, stick-figure-illustrated blog about almost everything.', '2010.10.10.')

blogpost_3 = BlogPost('William Turton', 'One Engineer Is Trying to Get IBM to Reckon With Trump.', 'Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.', '2017.03.28.')

blog = Blog()

blog.add(blogpost_1)
blog.add(blogpost_2)
blog.add(blogpost_3)

print(blog)

blog.delete(1)

print(blog)

blog.update(2, blogpost_1)

print(blog)
