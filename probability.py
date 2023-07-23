import copy
import random
# Consider using the modules imported above.
class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_to_draw):
        if num_balls_to_draw >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        else:
            drawn_balls = random.sample(self.contents, num_balls_to_draw)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful_experiments = 0

    for _ in range(num_experiments):
        copied_hat = copy.deepcopy(hat)  # Create a deep copy of the original hat to avoid modifying the original
        drawn_balls = copied_hat.draw(num_balls_drawn)

        # Check if the drawn balls contain at least the expected number of each color
        is_successful = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                is_successful = False
                break

        if is_successful:
            num_successful_experiments += 1

    probability = num_successful_experiments / num_experiments
    return probability

