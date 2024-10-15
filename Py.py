import csv
import statistics
import math
from scipy.stats import kendalltau, spearmanr

def read_text_file(file_path):
    """Reads the entire content of a text file."""
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def read_csv_file(file_path):
    """Reads a CSV file and returns the data as a list of rows."""
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def calculate_mean(data):
    """Calculates the mean of the data."""
    return sum(data) / len(data)

def calculate_median(data):
    """Calculates the median of the data."""
    return statistics.median(data)

def calculate_mode(data):
    """Calculates the mode of the data."""
    return statistics.mode(data)

def calculate_std_dev(data):
    """Calculates the standard deviation of the data."""
    return statistics.stdev(data)

def calculate_variance(data):
    """Calculates the variance of the data."""
    return statistics.variance(data)

def calculate_range(data):
    """Calculates the range of the data."""
    return max(data) - min(data)

def calculate_correlation_coefficient(data1, data2):
    """Calculates the Pearson correlation coefficient between two datasets."""
    if len(data1) != len(data2):
        raise ValueError("Datasets must have the same length for correlation.")
    return statistics.correlation(data1, data2)

def add(data):
    """Returns the sum of the data."""
    return sum(data)

def subtract(data):
    """Subtracts all subsequent numbers from the first number in the data."""
    if not data:
        raise ValueError("Data list is empty.")
    return data[0] - sum(data[1:])

def multiply(data):
    """Returns the product of the data."""
    result = 1
    for num in data:
        result *= num
    return result

def divide(data):
    """Divides the first number by each of the subsequent numbers in the data."""
    if not data:
        raise ValueError("Data list is empty.")
    result = data[0]
    try:
        for num in data[1:]:
            result /= num
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero encountered in data.")
    return result

def kendall_correlation(data1, data2):
    """Calculates the Kendall Tau correlation coefficient between two datasets."""
    if len(data1) != len(data2):
        raise ValueError("Datasets must have the same length for Kendall correlation.")
    return kendalltau(data1, data2)[0]

def spearman_correlation(data1, data2):
    """Calculates the Spearman rank-order correlation coefficient between two datasets."""
    if len(data1) != len(data2):
        raise ValueError("Datasets must have the same length for Spearman correlation.")
    return spearmanr(data1, data2)[0]

def write_to_csv_file(file_path, data):
    """Appends a row of data to a CSV file."""
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def display_menu():
    """Displays the calculator menu."""
    print("\nWelcome to the Math Operation Calculator")
    print("*****************************************")
    print("| 1. Addition                          |")
    print("| 2. Subtraction                       |")
    print("| 3. Multiplication                    |")
    print("| 4. Division                          |")
    print("| 5. Mean                              |")
    print("| 6. Median                            |")
    print("| 7. Mode                              |")
    print("| 8. Standard Deviation                |")
    print("| 9. Variance                          |")
    print("|10. Range                             |")
    print("|11. Correlation Coefficient           |")
    print("|12. Kendall Correlation               |")
    print("|13. Spearman Correlation              |")
    print("|14. Exit                              |")
    print("*****************************************")

def main():
    input_text_file_path = 'input.txt'
    output_csv_file_path = 'output.csv'

    try:
        text_data = read_text_file(input_text_file_path)
        # Assuming the input file has two lines: first for data1 and second for data2
        lines = text_data.strip().split('\n')
        if len(lines) < 2:
            raise ValueError("Input file must contain at least two lines of data.")
        data = [float(x) for x in lines[0].split()]
        data2 = [float(x) for x in lines[1].split()]
    except FileNotFoundError:
        print(f"Error: The file '{input_text_file_path}' was not found.")
        return
    except ValueError as ve:
        print(f"Error processing input file: {ve}")
        return

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                result = add(data)
                print(f"Addition: {result}")
                write_to_csv_file(output_csv_file_path, [f"Addition: {result}"])

            elif choice == "2":
                result = subtract(data)
                print(f"Subtraction: {result}")
                write_to_csv_file(output_csv_file_path, [f"Subtraction: {result}"])

            elif choice == "3":
                result = multiply(data)
                print(f"Multiplication: {result}")
                write_to_csv_file(output_csv_file_path, [f"Multiplication: {result}"])

            elif choice == "4":
                result = divide(data)
                print(f"Division: {result}")
                write_to_csv_file(output_csv_file_path, [f"Division: {result}"])

            elif choice == "5":
                result = calculate_mean(data)
                print(f"Mean: {result}")
                write_to_csv_file(output_csv_file_path, [f"Mean: {result}"])

            elif choice == "6":
                result = calculate_median(data)
                print(f"Median: {result}")
                write_to_csv_file(output_csv_file_path, [f"Median: {result}"])

            elif choice == "7":
                result = calculate_mode(data)
                print(f"Mode: {result}")
                write_to_csv_file(output_csv_file_path, [f"Mode: {result}"])

            elif choice == "8":
                result = calculate_std_dev(data)
                print(f"Standard Deviation: {result}")
                write_to_csv_file(output_csv_file_path, [f"Standard Deviation: {result}"])

            elif choice == "9":
                result = calculate_variance(data)
                print(f"Variance: {result}")
                write_to_csv_file(output_csv_file_path, [f"Variance: {result}"])

            elif choice == "10":
                result = calculate_range(data)
                print(f"Range: {result}")
                write_to_csv_file(output_csv_file_path, [f"Range: {result}"])

            elif choice == "11":
                result = calculate_correlation_coefficient(data, data2)
                print(f"Correlation Coefficient: {result}")
                write_to_csv_file(output_csv_file_path, [f"Correlation Coefficient: {result}"])

            elif choice == "12":
                result = kendall_correlation(data, data2)
                print(f"Kendall Correlation: {result}")
                write_to_csv_file(output_csv_file_path, [f"Kendall Correlation: {result}"])

            elif choice == "13":
                result = spearman_correlation(data, data2)
                print(f"Spearman Correlation: {result}")
                write_to_csv_file(output_csv_file_path, [f"Spearman Correlation: {result}"])

            elif choice == "14":
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 14.")

        except ZeroDivisionError as zde:
            print(f"Math error: {zde}")
        except statistics.StatisticsError as se:
            print(f"Statistics error: {se}")
        except ValueError as ve:
            print(f"Value error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
