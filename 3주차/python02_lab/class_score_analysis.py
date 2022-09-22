import pandas as pd

def read_data(filename):
    df = pd.read_csv(filename)
    data = df.values.tolist()
    return data
    # TODO

def add_weighted_average(data, weight):
    for row in data:
        row.append(row[0] * weight[0] + row[1] * weight[1]) # TODO

def analyze_data(data):
    mean = sum(data) / len(data) # TODO
    var = sum([(i - mean) ** 2 for i in data]) / len(data) # TODO
    data.sort()
    median = data[len(data) // 2] if len(data) % 2 == 1 else (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2 # TODO
    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:      # Check 'data' is valid
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0]) # 3
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')