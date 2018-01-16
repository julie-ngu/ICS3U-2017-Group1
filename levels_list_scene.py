# Created by: Julie Nguyen
# Created on: Dec 2017
# Created for: ICS3U
# This scene shows the levels

from scene import *
import ui
from level_1 import *

class LevelsListScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add background
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'green', 
                                     parent = self, 
                                     size = self.size)
                                     
        level_1_button_position = Vector2()
        level_1_button_position.x = self.screen_center_x-350
        level_1_button_position.y = self.screen_center_y
        self.level_1_button = SpriteNode('./assets/sprites/level_1_button.JPG',
                                       parent = self,
                                       position = level_1_button_position,
                                       scale = 0.3)
                                       
        level_2_button_position = Vector2()
        level_2_button_position.x = self.screen_center_x-120
        level_2_button_position.y = self.screen_center_y
        self.level_2_button = SpriteNode('./assets/sprites/level_2_button.PNG',
                                       parent = self,
                                       position = level_2_button_position,
                                       scale = 0.45)
                                           
        level_3_button_position = Vector2()
        level_3_button_position.x = self.screen_center_x+120
        level_3_button_position.y = self.screen_center_y
        self.level_3_button = SpriteNode('./assets/sprites/level_3_button.PNG',
                                       parent = self,
                                       position = level_3_button_position,
                                       scale = 0.45)
                                       
        level_4_button_position = Vector2()
        level_4_button_position.x = self.screen_center_x+350
        level_4_button_position.y = self.screen_center_y
        self.level_4_button = SpriteNode('./assets/sprites/level_4_button.PNG',
                                       parent = self,
                                       position = level_4_button_position,
                                       scale = 0.45)
                                       
        back_button_position = Vector2()
        back_button_position.x = self.screen_center_x - 440
        back_button_position.y = self.screen_center_y + 320                          
        self.back_button = SpriteNode('./assets/sprites/back_button.JPG',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.2)
    
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
        
        # if level 1 button is pressed, go to level 1 scene
        if self.level_1_button.frame.contains_point(touch.location):
            self.present_modal_scene(Level1Scene())
            
        # if back button is pressed, go to previous scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
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
    
