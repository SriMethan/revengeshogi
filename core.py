# This file is part of Revengeshogi Engine.
# Copyright (C) 2022- SriMethan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# You should have received a copy of the MIT License along with this 
# USI Shogi Engine. If not, view this https://opensource.org/licenses/MIT


import logging
import shogi
import random

logger = logging.getLogger(__name__)

board = None

def getBestMove(board: shogi.Board) -> shogi.Move:
    
    for candidate_move in list(board.legal_moves):
        
        board.push(candidate_move)
        if board.is_checkmate():
            logging.info(f"{candidate_move} will checkmate, this is the best move")
            return candidate_move
        else:
            board.pop()    

    return random.choice(list(board.legal_moves))