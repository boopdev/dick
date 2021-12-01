import os
import re

def formatdick(dick : str) -> int:
    x = re.match("8(=*)D", dick)

    if not x:
        raise ValueError("Invalid dick supplied")

    return len(x.group(1))

def ensureHand(hand) -> None:
    if hand is not None:
        return
    else:
        raise ValueError("Nothing in hand")

def runDicklang(filename : os.PathLike):
    in_hand = None
    vars_ = {}

    with open(filename, 'r') as buffer:
        
        for line in buffer:
            keyword, *args = line.strip('\n').split(" ")

            match keyword:
                case "DICK": # assign var
                    vars_[args[0]] = formatdick(args[1])

                case "GRAB": # set hand to var
                    try:
                        in_hand = [args[0], vars_[args[0]]]
                    except KeyError:
                        raise KeyError("No variable with that name found!")

                case "RELEASE": # unset hand from var
                    if in_hand[0] == args[0]:
                        in_hand = None
                    else:
                        raise ValueError("What")

                case "LONGDICK": # addition to hand
                    ensureHand(in_hand)
                    in_hand[1] += formatdick(args[0])

                case "SMALLDICK": # subtraction from hand
                    ensureHand(in_hand)
                    in_hand[1] -= formatdick(args[0])

                case "HUGEDICK": # multiply hand
                    ensureHand(in_hand)
                    in_hand[1] *= formatdick(args[0])

                case "TINYDICK": # divide from hand
                    ensureHand(in_hand)

                    if args[0] == 0:
                        raise ZeroDivisionError("You're really enjoying yourself aren't you?")

                    in_hand[1] /= formatdick(args[0])

                case "PEE": # print penis to term
                    print(f"8{'='*in_hand[1]}D")

                case "WEE": # print ascii value of hand
                    print(chr(in_hand[1]))