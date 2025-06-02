import sys
import locale


def reverse_and_sort_words(input_file, output_file):
    try:
        # Step 1: Read words from the input file
        with open(input_file, 'r') as infile:
            words = [line.strip() for line in infile if line.strip()]  # Remove empty lines and strip whitespace

        # Step 2: Reverse each word
        reversed_words = [word[::-1] for word in words]

        # Step 3: Sort reversed words lexicographically
        reversed_words.sort(key=locale.strxfrm)

        # Step 4: Reverse the sorted words back to their original order
        sorted_words = [word[::-1] for word in reversed_words]

        # Step 5: Write the sorted words to the output file
        with open(output_file, 'w') as outfile:
            for word in sorted_words:
                outfile.write(word + '\n')

        print(f"Words have been sorted and written to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with the path to your input file
    output_file = "output.txt"  # Replace with the path to your output file
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    loc = locale.getlocale()  # get current locale
    # use By locale; name might vary with platform
    locale.setlocale(locale.LC_ALL, 'be_BY.utf8')

    reverse_and_sort_words(input_file, output_file)
    locale.setlocale(locale.LC_ALL, loc)  # restore saved locale
