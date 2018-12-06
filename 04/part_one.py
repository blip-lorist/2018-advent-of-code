from collections import Counter
with open("sleep_graph.txt","r") as f:
    sleep_graphs = f.readlines()

sleep_graphs = [x.strip() for x in sleep_graphs]

minutes_asleep = Counter()
guard_minutes_hist = {}
for sleep_graph in sleep_graphs:

    guard_id, graph = sleep_graph.split("\t")
    guard_id = guard_id.strip()
    sleep_count = graph.count("#")
    minutes_asleep[guard_id] += sleep_count
    graph = list(graph)
    if guard_id in guard_minutes_hist.keys():
        minutes_histogram = guard_minutes_hist[guard_id]
    else:
        minutes_histogram = Counter()

    for idx, minute in enumerate(graph):
        if minute == "#":
            minutes_histogram[idx] += 1

    guard_minutes_hist[guard_id] = minutes_histogram



sorted_minutes = sorted(minutes_asleep.items(), key=lambda kv: kv[1])
sleepiest_guard = sorted_minutes[-1][0]
print(sleepiest_guard)
histogram = guard_minutes_hist[sleepiest_guard]
sorted_hist = sorted(histogram.items(), key=lambda kv: kv[1])
most_freq_minute = sorted_hist[-1][0]
print(most_freq_minute)

