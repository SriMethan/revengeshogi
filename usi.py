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
import main
import sys

logger = logging.getLogger(__name__)

board = shogi.Board()

def sendResponse(msg: str):
    logger.info(f"< {msg}")
    print(msg)

def commandReceived(msg: str):

    logger.info(f"> {msg}")

    if msg == "usi":

        sendResponse("id name Revengeshogi")
        sendResponse("id author SriMethan")
        sendResponse("usiok")
        return

    elif msg == "isready":
        sendResponse("readyok")
        return

    elif msg == "usinewgame":
        return

    elif "position startpos moves" in msg:
        moves = msg.split(" ")[3:]
        board.clear()
        board.set_sfen(shogi.STARTING_SFEN)
        for move in moves:
            board.push(shogi.Move.from_usi(move))
        return

    elif "position sfen" in msg:
        sfen = " ".join(msg.split(" ")[2:])
        sente_starts = sfen == "startpos" or sfen.split()[1] == "b"
        if sente_starts:
            sfen = 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1'
        else:
            sfen = 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL w - 2' 
        board.set_sfen(sfen)
        return

    elif msg[0:2] == "go":
        _move = main.getBestMove(board) 
        sendResponse(f"bestmove {_move}")
        return

    elif msg == "quit":
        sys.exit(0)
