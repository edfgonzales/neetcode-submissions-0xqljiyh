class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # count, time
        time = 0
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt < 0:
                    q.append((cnt, time + n))
            
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time