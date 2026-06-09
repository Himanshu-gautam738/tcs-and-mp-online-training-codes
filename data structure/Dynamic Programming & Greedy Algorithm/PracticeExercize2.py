# Dynamic Programming solution for Weighted Job Scheduling

class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

def latest_non_conflict(jobs, i):
    # Find the latest job that doesn't conflict with job[i]
    for j in range(i - 1, -1, -1):
        if jobs[j].finish <= jobs[i].start:
            return j
    return -1

def job_scheduling_dp(jobs):
    # Sort jobs by finish time
    jobs.sort(key=lambda job: job.finish)
    n = len(jobs)

    # dp[i] stores max profit until job[i]
    dp = [0] * n
    dp[0] = jobs[0].profit

    for i in range(1, n):
        incl_profit = jobs[i].profit
        l = latest_non_conflict(jobs, i)
        if l != -1:
            incl_profit += dp[l]
        dp[i] = max(incl_profit, dp[i - 1])

    return dp[-1]

# Example usage
jobs = [
    Job(1, 2, 50),
    Job(3, 5, 20),
    Job(6, 19, 100),
    Job(2, 100, 200)
]

print("Maximum profit using DP:", job_scheduling_dp(jobs))
