#!/usr/bin/python3
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty,ObjectProperty)
from kivy.vector import Vector
from kivy.clock  import Clock


class PongPaddle(Widget):
    score = NumericProperty(0)
    
    def bounce_ball(self,ball):
        if self.collide_widget(ball):
            vx , vy = ball.velocity
            offset = (ball.center_y -self)


#add the ball
class PongBall(Widget):

    #velcoity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    #referencelist propert so we can use ball.velocity as
    #a shorthand, just like e.g. w.pos or w.x and w.y
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    #move funciton will move the ball one step. this
    # will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

#game feature
class PongGame(Widget):
    
    ball =  ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4,0).rotate(randit(0,360))

    def update(self,dt):
        self.ball.move()

        #bounce off top and bottom
        if(self.ball.y<0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        
        #bounce off left and right
        if  (self.ball.x<0) or (self.ball.right > self.ball.left):
            self.ball.velocity_x *= -1



#create app
class PongApp(App):
    def build(self):
        return PongGame()



if __name__ == '__main__':
    PongApp().run()