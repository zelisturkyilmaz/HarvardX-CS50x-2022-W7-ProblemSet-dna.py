import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Missing command-line arguments")
        sys.exit(1)
    if not ".csv" in sys.argv[1]:
        print("Second argument must be csv file")
        sys.exit(2)
    if not ".txt" in sys.argv[2]:
        print("Third argument must be a text file")
        sys.exit(3)

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as data:
        reader = csv.DictReader(data)
        database = {key: [] for key in reader.fieldnames}
        for row in reader:
            for key in reader.fieldnames:
                database[key].append(row[key])

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequence:
        text = sequence.read()

    # TODO: Find longest match of each STR in DNA sequence
    match = []
    keys = []
    for sub in database.keys():
        a = str(longest_match(text, sub))
        match.append(a)
        keys.append(sub)
    matches = dict(zip(keys, match))
    del matches["name"]

#    print(database)
#    print(matches)

    # TODO: Check database for matching profiles
    length = len(database["name"])
    index = -1
    freq = []
    for key in matches:
        for i in range(length):
            if matches[key] == database[key][i]:
                freq.append(i)
                if freq.count(i) == len(matches):
                    index = i

    if index >= 0:
        print(database["name"][index])
    else:
        print("No match")

#    print(freq)
#    print(length)
#    print(index)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
