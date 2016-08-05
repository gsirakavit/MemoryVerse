import string
from random import randint

verses = ['Blessed is the man who does not walk in the counsel of the wicked or stand in the way of sinners or sit in the seat of mockers. But his delight is in the law of the LORD, and on his law he meditates day and night. He is like a tree planted by streams of water, which yields its fruit in season and whose leaf does not wither. Whatever he does prospers. Not so the wicked! They are like chaff that the wind blows away. Therefore the wicked will not stand in the judgment, nor sinners in the assembly of the righteous. For the LORD watches over the way of the righteous, but the way of the wicked will perish.',
'Teacher, which is the greatest commandment in the law? Jesus replied, Love the Lord your God with all your heart and with all your soul and with all your mind. This is the first and greatest commandment.', 
'All Scripture is God-breathed and is useful for teaching, rebuking, correcting, and training in righteousness, so that the man of God may be thoroughly equipped for every good work.', 
'Do not let this Book of the Law depart from your mouth; meditate on it day and night, so that you may be careful to do everything written in it. Then you will be prosperous and successful.']
refs = ['Psalms 1:1-6',
'Matthew 22:36-38', 
'2 Timothy 3:16-17', 
'Joshua 1:8']

# Create a dictionary using a comprehension - this maps every character from
# string.punctuation to None. Initialize a translation object from it.
def std_text(s):
    translator = str.maketrans({key: None for key in string.punctuation})
    s = s.translate(translator)
    s = s.lower()
    return s

def verse_check(i):
    verses[i] = std_text(verses[i])
    response = input("\nEnter the text for {}:\n".format(refs[i]))
    response = std_text(response)
    if response == verses[i]:
        return print("You got this!\n")
    else:
        bwords = set(verses[i].split(' '))
        ywords = set(response.split(' '))
        words = bwords & ywords
        progress = round(len(words)/len(bwords) * 100, 1)
        return print("\nYou are {}% done with memorizing this verse. You need to practice more!\nCompare the NIV translation of the Bible to what you typed.\n{}\n".format(progress, verses[i]))

task = input("Press 1 to review all verses OR\nPress 2 to review the last verse OR\nPress 3 to review a particular verse OR\nPress 4 or any other random key to review a random verse\nEnter your selection: ")
if task == '1':
    for j in range(0,len(verses)):
        verse_check(j)
elif task == '2':
    j = len(verses) - 1
    verse_check(j)
elif task == '3':
    j = int(input("Which verse would you like to review? Select a verse between 0 and {}: ".format(len(verses)-1)))
    if j >= 0 and j < len(verses):
        verse_check(j)
    else:
        print("Bad input! Try again.")
else:
    j = randint(0, len(verses)-1)
    verse_check(j)