#
##Author: Radhey Ruparel
##Description: A program based gif that displays a landscape into a graphical canvas 
##and allows the user to control the perspective of the landscape by moving the mouse. 
##The perspective seems to change due to an effect called motion parallax.
#

#Importing all the modules for the program execution  
import sys
import os 
import random #Importing the random module

#Important code for using graphics.py
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

#This helps to create motion parallax
def mouse_motion_control(graphics_ui): 
    
    '''This function, return mouse graphics function to all the other functions required and the 
    shapes in motion. The graphics_ui is a graphic varaibles (gui) and parameter varaibles for this funtion'''
    
    x_mouse = (graphics_ui.mouse_x)#This makes the graphics move using the mouse on the x-axis
    y_mouse = (graphics_ui.mouse_y)#This makes the graphics move using the mouse on the y-axis
    return x_mouse, y_mouse #In now returns to all the fuctions, in which this function is called

def sun(graphics_ui):
    '''This fucntion creates the Sun on the right top corner and gives it prallax ability 
    graphic The graphics_ui is a graphic varaibles (gui) and parameter varaibles for this funtion'''
    
    #The mouse function is called to give motion to the graphical objects in this function
    x_mouse, y_mouse=mouse_motion_control(graphics_ui)
    x_mouse=(x_mouse/40)-18 #Motion pallax ability for graphics in the x-axis
    y_mouse=(y_mouse/40)-18 #Motion pallax ability for graphics in the y-axis
    
    graphics_ui.ellipse(510+x_mouse,100+y_mouse,100,100,'yellow') #An yellow big circle on the right top corner
    
def grass_and_tree(graphics_ui):
    
    '''This fucntion creates grass and tree on the bottom of cancvas and gives them the prallax ability 
    graphic The graphics_ui is a graphic varaibles (gui) and parameter varaibles for this funtion'''
    
    #The mouse function is called to give motion to the graphical objects in this function
    x_mouse, y_mouse=mouse_motion_control(graphics_ui)
    x_mouse=(x_mouse/7)-100 #Motion pallax ability for graphics in the x-axis
    y_mouse=(y_mouse/7)-100#Motion pallax ability for graphics in the y-axis
    
    color_string_grass=graphics_ui.get_color_string(42,253,132) #This makes a specific green color string for the grass
    graphics_ui.rectangle(x_mouse-100,y_mouse+600,1200,200,color_string_grass) #This print the land mass of green grass

    
    grass_index=0 #Managing number of grass object is printed  
    x_coord_grass=-100 #so the printing starts from 100 pixels outside of the canvas
    while grass_index<300: #So it can print 300 rectangle grass objects
        graphics_ui.rectangle(x_mouse+x_coord_grass,y_mouse+570,3,30,color_string_grass)
        x_coord_grass+=6 #For the next rectangle to printed after 6 pixels
        grass_index+=1 #To fail the loop
    
    color_string_tree_base=graphics_ui.get_color_string(163,43,45) #This makes a specific brown color string for tree truck
    graphics_ui.rectangle(x_mouse+510,y_mouse+575,30,100,color_string_tree_base) #This prints the tree truck
    
    color_string_tree_top=graphics_ui.get_color_string(15,126,17) #This makes a specific green color string for tree 
    graphics_ui.ellipse(x_mouse+525,y_mouse+550,80,125,color_string_tree_top) #This prints the 
    

