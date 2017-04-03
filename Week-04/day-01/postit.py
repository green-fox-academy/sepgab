class PostIt():
    def __init__(self):
        self.background_color = 'white'
        self.text = ''
        self.text_color = 'black'

postit_1 = PostIt()
postit_1.background_color = 'orange'
postit_1.text = 'Idea 1'
postit_1.text_color = 'blue'

postit_2 = PostIt()
postit_2.background_color = 'pink'
postit_2.text = 'Awesome'
postit_2.text_color = 'black'

postit_3 = PostIt()
postit_3.background_color = 'yellow'
postit_3.text = 'Superb!'
postit_3.text_color = 'green'

print ('Background: ' + postit_1.background_color + ', Text: ' + postit_1.text + ', Text color: ' + postit_1.text_color)
print ('Background: ' + postit_2.background_color + ', Text: ' + postit_2.text + ', Text color: ' + postit_2.text_color)
print ('Background: ' + postit_3.background_color + ', Text: ' + postit_3.text + ', Text color: ' + postit_3.text_color)
