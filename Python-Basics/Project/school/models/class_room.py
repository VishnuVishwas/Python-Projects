# class_room.py

class ClassRoom:

    # list of class rooms present
    list_of_class_room = {
        "100": ["8th std", 'A sec'],
        "101": ["8th std", 'B sec'],
        "102": ["9th std", 'A sec'],
        "103": ["9th std", 'B sec'],
        "104": ["10th std", 'A sec'],
        "105": ["10th std", 'B sec']
    }

    def __init__(self, class_id: str, capacity: str) -> None:
        self.class_id = class_id
        self.capacity = capacity
        self.grade = self.list_of_class_room[class_id][0]
        self.section = self.list_of_class_room[class_id][1]

    # dispaly classroom info
    def display_class_room_info(self):
        print(f"\nDetails of classroom:\nClass ID: {self.class_id}\nCapacity: {self.capacity}\nGrade: {self.grade}\nSection: {self.section}")

if __name__ == '__main__':
    room = ClassRoom('100', '500')
    room.class_room_info()