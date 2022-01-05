# This file is part of Revengeshogi Engine.
# Copyright (C) 2022- SriMethan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License.
#
# You should have received a copy of the MIT License along with this 
# USI Shogi Engine. If not, view this https://opensource.org/licenses/MIT

import logging
import usi
import sys

def main():

    logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('Revengeshogi started')

    try:
        while True:
            msg = input()
            usi.commandReceived(msg)

    except Exception:
        logging.exception('Fatal error in main loop')

if __name__ == '__main__':
    main()