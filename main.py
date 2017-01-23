#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from random import choice
from random import randint

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = open("fortunes.txt", "r")
        n_fortunes = f.read()
        f.close()
        fortunes = n_fortunes.split('\n')
        fortune = choice(fortunes)
        header = '<link type="text/css" rel="stylesheet" href="/static/css/normalize.css">'
        header += '<link type="text/css" rel="stylesheet" href="/static/css/fortune.css">'
        header += '<link rel="icon" href="/static/images/fortuneCookie.png">'
        header += '<div class="container"><h1>Fortune Cookie</h1>'
        fortuneSentence = 'Your fortune: <span class="st">' + fortune + '</span>'
        fortuneParagraph = '<p>' + fortuneSentence + '</p>'
        luckyNumber = str(randint(1,99))
        luckyNumberParagraph = '<p>Your lucky number: <span class="st">' + \
                luckyNumber + '</span></p>'
        nextFortuneButton = '<a href="."><button>Another<br>Cookie<br>Please' + \
                '</button></a></div>'
        content = header + fortuneParagraph + luckyNumberParagraph + \
                nextFortuneButton
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
