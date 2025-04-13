def min_drops(floors=102, eggs=7):
    # Create a DP table where dp[e][d] is the max number of floors we can check with e eggs and d drops
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

    drops = 0  # Number of drops needed
    while dp[eggs][drops] < floors:
        drops += 1
        for e in range(1, eggs + 1):
            dp[e][drops] = dp[e - 1][drops - 1] + dp[e][drops - 1] + 1

    print(f"Minimum number of drops required with {eggs} eggs and {floors} floors is: {drops}")
    return drops

# Run it
if __name__ == "__main__":
    min_drops()

