from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.card import MDCard
from Aandp import AnalyzeScreen
from kivy.properties import StringProperty

import csv
import os
import sys
from pathlib import Path

##File last modified 08-03-21 at 12:43 pm


Window.size = (300,600)

"""
KV_DIR = f"{os.path.dirname(__file__)}/kv/"

for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        print(kv_file)
        Builder.load_string(kv.read())
"""
Builder.load_file("allmatches.kv")
Builder.load_file("aandp.kv")

          
class Matches(MDCard):
    def show_matches(self):
        sm.transition.direction = 'left'
        sm.current = 'analyzeScreen'


class AllMatches(MDScreen):
    def on_pre_enter(self):
        match1 = Matches()
        self.ids.matchlist.add_widget(match1)
        
    
class FirstScreen(MDScreen):
    pass

class All(MDScreen):
    pass

#took screemanager out to accomadate logic in show_matches of MDCard
sm = ScreenManager()
class FirstScreen1(MDApp):
    ttfpath = StringProperty()
    cimagepath = StringProperty()
    bimagepath = StringProperty()

    def build(self):
        sm.add_widget(AllMatches(name='allmatches'))
        sm.add_widget(AnalyzeScreen(name='analyzeScreen'))
        return sm
    #below code was in build method
    """
    path = os.path.dirname(os.path.abspath(__file__))
        ttfpath = path + "\\ttf\\"
        print("ttfpath ==",ttfpath)
        cimagepath = path + "\\images\\csk.jpg"
        bimagepath = path + "\\images\\rcb.jpg"
        print("imagepath ==",cimagepath)
        print("imagepath ==",bimagepath)
    """

FirstScreen1().run()