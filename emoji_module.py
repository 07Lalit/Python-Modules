"""
                       Emoji module in python
                       ---------------------

1) Every emoji has a unicode associated with it .
2) Emojis also have a CLDR short name , which can also be used .
3) From the list of unicodes. replace "+" with "000".

    ex-: "U+1F600" will become "U0001F600" and prefix the unicode with
    "\" and print it .
4) Install pip install emoji .
EMOJI_ALIAS_UNICODE

emojize(':xyz_uujp:') : Requires the CLDR short name and  returns the corres
ponding emoji. replace the spaces with underscore in CLDR short name

"""
print(chr(128512))
print('\U0001F600')
import emoji

print(emoji.EMOJI_DATA.keys())
print()
print(emoji.emojize(':face_with_tears_of_joy:',language='en'))
print(emoji.emojize(':face_blowing_a_kiss:'))
print(emoji.emojize(':winking_face_with_tongue:'))