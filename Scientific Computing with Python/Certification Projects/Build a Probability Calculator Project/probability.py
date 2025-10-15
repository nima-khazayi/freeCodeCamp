import copy
import random

class Hat:
    def __init__(self, **balls):
        """Initialize the hat with variable number of colored balls."""
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """Draw num_balls randomly from the hat without replacement."""
        if num_balls >= len(self.contents):
            # If requested more than available, return all balls
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        drawn_balls = random.sample(self.contents, num_balls)
        # Remove drawn balls from contents
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Estimate probability of drawing expected_balls from the hat."""
    success_count = 0
    
    for _ in range(num_experiments):
        # Make a deep copy of the hat to avoid modifying the original
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        
        # Check if all expected balls are in drawn
        success = True
        for color, count in expected_balls.items():
            if drawn.count(color) < count:
                success = False
                break
        if success:
            success_count += 1
    
    probability = success_count / num_experiments
    return probability
