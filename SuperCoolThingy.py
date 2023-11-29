# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:44:13 2023

@author: mural
"""
import pygame, simpleGE

class Game(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
        #initialize background to yellow
        self.background.fill((214, 195, 235))
        
        self.addLabels()
        self.addButton()
        self.addMultiLabel()
        
        self.sprites = [self.lblTitle, self.label,
                        self.lblButton, self.button,
                        self.multi]
    
    def addLabels(self):
        self.lblTitle = simpleGE.Label()
        self.lblTitle.font = pygame.font.Font("PepperidgeScript.otf", 40)
        self.lblTitle.text = "War, but with Tarot"
        self.lblTitle.center = (320, 40)
        self.lblTitle.size = (400, 40)
        
        self.label = simpleGE.Label()
        self.label.font = pygame.font.Font("Fancy Delight.ttf", 40)
        self.label.text = "BY: Jackie H"
        self.label.fgColor = (0xCC, 0x00, 0x00)
        self.label.bgColor = (214, 195, 235)
        self.label.center = (320, 100)
        self.label.size = (200, 60)
        
    def addButton(self): 
        self.lblButton = simpleGE.Label()
        self.lblButton.center = (200, 180)
        self.lblButton.text = "Button"
        
        self.button = simpleGE.Button()
        self.button.center = (450, 180)
        self.button.text = "don't click me"
    
    def addMultiLabel(self):
        self.multi = simpleGE.MultiLabel()
        self.multi.textLines = [
            "This is a multiline text box.",
            "It's useful when you want to",
            "put larger amounts of text",
            "on the screen. Of course, you",
            "can change the colors and font."
            ]
        self.multi.size = (400, 200)
        self.multi.center = (320, 370)
        
    def update(self):        
        if self.button.clicked:
            self.lblButton.text = "Ouch!"
            self.background.fill((214, 195, 235))
            self.screen.blit(self.background, (0, 0))
        

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
    