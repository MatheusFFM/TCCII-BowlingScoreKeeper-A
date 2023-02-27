from typing import List

from bowling.frame import Frame


class BowlingGame:
    game_frames = 10
    frames: List[Frame]
    bonus: Frame

    def __init__(self) -> None:
        self.frames = []
        self.bonus = None

    def add_frame(self, frame: Frame) -> bool:
        """ Add a frame to the game """
        if(len(self.frames) < self.game_frames):
            self.frames.append(frame)
            return True
        return False

    def add_frames(self, frames: List[Frame]) -> bool:
        """ Add a frame to the game """
        if(len(self.frames) + len(frames) <= self.game_frames):
            self.frames.extend(frames)
            return True
        return False

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        # To be implemented
        pass

    def is_valid_game(self) -> bool:
        """ Has all the necessaries throws """
        return len(self.frames) == self.game_frames

    def score(self) -> int:
        """ Get the score from the game """
        score = 0

        for index, frame in enumerate(self.frames):
                score = score + self.get_value(frame, index, self.frames)
        
        return score
    
    def get_value(self, frame, index, frames, comes_from_strike = False):
        if(index < len(frames)):
            if (frame.is_strike()):
                next_frame = frames[index + 1]
                if(comes_from_strike):
                    return frame.score() + next_frame.first_throw
                elif(next_frame.is_strike()):
                    return frame.score() + self.get_value(next_frame, index + 1, frames, True)
                else:
                    return frame.score() + next_frame.score()
            elif (frame.is_spare()):
                next_frame = frames[index + 1]
                return frame.score() + next_frame.first_throw
        return frame.score()

    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        # To be implemented
        pass
