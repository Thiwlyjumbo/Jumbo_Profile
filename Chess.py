import chess

# กำหนดคะแนนของหมากแต่ละตัว (คิงคะแนนเยอะสุดเพราะห้ามตาย)
PIECE_VALUES = {
    chess.PAWN: 10,
    chess.KNIGHT: 30,
    chess.BISHOP: 30,
    chess.ROOK: 50,
    chess.QUEEN: 90,
    chess.KING: 900
}

# ฟังก์ชันประเมินกระดาน: นำคะแนนหมากขาว - คะแนนหมากดำ
def evaluate_board(board):
    if board.is_checkmate():
        return -9999 if board.turn == chess.WHITE else 9999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    score = 0
    for piece_type in PIECE_VALUES:
        # นับจำนวนหมากแต่ละสี
        white_pieces = len(board.pieces(piece_type, chess.WHITE))
        black_pieces = len(board.pieces(piece_type, chess.BLACK))
        score += (white_pieces - black_pieces) * PIECE_VALUES[piece_type]
    return score

# อัลกอริทึม Minimax พร้อม Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if is_maximizing: # ฝั่งขาวพยายามทำคะแนนให้บวกมากที่สุด
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break # ตัดกิ่งทิ้ง
        return max_eval
    else: # ฝั่งดำพยายามทำคะแนนให้ติดลบมากที่สุด
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break # ตัดกิ่งทิ้ง
        return min_eval

# ฟังก์ชันให้บอทเลือกตาเดินที่ดีที่สุด
def get_best_move(board, depth=3):
    best_move = None
    is_maximizing = board.turn == chess.WHITE
    
    if is_maximizing:
        best_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, int(depth) - 1, -float('inf'), float('inf'), False)
            board.pop()
            if eval > best_eval:
                best_eval = eval
                best_move = move
    else:
        best_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, int(depth) - 1, -float('inf'), float('inf'), True)
            board.pop()
            if eval < best_eval:
                best_eval = eval
                best_move = move
                
    return best_move

# --- เริ่มเกม ---
def play_game():
    board = chess.Board()
    print("=== ยินดีต้อนรับสู่ Python Chess Bot ===")
    print("วิธีเดิน: พิมพ์ตัวย่อแบบสากล เช่น e4, Nf3, Bc4, O-O")
    
    # เลือกฝั่ง
    player_side = input("คุณต้องการเล่นฝั่งไหน? (w = ขาว / b = ดำ): ").lower()
    while player_side not in ['w', 'b']:
        player_side = input("กรุณาพิมพ์ w หรือ b: ").lower()
        
    player_color = chess.WHITE if player_side == 'w' else chess.BLACK

    # ลูปสลับตากันเดิน
    while not board.is_game_over():
        print("\n" + "-"*30)
        print(board) # แสดงกระดาน (ตัวพิมพ์ใหญ่=ขาว, ตัวพิมพ์เล็ก=ดำ)
        print("-"*30)

        if board.turn == player_color:
            # ตาผู้เล่น
            move_str = input(f"\nตาของคุณ เดินหมาก: ")
            try:
                move = board.parse_san(move_str)
                board.push(move)
            except ValueError:
                print("!! ตาเดินไม่ถูกต้อง หรือพิมพ์ผิดรูปแบบ ลองใหม่ครับ (เช่น e4, Nf3)")
        else:
            # ตาบอท
            print("\nบอทกำลังคิด...")
            bot_move = get_best_move(board, depth=3) # ปรับ depth ได้ (ยิ่งเยอะยิ่งเก่งแต่คิดนาน)
            # แสดงชื่อหมากที่บอทเดิน
            san_move = board.san(bot_move)
            print(f"-> บอทเดิน: {san_move}")
            board.push(bot_move)

    # จบเกม
    print("\n" + "="*30)
    print(board)
    print("เกมจบแล้ว!")
    if board.is_checkmate():
        winner = "ดำ" if board.turn == chess.WHITE else "ขาว"
        print(f"รุกฆาต! สี{winner} ชนะ!")
    elif board.is_stalemate():
        print("เสมอ! (Stalemate)")
    else:
        print("เสมอ!")

if __name__ == "__main__":
    play_game()