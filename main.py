#!/usr/bin/env python
#
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
        header = '<link type="text/css" rel="stylesheet" href="/static/css/normalize.css">'
        header += '<link type="text/css" rel="stylesheet" href="/static/css/fortune.css">'
        header += '<div class="container"><h1>Fortune Cookie</h1>'
        fortune = getRandomFortune()
        fortuneSentence = 'Your fortune: <strong>' + fortune + '</strong>'
        fortuneParagraph = '<p>' + fortuneSentence + '</p>'
        luckyNumber = randint(1,99)
        luckyNumberParagraph = '<p>Your lucky number: <strong>' + \
                str(luckyNumber) + '</strong></p>'
        nextFortuneButton = '<a href="."><button>Another Cookie Please' + \
                '</button></a>'
        content = header + fortuneParagraph + luckyNumberParagraph + \
                nextFortuneButton + "</div>"
        self.response.write(content)

def getRandomFortune():
    fortunes = [
            'There is much code in your future.',
            'You will be wealthy.',
            'You will master the environment.',
            "Expect great things and great things will come",
            "The cooler you think you are the dumber you look.",
            "Share your hapiness with others today.",
            "Your future will be happy and productive."
            ]

    return choice(fortunes)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
