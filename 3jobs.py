def printJobScheduling(arr, t):
    # Sort jobs by descending profit
    arr.sort(key=lambda x: x[2], reverse=True)
    n = len(arr)
    result = [False] * t  # To keep track of free time slots
    job = ['-1'] * t      # To store result (sequence of jobs)
    # Iterate through all given jobs
    for i in range(n):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
    print("🧾 Following is the maximum profit job sequence:")
    print(" → ".join(job))
# Driver code
if __name__ == "__main__":
    arr = [
        ['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]
    ]
    printJobScheduling(arr, 3)

