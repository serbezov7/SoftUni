from collections import deque


def read_robots():
    robots_dict_ = {}
    robot_parts = input().split(";")
    for robot_ in robot_parts:
        name, processing_time = robot_.split("-")
        robots_dict_[name] = processing_time
    return robots_dict_


def convert_to_sec(hours, minutes, seconds):
    time_ = hours * 60 * 60 + minutes * 60 + seconds
    return time_


def read_products():
    products_ = deque()
    while True:
        product = input()
        if product == "End":
            break
        else:
            products_.append(product)
    return products_


robots_dict = read_robots()

time = [int(x) for x in input().split(":")]
time_in_seconds = convert_to_sec(time[0], time[1], time[2])

products = read_products()

processing_robots = {}

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)
    m, s = divmod(time_in_seconds, 60)
    h, m = divmod(m, 60)

    for robot in [x for x in processing_robots.keys()]:
        processing_robots[robot] -= 1
        if processing_robots[robot] == 0:
            processing_robots.pop(robot)

    current_product = products.popleft()

    for robot in robots_dict.keys():
        if robot not in processing_robots.keys():
            print(f"{robot} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            processing_robots[robot] = int(robots_dict[robot])
            break
    else:
        products.append(current_product)
