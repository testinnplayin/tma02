# Problem: calculate UK shoe sizes from foot lengths

# Input: foot_lengths, a list of foot lengths in inches that are positive floating-point numbers from 7.67 to 12.0
foot_lengths = [7.67, 7.8, 9.4, 9.5, 9.6, 11.9, 11.95, 12.0]

# Output: shoe_sizes, a list of shoe sizes that are positive floating-point numbers from 0.0 to 13.0.
shoe_sizes = []

# Sub-problem: convert foot length to rough shoe size
for foot_length in foot_lengths:
    rough_shoe_size = (foot_length * 3) - 23

    # Sub-problem: round rough shoe size up to nearest 0.5
    shoe_size = round(rough_shoe_size * 2) / 2
    shoe_sizes = shoe_sizes + [shoe_size]

print(shoe_sizes)
