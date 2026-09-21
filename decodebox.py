def character_frequency_sorted(filename):
    """
    Parses a text file, counts character frequencies (case-insensitive),
    and prints them sorted from most to least frequent.
    Handles potential errors and non-text files.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except UnicodeDecodeError:
        print(f"Error: '{filename}' appears to be a binary file, not a text file. Skipping.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    char_counts = {}
    for char in text:
        char = char.lower()  # Case-insensitive counting
        char_counts[char] = char_counts.get(char, 0) + 1

    # Sort by frequency (most frequent first)
    sorted_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

    # Print the frequencies
    for char, count in sorted_counts:
        print(f"'{char}': {count}")

    print(f"\nTotal unique characters: {len(char_counts)}")

# Example usage:
filename = "code1.txt"
character_frequency_sorted(filename)