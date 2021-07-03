import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for col, num in kwargs.items():
            for i in range(num):
                self.contents.append(col)
    
    def draw(self, num):
        if num >= len(self.contents): 
            return self.contents
        
        hand = []
        for i in range(num):
            pick = random.choice(self.contents)
            hand.append(pick)
            self.contents.remove(pick)
        return hand
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for i in range(num_experiments):
        success = True
        clone_hat = copy.deepcopy(hat)
        draw_balls = {}
        for ball in clone_hat.draw(num_balls_drawn):
            draw_balls[ball] = draw_balls.get(ball, 0) + 1
        
        for col, num in expected_balls.items():
            if num > draw_balls.get(col, 0):
                success = False
        
        if success: num_success += 1

    return num_success / num_experiments



