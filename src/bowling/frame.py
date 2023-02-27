class Frame:
    strike_value = 10

    def __init__(self, first_throw: int, second_throw: int) -> None:
        self.first_throw = self.verify_max_min_throw(first_throw)
        self.second_throw = self.verify_max_min_throw(second_throw) if not self.is_strike() else 0

    def verify_max_min_throw(self, throw):
        if(throw > 10):
            return 10
        if(throw < 0):
            return 0
        return throw

    def score(self) -> int:
        """ The score of a single frame """
        return self.first_throw + self.second_throw

    def is_strike(self) -> bool:
        """ Return whether the frame is a strike or not """
        return self.first_throw == self.strike_value

    def is_spare(self) -> bool:
        """ Return whether the frame is a spare or not """
        return (not self.is_strike()) and (self.first_throw + self.second_throw == self.strike_value)

    def is_last_frame(self) -> bool:
        """ Return whether the frame is a last frame of the game """
        # To be implemented
        pass

    def bonus(self) -> int:
        """ Bonus throw """
        # To be implemented
        pass
