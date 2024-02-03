def badge_maker(name):
    badge = f'Hello, my name is {name}.'
    return badge

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = badge_maker(name)
        badges.append(badge)
    return badges

def assign_rooms(names):
    rooms = []
    # loop through rooms to assign names
    for i in range(0, 8):
        if len(names) < i:
            exit
        else:
            rooms.append(f'Hello, {names[i]}! You\'ll be assigned to room {i + 1}!')
    return rooms

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    badges_and_rooms = badges + rooms
    for item in badges_and_rooms:
        print(item)
    
    return None
