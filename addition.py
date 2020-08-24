#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on August 2020
# This program adds 0.1 to 0.2

import constants


def main():
    # This function adds 0.1 to 0.2

    # Process
    total = constants.ADDEND_1 + constants.ADDEND_2

    # Output
    print("")
    print("The sum of {0} and {1} is {2}"
          .format(constants.ADDEND_1, constants.ADDEND_2, total))


if __name__ == "__main__":
    main()
