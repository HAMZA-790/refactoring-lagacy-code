def compute_stats(filename):
    """
    Read numbers from a file and compute statistics.

    Args:
        filename: Path to the file containing numbers (one per line)
    """
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file if line.strip()]

        if not numbers:
            print("No data found in file")
            return

        total = len(numbers)
        summation = sum(numbers)
        average = round(summation / total)
        minimum = min(numbers)
        maximum = max(numbers)

        print(f"total = {total}")
        print(f"summation = {summation}")
        print(f"average = {average}")
        print(f"Minimum = {minimum}")
        print(f"Maximum = {maximum}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except ValueError as e:
        print(f"Error: Invalid number format in file - {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    compute_stats("random_nums.txt")