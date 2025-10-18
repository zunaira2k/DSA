def activity_selection(start, finish):
    n = len(start)
    # Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = []
    last_finish = 0

    for s, f in activities:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f

    return selected

start = list(map(int, input('Please enter start time: ').split()))
finish = list(map(int, input('Please enter finish time: ').split()))

result = activity_selection(start, finish)
print("Selected activities:", result)
