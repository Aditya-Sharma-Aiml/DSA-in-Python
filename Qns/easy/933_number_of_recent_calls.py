class RecentCounter:

    def __init__(self):
        self.queue = []  # Queue to store timestamps of requests
        self.first_req_time = -1  # Timestamp of the first request

    def ping(self, t: int) -> int:
        # Add the current timestamp to the queue
        self.queue.append(t)

        # Remove requests older than 3000 milliseconds from the beginning of the queue
        while self.queue and self.queue[0] < t - 3000:
            self.queue.pop(0)

        # Update the timestamp of the first request if necessary
        if self.first_req_time == -1:
            self.first_req_time = t

        # Return the current number of requests within the past 3000 milliseconds
        return len(self.queue)