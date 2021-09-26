class Win_or_Door:
    def __init__(self, width, length, ):
        self.width = width
        self.length = length

    def win_or_dor_square(self):
        win_or_dor_square = self.width * self.length
        return win_or_dor_square


class Wallpappers:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def square_wallpappers(self):
        square_wallpappers = self.width * self.length
        return square_wallpappers


class Room:
    def __init__(self, width, length, high):
        self.width = width
        self.length = length
        self.high = high
        self.win_and_door = []

    def room_square(self):
        room_square = (self.width + self.length) * self.high * 2
        return room_square

    def add_win_or_door(self, new_win_and_door):
        self.win_and_door.append(new_win_and_door)

    def work_square(self):
        work_square = self.room_square()
        for i in self.win_and_door:
            work_square -= i.win_or_dor_square()
        return work_square


print("Enter the values ​​for the width, length and height of your room:")
room = Room(float(input()), float(input()), float(input()))

print("Enter the width and height of your window:")
room.add_win_or_door(Win_or_Door(float(input()), float(input())))

print("Enter the width and height of your door:")
room.add_win_or_door(Win_or_Door(float(input()), float(input())))

print("Enter the width and length of the wallpaper roll:")
wallpappers = Wallpappers(float(input()), float(input()))

print(f"""Number of rolls of wallpaper required:
{int(room.work_square() / wallpappers.square_wallpappers())}""")
