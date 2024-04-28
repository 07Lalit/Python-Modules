"""
                            PYTHON Web Browser Module
                            ------------------------

=> Provides a high-level interface which allow displaying web-based
   document to users.
   It can be used to lauch a browser in a platform-independent manner.

   1) open()
   2) open_new() : open the page in a new browser window.
   3) open_new_tab(): Open the page in  a new browser tab
   4) get() : to specify a particular browser

   chrome: 'C:/Program Files (x86)/Google/
"""

# import webbrowser
# webbrowser.open()

from webbrowser import *
#
# open('https://leetcode.com/u/La_lit07/')
# open_new('https://leetcode.com/u/La_lit07/')
#open_new_tab('https://leetcode.com/u/La_lit07/')
ch= get("C:\Program Files (x86)\Microsoft\Edge")
ch.open('google.com')