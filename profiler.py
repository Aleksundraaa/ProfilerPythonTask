import time

stats = {}
class FunctionStats:
    def __init__(self):
        self.calls = 0
        self.total_time = 0
        self.min_time = float("inf")
        self.max_time = 0

def profiler_enter(func_id):
    start_time = time.perf_counter()
    return start_time

def profiler_exit(func_id, start_time):
    elapsed = time.perf_counter() - start_time
    s = stats.setdefault(func_id, FunctionStats())
    s.calls +=1
    s.total_time += elapsed
    s.max_time = max(s.max_time, elapsed)
    s.min_time = max(s.min_time, elapsed)

