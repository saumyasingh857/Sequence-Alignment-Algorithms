def pairwise_comparison(seq1, seq2):
    # Convert sequences to uppercase
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    # Check if lengths are equal
    if len(seq1) != len(seq2):
        print("Sequences must be of equal length.")
        return

    matches = 0

    print("\nPosition\tSeq1\tSeq2\tResult")

    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            matches += 1
            result = "Match"
        else:
            result = "Mismatch"

        print(f"{i+1}\t\t{seq1[i]}\t{seq2[i]}\t{result}")

    similarity = (matches / len(seq1)) * 100

    print("\nTotal Matches:", matches)
    print("Total Length:", len(seq1))
    print("Similarity Percentage: {:.2f}%".format(similarity))


# User Input
sequence1 = input("Enter First DNA Sequence: ")
sequence2 = input("Enter Second DNA Sequence: ")

pairwise_comparison(sequence1, sequence2)