#Declaring the main function  
def main():
    
    gui=graphics(700,700,'Landscape') #This makes the canvas for the landscape
    
    
    flag=0 #As the loop should only when the one condition is fullfiled 
    while flag==0:
        
        red_left_mount = random.randint(0, 255) #Redness of the left mountain
        green_left_mount = random.randint(0, 255) #Greeness of the left mountain
        blue_left_mount = random.randint(0, 255) #Blueness of the left mountain 
        COLOR_STRING_LEFT_MOUNT = gui.get_color_string(red_left_mount, green_left_mount, 
        blue_left_mount) #The color string for the left mountain
        
        red_right_mount = random.randint(0, 255) #Redness of the right mountain
        green_right_mount = random.randint(0, 255) #Greeness of the right mountain
        blue_right_mount = random.randint(0, 255) #Blueness of the right mountain 
        COLOR_STRING_RIGHT_MOUNT = gui.get_color_string(red_right_mount, green_right_mount, 
        blue_right_mount) #The color string for the right mountain
        
        
        red_middle_mount = random.randint(0, 255) #Redness of the middle mountain
        green_middle_mount = random.randint(0, 255) #Greeness of the middle mountain
        blue_middle_mount = random.randint(0, 255) #Blueness of the left mountain 
        COLOR_STRING_MIDDLE_MOUNT = gui.get_color_string(red_middle_mount, green_middle_mount, 
        blue_middle_mount) #The color string for the right mountain
        
        if (not COLOR_STRING_MIDDLE_MOUNT==COLOR_STRING_LEFT_MOUNT and not COLOR_STRING_MIDDLE_MOUNT==COLOR_STRING_RIGHT_MOUNT and
        not COLOR_STRING_RIGHT_MOUNT==COLOR_STRING_LEFT_MOUNT): #In order ensure the random generation of color string is not same of any two mountians
            flag=1 #Hence this will fail the string 

    while True: #An Infinte for the motion till the user closes the window
        
        x_coord_birds=-600 #Birds path starts outside of the canvas
        y_coord_birds=100 #First Birds vertical on the horizontal path 
        
        #This loop makes the five set of birds move a horizontal path on particular vertical position
        while x_coord_birds<800: #Repeat the seqencae as the birds goes outside of the canvas
            
            gui.clear() #Clearing all the frame animation to happen
            
            #This prints the blue sky background
            gui.rectangle(-100,-100,900,900,'sky blue') 
            
            #This prints the sun by calling the sun function, by giving gui graphical variable 
            sun(gui) 
            
            #The mouse function is called to give motion to the middle mountain
            x_mouse, y_mouse=mouse_motion_control(gui)
            x_mouse=(x_mouse/30)-23 #Motion pallax ability for graphics in the x-axis
            y_mouse=(y_mouse/30)-23#Motion pallax ability for graphics in the y-axis
            
            #This prints the middle mountian in the landscape
            gui.triangle(350+x_mouse,200+y_mouse,100+x_mouse,700+y_mouse,600+x_mouse,
            700+y_mouse,COLOR_STRING_MIDDLE_MOUNT)
            
            #The mouse function is called to give motion to left and right mountain
            x_mouse, y_mouse=mouse_motion_control(gui)
            x_mouse=(x_mouse/18)-39 #Motion pallax ability for graphics in the x-axis
            y_mouse=(y_mouse/18)-39 #Motion pallax ability for graphics in the y-axis
            
            #This prints the left mountian in the landscape
            gui.triangle(150+x_mouse,250+y_mouse,-100+x_mouse,600+y_mouse,400+x_mouse,
            600+y_mouse, COLOR_STRING_LEFT_MOUNT)
            
            #This prints the right mountian in the landscape
            gui.triangle(550+x_mouse,250+y_mouse,300+x_mouse,600+y_mouse,800+x_mouse,
            600+y_mouse, COLOR_STRING_RIGHT_MOUNT)
            grass_and_tree(gui)
            
            #As we need 5 birds
            number_of_birds=5
            
            #This loop main for formation and printing of the five birds
            while number_of_birds>0:
                #This prints the right side of all the five birds
                gui.line((x_coord_birds+60+(number_of_birds*100)),(y_coord_birds+(number_of_birds*20)),(x_coord_birds+30+(number_of_birds*100)),(y_coord_birds+(number_of_birds*20)+10),'black')
                #This prints the lefts side of all the five birds
                gui.line((x_coord_birds+(number_of_birds*100)),(y_coord_birds+(number_of_birds*20)),(x_coord_birds+30+(number_of_birds*100)),(y_coord_birds+(number_of_birds*20)+10),'black')
                number_of_birds-=1 #To fail the loop responsible for the formation of the birds
            x_coord_birds+=5 #To fail the loop reponsible for the horizontal motion of 5 sets of birds
            gui.update_frame(50) #Updating the frame for the animation
    pass

#Calling the main function
main()