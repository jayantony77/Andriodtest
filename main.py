from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout
from analyzescreen import AnalyzeScreen, AScreen, BScreen
from scoresscreen import ScoresScreen
from scoresscreenbowl import ScoresScreenBowl
import globalvar

import csv
import os
import sys
from pathlib import Path


Window.size = 300, 600


path = os.path.dirname(os.path.abspath(__file__))
     
path = path + '/kv/'

Builder.load_file(path+"allmatches.kv")
Builder.load_file(path+"analyzescreen.kv")
Builder.load_file(path+"scoresscreen.kv")
Builder.load_file(path+"scoresscreenbowl.kv")

class MatchesItem(RelativeLayout):
    def show_matches(self):
        sm.transition.direction = 'left'
        sm.current = 'analyzeScreen'

class AllMatches(MDScreen):
    def on_pre_enter(self):
        match = MatchesItem()
        if len(self.ids.matchlist.children) < 1:
            self.ids.matchlist.add_widget(match)
    
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
        sm.add_widget(AScreen(name='ascreen'))
        sm.add_widget(BScreen(name='bscreen'))
        sm.add_widget(ScoresScreen(name='scoresScreen'))
        sm.add_widget(ScoresScreenBowl(name='scoresScreenBowl'))
        print(sm.screens)
        return sm

    def prevbatting1(self):
        sm.screens[4].ids.scorestb.cluetxt="CSK-bat"
        sm.transition.direction = 'left'
        sm.current = 'scoresScreen'
        
    def prevbowling1(self):
        sm.screens[5].ids.scorestbb.cluetxt="CSK-bowl"
        sm.transition.direction = 'left'
        sm.current = 'scoresScreenBowl'
    
    def prevbatting2(self):
        sm.screens[4].ids.scorestb.cluetxt="RCB-bat"
        sm.transition.direction = 'left'
        sm.current = 'scoresScreen'
        
    def prevbowling2(self):
        sm.screens[5].ids.scorestbb.cluetxt="RCB-bowl"
        sm.transition.direction = 'left'
        sm.current = 'scoresScreenBowl'
        

    def switch_analyze(self):
        sm.screens[1].ids.anal.matchinfo="CSK-RCB"
        sm.transition.direction = 'left'
        sm.current = 'analyzeScreen'
    
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