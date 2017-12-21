# Created by: Julie Nguyen
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the levels

from scene import *
import ui


class LevelsListScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'green', 
                                     parent = self, 
                                     size = self.size)
                                     
        #self.level_1_button = SpriteNode('./assets/sprites/FILENAME.png',
                                       #parent = self,
                                       #position = self.size/2(change to 3),
                                       #scale = 0.75)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
