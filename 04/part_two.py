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



guard_worst_minute = {}
for guard_id, histogram in guard_minutes_hist.items():
    sorted_hist = sorted(histogram.items(), key=lambda kv: kv[1])
    if len(sorted_hist) == 0:
        continue
    worst_minute = sorted_hist[-1]
    guard_worst_minute[guard_id] = worst_minute

sorted_worst = sorted(guard_worst_minute.items(), key=lambda kv: kv[1][1])
worst_guard = sorted_worst[-1]
guard_id = worst_guard[0]
print(guard_id)
worst_min = worst_guard[1][0]
print(worst_min)

