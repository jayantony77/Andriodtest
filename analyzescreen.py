from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFillRoundFlatButton


sm = ScreenManager()
class AnalyzeScreen(MDScreen):
    def on_pre_enter(self):
        print("Printing...",self.ids.anal.matchinfo)
       
        with open("D:/Cricket/KivyMD-master/demos/AndriodFresh/prediction.txt", "r") as f:
            #self.ids.code_input.font_name="D:/Cricket/KivyMD-master/demos/AndriodFresh/Montserrat-Regular.ttf"
            #self.ids.code_input.font_name="D:/Cricket/KivyMD-master/demos/AndriodFresh/LibreBaskerville-Regular"
            self.ids.ascr.ids.code_input.text= f.read()
            print("In Analyze Screen")

        cluetext = str(self.ids.anal.matchinfo)
        team1 = cluetext.partition("-")[0]
        team2 = cluetext.partition("-")[2]        
        if len(self.ids.bscr.ids.matcard.children) < 1:
            matchcrd = MatchCard()
            matchcrd.ids.match1but.text= team1+ " previous batting and Bowling"
            matchcrd.ids.match1but_bat.text= team1+ " prev bat"
            matchcrd.ids.match1but_bowl.text= team1+ " prev bowl"
            self.ids.bscr.ids.matcard.add_widget(matchcrd)

            matchcrd1 = MatchCard1()
            matchcrd1.ids.match2but.text= team2+ " previous batting and Bowling"
            matchcrd1.ids.match2but_bat.text= team2+ " prev bat"
            matchcrd1.ids.match2but_bowl.text= team2+ " prev bowl"
            self.ids.bscr.ids.matcard.add_widget(matchcrd1)



        

class AScreen(MDScreen, ModalView):
    pass
class BScreen(MDScreen):
    pass

class CScreen(MDScreen):
    def on_press(self, text):
        if text == "bat":
            self.ids.img.source= "battingheavy.jpg"
        if text == "bal":
            self.ids.img.source= "balancedteam.jpg"
        if text == "bowl":
            self.ids.img.source= "bowlingheavy.jpg"
        
class MatchCard(MDCard):
    pass
class MatchCard1(MDCard):
    pass

class RoundFlatToggleButton(MDFillRoundFlatButton):
    pass
