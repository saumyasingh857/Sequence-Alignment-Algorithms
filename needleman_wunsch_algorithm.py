def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-1):
    m = len(seq1)
    n = len(seq2)

    # Create scoring matrix
    score = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        score[i][0] = i * gap

    for j in range(n + 1):
        score[0][j] = j * gap

    # Fill scoring matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                diagonal = score[i - 1][j - 1] + match
            else:
                diagonal = score[i - 1][j - 1] + mismatch

            up = score[i - 1][j] + gap
            left = score[i][j - 1] + gap

            score[i][j] = max(diagonal, up, left)

    # Traceback
    align1 = ""
    align2 = ""

    i = m
    j = n

    while i > 0 and j > 0:
        current = score[i][j]

        if seq1[i - 1] == seq2[j - 1]:
            diag_score = score[i - 1][j - 1] + match
        else:
            diag_score = score[i - 1][j - 1] + mismatch

        if current == diag_score:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1

        elif current == score[i - 1][j] + gap:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1

        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1

    while i > 0:
        align1 = seq1[i - 1] + align1
        align2 = "-" + align2
        i -= 1

    while j > 0:
        align1 = "-" + align1
        align2 = seq2[j - 1] + align2
        j -= 1

    print("\nGlobal Alignment:")
    print(align1)
    print(align2)
    print("\nAlignment Score:", score[m][n])


# User Input
seq1 = input("Enter First Sequence: ").upper()
seq2 = input("Enter Second Sequence: ").upper()

needleman_wunsch(seq1, seq2)