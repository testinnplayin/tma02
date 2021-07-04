# Problem: find greatest difference between any length in a list of shoe lengths and a target shoe length

# Input: shoe_lengths, a list of positive, floating-point numbers representing shoe lengths in inches
shoe_lengths = [10.0, 10.1, 10.2, 11.0, 9.8]

# Input: target_length, a positive, floating-point number representing a target shoe length in inches
target_length = 10.5

differences = []

# Sub-problem: calculate difference for each shoe_length between it and the target_length
for shoe_length in shoe_lengths:
    # Sub-problem: find the difference based on absolute value between shoe_length and target_length
    if shoe_length < target_length:
        difference = target_length - shoe_length
    else:
        difference = shoe_length - target_length
    # Sub-problem: round the difference to one decimal place
    difference = round(difference * 10) / 10

    differences = differences + [difference]

# Sub-problem: find the position of the largest difference in the list of length differences if there are any
length_of_differences = len(differences)

if length_of_differences > 0:
    largest_difference_index = 0

    # Output: largest_difference, a positive floating-point number
    for difference_index in range(1, length_of_differences):
        if differences[difference_index] > differences[largest_difference_index]:
            largest_difference_index = difference_index

    largest_difference = differences[largest_difference_index]
else:
    largest_difference = 0

print(largest_difference)
