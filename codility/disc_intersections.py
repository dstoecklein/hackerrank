class DiscLog():
    def __init__(self, x, start_end) -> None:
        self.x = x # x pos where disc starts
        self.start_end = start_end

def solution(arr):
    discHistory = []
    for i in range(len(arr)):
        discHistory.append(DiscLog(i - arr[i], 1)) # start of disc
        discHistory.append(DiscLog(i + arr[i], -1)) # end of disc
    discHistory.sort(key=lambda d: (d.x, -d.start_end)) # negative for descending order
    intersections = 0
    active_intersections = 0

    for log in discHistory:
        active_intersections += log.start_end
        if log.start_end > 0:
            intersections += active_intersections - 1
        if intersections > 10000000:
            return -1
    return intersections

print(solution([1,5,2,1,4,0]))