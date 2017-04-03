# Create a BlogPost class that has
# an authorName
# a title
# a text
# a publicationDate

# Create a few blog post objects:
# "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
# Lorem ipsum dolor sit amet.
# "Wait but why" titled by Tim Urban posted at "2010.10.10."
# A popular long-form, stick-figure-illustrated blog about almost everything.
# "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
# Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.

class BlogPost():
    def __init__(self):
        self.author_name = ''
        self.title = ''
        self.text = ''
        self.publication_date = ''

blogpost_1 = BlogPost()
blogpost_1.author_name = 'John Doe'
blogpost_1.title = 'Lorem Ipsum'
blogpost_1.text = 'Lorem ipsum dolor sit amet.'
blogpost_1.publication_date = '2000.05.04.'

blogpost_2 = BlogPost()
blogpost_2.author_name = 'Tim Urban'
blogpost_2.title = 'Wait but why'
blogpost_2.text = 'A popular long-form, stick-figure-illustrated blog about almost everything.'
blogpost_2.publication_date = '2010.10.10.'

blogpost_3 = BlogPost()
blogpost_3.author_name = 'William Turton'
blogpost_3.title = 'One Engineer Is Trying to Get IBM to Reckon With Trump.'
blogpost_3.text = 'Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.'
blogpost_3.publication_date = '2017.03.28.'

print(blogpost_1.author_name)
