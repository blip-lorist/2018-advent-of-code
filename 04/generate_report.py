with open("sorted_timestamps.txt", "r") as f:
    logs = f.readlines()

logs = [x.strip() for x in logs]

print("Date\tID\tMinute")
minute_tens_string = "0"*10 + "1"*10 + "2"*10 + "3"*10 + "4"*10 + "5"*10
minutes_string = "0123456789"*6
print("\t\t{}".format(minute_tens_string))
print("\t\t{}".format(minutes_string))

guard_id = None
start_sleep_minute = None
current_guard_sleep_ranges = []
for log in logs:
    if "begins shift" in log:
        shift_log = log.split(" ")
        if guard_id != shift_log[3]:
            # log previous guard
            sleep_graph = ["."] * 60
            for sleep_range in current_guard_sleep_ranges:
                sleep_minute_count = len(sleep_range)
                first_minute = sleep_range[0]
                last_minute = sleep_range[-1]
                sleep_range_visual = sleep_minute_count * ["#"]
                sleep_graph[first_minute:last_minute + 1] = sleep_range_visual

            sleep_graph = "".join(sleep_graph)
            print("\t{}\t{}".format(guard_id, sleep_graph))
            guard_id = shift_log[3]
            current_guard_sleep_ranges = []
            continue

    if "falls asleep" in log:
        sleep_log = log.split(" ")
        start_sleep_minute = int(sleep_log[1].split(":")[1].replace("]", ""))

    if "wakes up" in log:
        sleep_log = log.split(" ")
        end_sleep_minute = int(sleep_log[1].split(":")[1].replace("]", ""))
        sleep_range = range(start_sleep_minute, end_sleep_minute)
        current_guard_sleep_ranges.append(sleep_range)
