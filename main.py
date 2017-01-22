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

fortunes = [
        "Don't eat any Chinese food today or you be sick!",
        "Don't panic",
        "Everything will be ok. Don't obsess.",
        "Expect great things and great things will come.",
        "Give person fish, he eat for day. Teach person to fish, he always smell funny.",
        "He who dies with most toys, still dead.",
        "If you can read this, you are literate. Congratulations.",
        "If you drive like hell, you'll get there faster.",
        "It could be better, but it's good enough.",
        "It's up to you to clearify.",
        "Let's finish this up now, someone is waiting for you on that.",
        "Life is a sexually transmitted terminal condition.",
        "Marriage lets you annoy one special person for the rest of your life",
        "Share your hapiness with others today.",
        "Stop eating now. Food poisoning no fun.",
        "The best year-round temperature comes from a warm heart and a cool head",
        "The cooler you think you are the dumber you look.",
        "The finest men like the finest steels have been tempered in the greatest heat.",
        "The fortune you seek, is in another cookie",
        "There is much code in your future.",
        "Time will prove you right, you must stay where you are.",
        "Two days from now, tomorrow will be yesterday.",
        "You are cleverly disguised as responsible adult.",
        "You will be wealthy.",
        "You will die alone and poorly dressed.",
        "You will find a thing. It may be important.",
        "You will master your environment.",
        "You will think for yourself when you stop letting others think for you.",
        "You will find a bushel of money",
        "You will soon have an out of money experience.",
        "Your future will be happy and productive.",
        "Your smile will tell you what makes you feel good.",
        "Your reality check is about to bounce.",
        "When chosen for jury duty, tell judge fortune cookie say 'guilty!'"
        ]


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<link type="text/css" rel="stylesheet" href="/static/css/normalize.css">'
        header += '<link type="text/css" rel="stylesheet" href="/static/css/fortune.css">'
        header += '<div class="container"><h1>Fortune Cookie</h1>'
        fortune = choice(fortunes)
        fortuneSentence = 'Your fortune: <strong>' + fortune + '</strong>'
        fortuneParagraph = '<p>' + fortuneSentence + '</p>'
        luckyNumber = str(randint(1,99))
        luckyNumberParagraph = '<p>Your lucky number: <strong>' + \
                luckyNumber + '</strong></p>'
        nextFortuneButton = '<a href="."><button>Another<br>Cookie<br>Please' + \
                '</button></a></div>'
        content = header + fortuneParagraph + luckyNumberParagraph + \
                nextFortuneButton
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
