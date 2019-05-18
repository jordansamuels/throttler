from collections import deque


class Throttle:
    def __init__(self, max_messages, time_window):
        self.time_window = time_window
        self._d = deque([], maxlen=max_messages)

    def accept(self, t):
        while len(self._d) > 0 and self._d[0] + self.time_window <= t:
            self._d.popleft()
        if len(self._d) < self._d.maxlen:
            self._d.append(t)
            return True
        else:
            return False




