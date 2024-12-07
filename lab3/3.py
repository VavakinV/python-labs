def can_divide_videos(n, k, durations):
    total_sum = sum(durations)

    if total_sum % k != 0:
        return "Нет"
    
    target = total_sum // k
    current_sum = 0
    post_count = 0
    lengths = []
    
    for duration in durations:
        current_sum += duration
        post_count += 1

        if current_sum > target:
            return "Нет"

        if current_sum == target:
            lengths.append(post_count)
            post_count = 0
            current_sum = 0
            
    if post_count == 0:
        return "Да\n" + ' '.join(map(str, lengths))
    else:
        return "Нет"

def process_file(filename):
    with open(filename) as f:
        first_line = f.readline().strip()
        N, K = map(int, first_line.split())
        durations = list(map(int, (f.readline().strip().split())))
    
    return N, K, durations

n, k, durations = process_file("lab3/videos.txt")

result = can_divide_videos(n, k, durations)
print(result)
