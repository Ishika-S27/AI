## chap 1 
# import pyjokes

# print("Printing jokes..")
# jokes = pyjokes.get_joke()
# print(jokes)

# so thanks 
# that was my program 

# practice set 

""""
print(''' 
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, Twinkle, Little Star | Nursery Rhyme For Kids With ...
Twinkle, twinkle, little star,
How I wonder what you are!
When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Twinkle, Twinkle Little Star Lyrics | Kid Song Lyrics ...
Twinkle, twinkle, little star,
How I wonder what you are!
Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go
If you did not twinkle so?
Twinkle, twinkle, little star,
How I wonder what you are! ''')

"""

'''
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
'''

import os 

directory_path = '/New folder'
contents = os.listdir(directory_path)

for item in contents:
    print(item)