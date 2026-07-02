def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-1):
    m = len(seq1)
    n = len(seq2)

    # Create scoring matrix
    score = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    max_score = 0
    max_pos = (0, 0)

    # Fill matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                diag = score[i - 1][j - 1] + match
            else:
                diag = score[i - 1][j - 1] + mismatch

            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap

            score[i][j] = max(0, diag, up, left)

            if score[i][j] > max_score:
                max_score = score[i][j]
                max_pos = (i, j)

    # Traceback
    align1 = ""
    align2 = ""

    i, j = max_pos

    while i > 0 and j > 0 and score[i][j] > 0:

        if seq1[i - 1] == seq2[j - 1]:
            diag_score = score[i - 1][j - 1] + match
        else:
            diag_score = score[i - 1][j - 1] + mismatch

        if score[i][j] == diag_score:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1

        elif score[i][j] == score[i - 1][j] + gap:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1

        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    print("\nBest Local Alignment:")
    print("Sequence 1:", align1)
    print("Sequence 2:", align2)
    print("Alignment Score:", max_score)


# User Input
seq1 = input("Enter First Sequence: ").upper()
seq2 = input("Enter Second Sequence: ").upper()

smith_waterman(seq1, seq2)