def checkmate(board):
    if not isinstance(board, str) or not board:
        return

    lines = board.splitlines()
    if lines and lines[0] == '':
        lines = lines[1:]
    if lines and lines[-1] == '':
        lines = lines[:-1]

    size = len(lines)
    if size == 0:
        return

    # Check if the board is square
    for row in lines:
        if len(row) != size:
            return

    # Find King's position and verify there is exactly one King
    king_pos = None
    king_count = 0
    pieces = {'P', 'B', 'R', 'Q', 'K'}

    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    if king_count != 1 or king_pos is None:
        return

    kr, kc = king_pos

    # 1. Check Pawn attack (Pawn attacks up-left and up-right)
    # So a pawn below the King at (kr + 1, kc - 1) or (kr + 1, kc + 1) attacks the King
    pawn_offsets = [(1, -1), (1, 1)]
    for dr, dc in pawn_offsets:
        r, c = kr + dr, kc + dc
        if 0 <= r < size and 0 <= c < size:
            if lines[r][c] == 'P':
                print("Success")
                return

    # 2. Check Orthogonal rays for Rook (R) or Queen (Q)
    orthogonal_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in orthogonal_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ('R', 'Q'):
                print("Success")
                return
            elif piece in pieces:
                # Any other piece blocks the ray
                break
            r += dr
            c += dc

    # 3. Check Diagonal rays for Bishop (B) or Queen (Q)
    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = lines[r][c]
            if piece in ('B', 'Q'):
                print("Success")
                return
            elif piece in pieces:
                # Any other piece blocks the ray
                break
            r += dr
            c += dc

    print("Fail")
