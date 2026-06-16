from constraint import Problem, BacktrackingSolver


def read_input():
    num_families = int(input())
    families = {}
    for _ in range(num_families):
        name, size, reqs_string = input().split()
        reqs = reqs_string.split('-')
        families[name] = {'size': int(size), 'requirements': reqs}
    num_rooms = int(input())
    rooms = {}
    for _ in range(num_rooms):
        room_id, capacity, amenities_string = input().split()
        floor = room_id[0]
        amenities = amenities_string.split('-')
        rooms[int(room_id)] = {'floor': int(floor), 'capacity': int(capacity), 'amenities': amenities}
    return families, rooms


def room_fits_guest(room_id, guest_name, families, rooms):
    """Returns True if the given room satisfies all requirements of the guest."""
    if room_id is None:
        return True  # rejection is always structurally valid (checked separately)
    room = rooms[room_id]
    guest = families[guest_name]
    # Room must have enough capacity
    if room['capacity'] < guest['size']:
        return False
    # Room must provide every amenity the guest requires
    for req in guest['requirements']:
        if req not in room['amenities']:
            return False
    return True


def find_valid_rooms(guest_name, families, rooms):
    """Returns the list of room IDs that can accommodate this guest."""
    return [
        room_id for room_id in rooms
        if room_fits_guest(room_id, guest_name, families, rooms)
    ]


if __name__ == '__main__':
    families, rooms = read_input()
    guest_names = list(families.keys())

    problem = Problem(solver=BacktrackingSolver())

    for name in guest_names:
        valid_rooms = find_valid_rooms(name, families, rooms)
        domain = valid_rooms + [None]  # None means the guest is rejected
        problem.addVariable(name, domain)

    for i in range(len(guest_names)):
        for j in range(i + 1, len(guest_names)):
            name_a = guest_names[i]
            name_b = guest_names[j]
            problem.addConstraint(
                lambda room_a, room_b: not (room_a is not None and room_a == room_b),
                (name_a, name_b)
            )


    def no_unjustified_rejection(rejected_guest, *other_assignments,
                                 valid_rooms_for_rejected=None):
        if rejected_guest is not None:
            return True

        occupied = set(other_assignments)
        for room_id in valid_rooms_for_rejected:
            if room_id not in occupied:
                return False
        return True


    for name in guest_names:
        valid_rooms = find_valid_rooms(name, families, rooms)
        if not valid_rooms:
            continue
        other_guests = [g for g in guest_names if g != name]
        if not other_guests:
            problem.addConstraint(
                lambda assigned: assigned is not None,
                [name]
            )
            continue
        problem.addConstraint(
            lambda rejected, *others, vr=valid_rooms:
            no_unjustified_rejection(rejected, *others, valid_rooms_for_rejected=vr),
            [name] + other_guests
        )

    solutions = problem.getSolutions()  # Ne menuvaj! Do not modify!


    def total_people(solution):
        return sum(
            families[guest]['size']
            for guest, room in solution.items()
            if room is not None
        )


    best = max(solutions, key=total_people) if solutions else None

    print("Best assignment:")
    if best:
        assigned = [(room, guest) for guest, room in best.items() if room is not None]
        assigned.sort(key=lambda x: x[0])
        for room_id, guest_name in assigned:
            print(f"{guest_name}->{room_id}")