morseFrequency = {"shell": 505, "halls": 515, "slick": 522, "boxes": 535, "leaks": 542, "strobe": 545,
                  "bistro": 552, "flick": 555, "bombs": 565, "break": 572, "steak": 582, "sting": 592, "vector": 595, "beats": 600}

morseTranslate = {'.-': 'A', '-...': 'B',
                  '-.-.': 'C', '-..': 'D', '.': 'E',
                  '..-.': 'F', '--.': 'G', '....': 'G',
                  '..': 'I', '.---': 'J', '-.-': 'K',
                  '.-..': 'L', '--': 'M', '-.': 'N',
                  '---': 'O', '.--.': 'P', '--.-': 'Q',
                  '.-.': 'R', '...': 'S', '-': 'T',
                  '..-': 'U', '...-': 'V', '.--': 'W',
                  '-..-': 'X', '-.--': 'Y', '--..': 'Z'}


def Wires(lastSerial, isOddBool):
    wires = input(
        "\nEnter the color order of the wires from top to bottom using letters (e.g., b for black and bl for blue)\n")
    lastWire = wires[-1]
    wireLen = len(wires) - wires.count("bl")

    if wireLen == 3:
        if "r" in wires.lower():
            if lastWire == "w":
                print("Cut the last wire")
            elif wires.count("bl") > 1:
                print("Cut the last blue wire")
            else:
                print("Cut the last wire")
        else:
            print("Cut the second wire")
    elif wireLen == 4:
        if wires.count("r") > 1 and isOddBool:
            print("Cut the last red wire")
        elif lastWire == "y" and "r" not in wires.lower():
            print("Cut the first wire")
        elif wires.count("bl") == 1:
            print("Cut the first wire")
        elif wires.count("y") > 1:
            print("Cut the last wire")
        else:
            print("Cut the second wire")
    elif wireLen == 5:
        if lastWire == "b" and lastSerial % 2 != 0:
            print("Cut the fourth wire")
        elif wires.count("r") == 1 and wires.count("y") > 1:
            print("Cut the first wire")
        elif wires.count("b") == 0:
            print("Cut the second wire")
        else:
            print("Cut the first wire")
    elif wireLen == 6:
        if wires.count("y") == 0 and isOddBool:
            print("Cut the third wire")
        elif wires.count("y") == 1 and wires.count("w") > 1:
            print("Cut the fourth wire")
        elif wires.count("r") == 0:
            print("Cut the last wire")
        else:
            print("Cut the fourth wire")


def Button(battery_count, has_lit_CAR, has_lit_FRK):
    def held_button(strip_color):
        if strip_color.lower() == "bl" or strip_color.lower() == "blue":
            print("Release the button when the countdown timer has a 4 in any position")
        elif strip_color.lower() == "w" or strip_color.lower() == "white":
            print("Release the button when the countdown timer has a 1 in any position")
        elif strip_color.lower() == "y" or strip_color.lower() == "yellow":
            print("Release the button when the countdown timer has a 5 in any position")
        else:
            print("Release the button when the countdown timer has a 1 in any position")

    button_color = input(
        "\nWhat color is the button? (e.g., bl for blue, r for red)\n")
    button_label = input("What does the button say?\n")

    if button_color.lower() == "bl" and button_label.lower() == "abort":
        strip_color = input(
            "Hold down the button. What color strip lights up at the side of the module?\n")
        held_button(strip_color)
    elif button_label.lower() == "detonate" and battery_count > 1:
        print("Press and immediately release the button.")
    elif button_color.lower() == "w" and has_lit_CAR.lower() == "yes":
        strip_color = input(
            "Hold down the button. What color strip lights up at the side of the module?\n")
        held_button(strip_color)
    elif battery_count > 2 and has_lit_FRK.lower() == "yes":
        print("Press and immediately release the button.")
    elif button_color.lower() == "y":
        strip_color = input(
            "Hold down the button. What color strip lights up at the side of the module?\n")
        held_button(strip_color)
    elif button_color.lower() == "r" and button_label.lower() == "hold":
        print("Press and immediately release the button.")
    else:
        strip_color = input(
            "Hold down the button. What color strip lights up at the side of the module?\n")
        held_button(strip_color)


# Keypad requires too much visual information, not sure how to represent this in a text-based solver.
def Keypad():
    print("Keypad")

# Simon says rules could be displayed by text, or have the computer ask about strikes and check for vowels and take in the color sequence and repeat it


def SimonSays():
    print("SimonSays")


def WhosOnFirst():
    wofTR = ["first", "okay", "c"]
    wofMR = ["blank", "read", "red", "you", "you're", "their"]
    wofBR = ["display", "says", "no", "lead",
             "you are", "hold on", "there", "see", "cee"]
    wofTL = ["ur"]
    wofML = ["yes", "nothing", "led", "they are"]
    wofBL = ["--", "reed", "they're", "leed"]

    def WhosOnFirstLabelList(wofSecondary):
        print("Push the first button in the list below:")
        match wofSecondary.lower():
            case "ready":
                print(
                    "YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY, NO, FIRST, UHHH, NOTHING, WAIT")
            case "first":
                print(
                    "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST")
            case "no":
                print(
                    "BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO, MIDDLE")
            case "blank":
                print(
                    "WAIT, RIGHT, OKAY, MIDDLE, BLANK, PRESS, READY, NOTHING, NO, WHAT, LEFT, UHHH, YES, FIRST")
            case "nothing":
                print(
                    "UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING, READY")
            case "yes":
                print(
                    "OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES, LEFT, BLANK, NO, WAIT")
            case "what":
                print(
                    "UHHH, WHAT, LEFT, NOTHING, READY, BLANK, MIDDLE, NO, OKAY, FIRST, WAIT, YES, PRESS, RIGHT")
            case "uhhh":
                print(
                    "READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH, MIDDLE, WAIT, FIRST")
            case "left":
                print(
                    "RIGHT, LEFT, FIRST, NO, MIDDLE, YES, BLANK, WHAT, UHHH, WAIT, PRESS, READY, OKAY, NOTHING")
            case "right":
                print(
                    "YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT, MIDDLE, LEFT, UHHH, BLANK, OKAY, FIRST")
            case "middle":
                print(
                    "BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE, RIGHT, FIRST, UHHH, YES")
            case "okay":
                print(
                    "MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY, LEFT, READY, BLANK, PRESS, WHAT, RIGHT")
            case "wait":
                print(
                    "UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT, NOTHING, READY, RIGHT, MIDDLE")
            case "press":
                print(
                    "RIGHT, MIDDLE, YES, READY, PRESS, OKAY, NOTHING, UHHH, BLANK, LEFT, FIRST, WHAT, NO, WAIT")
            case "you":
                print(
                    "SURE, YOU ARE, YOUR, YOU’RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU, UH UH, LIKE, DONE, U")
            case "you are":
                print(
                    "YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU’RE, SURE, UR, YOU ARE")
            case "your":
                print(
                    "UH UH, YOU ARE, UH HUH, YOUR, NEXT, UR, SURE, U, YOU’RE, YOU, WHAT?, HOLD, LIKE, DONE")
            case "you're":
                print(
                    "YOU, YOU’RE, UR, NEXT, UH UH, YOU ARE, U, YOUR, WHAT?, UH HUH, SURE, DONE, LIKE, HOLD")
            case "ur":
                print(
                    "DONE, U, UR, UH HUH, WHAT?, SURE, YOUR, HOLD, YOU’RE, LIKE, NEXT, UH UH, YOU ARE, YOU")
            case "u":
                print(
                    "UH HUH, SURE, NEXT, WHAT?, YOU’RE, UR, UH UH, DONE, U, YOU, LIKE, HOLD, YOU ARE, YOUR")
            case "uh huh":
                print(
                    "UH HUH, YOUR, YOU ARE, YOU, DONE, HOLD, UH UH, NEXT, SURE, LIKE, YOU’RE, UR, U, WHAT?")
            case "uh uh":
                print(
                    "UR, U, YOU ARE, YOU’RE, NEXT, UH UH, DONE, YOU, UH HUH, LIKE, YOUR, SURE, HOLD, WHAT?")
            case "what?":
                print(
                    "YOU, HOLD, YOU’RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?, SURE")
            case "done":
                print(
                    "SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU’RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE")
            case "next":
                print(
                    "WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT, LIKE, DONE, YOU ARE, UR, YOU’RE, U, YOU")
            case "hold":
                print(
                    "YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU’RE, NEXT, HOLD, UH HUH, YOUR, LIKE")
            case "sure":
                print(
                    "YOU ARE, DONE, LIKE, YOU’RE, YOU, HOLD, UH HUH, UR, SURE, U, WHAT?, NEXT, YOUR, UH UH")
            case "like":
                print(
                    "YOU’RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE, SURE, YOU ARE, YOUR")

    for _ in range(3):
        wofDisplayed = input(
            "What word is displayed? (-- for a blank display)\n")
        wofSecondary = ""
        if wofDisplayed in wofTR:
            wofSecondary = input("What word is in the top right?\n")
        elif wofDisplayed in wofMR:
            wofSecondary = input("What word is in the middle right?\n")
        elif wofDisplayed in wofBR:
            wofSecondary = input("What word is in the bottom right?\n")
        elif wofDisplayed in wofTL:
            wofSecondary = input("What word is in the top left?\n")
        elif wofDisplayed in wofML:
            wofSecondary = input("What word is in the middle left?\n")
        elif wofDisplayed in wofBL:
            wofSecondary = input("What word is in the bottom left?\n")

        WhosOnFirstLabelList(wofSecondary)


def Memory():
    def get_position_value(position):
        return input(f"What number is in the {position} position?\n")

    def get_button_position(label):
        return input(f"What position is the button labeled {label}?\n")

    def press_button(label):
        print(f"Press the button with the label {label}")

    displayedNumber = int(input("What number is being displayed?\n"))

    stage1Pos, stage1Value = None, None
    stage2Pos, stage2Value = None, None
    stage3Pos, stage3Value = None, None
    stage4Pos, stage4Value = None, None

    # STAGE ONE
    if displayedNumber in [1, 2]:
        stage1Pos = 2
        stage1Value = get_position_value(stage1Pos)
        print("Press the second position")
    elif displayedNumber == 3:
        stage1Pos = 3
        stage1Value = get_position_value(stage1Pos)
        print("Press the third position")
    elif displayedNumber == 4:
        stage1Pos = 4
        stage1Value = get_position_value(stage1Pos)
        print("Press the fourth position")

    # STAGE TWO
    displayedNumber = int(input("What number is being displayed?\n"))
    if displayedNumber == 1:
        stage2Pos = get_button_position(4)
        stage2Value = 4
        press_button(4)
    elif displayedNumber in [2, 4]:
        stage2Value = get_position_value(stage1Pos)
        stage2Pos = stage1Pos
        print(f"Press the button in position {stage1Pos}")
    elif displayedNumber == 3:
        stage2Value = get_position_value(1)
        stage2Pos = 1
        print("Press the button in the first position")

    # STAGE THREE
    displayedNumber = int(input("What number is being displayed?\n"))
    if displayedNumber == 1:
        stage3Pos = get_button_position(stage2Value)
        stage3Value = stage2Value
        press_button(stage2Value)
    elif displayedNumber == 2:
        stage3Pos = get_button_position(stage1Value)
        stage3Value = stage1Value
        press_button(stage1Value)
    elif displayedNumber == 3:
        stage3Value = get_position_value(3)
        stage3Pos = 3
        print("Press the button in the third position")
    elif displayedNumber == 4:
        stage3Pos = get_button_position(4)
        stage3Value = 4
        print("Press the button labeled 4")

    # STAGE FOUR
    displayedNumber = int(input("What number is being displayed?\n"))
    if displayedNumber == 1:
        stage4Value = get_position_value(stage1Pos)
        stage4Pos = stage1Pos
        print(f"Press the button in position {stage1Pos}")
    elif displayedNumber == 2:
        stage4Value = get_position_value(1)
        stage4Pos = 1
        print("Press the button in the first position")
    elif displayedNumber in [3, 4]:
        stage4Value = get_position_value(stage2Pos)
        stage4Pos = stage2Pos
        print(f"Press the button in position {stage2Pos}")

    # STAGE FIVE
    displayedNumber = int(input("What number is being displayed?\n"))
    if displayedNumber == 1:
        press_button(stage1Value)
    elif displayedNumber == 2:
        press_button(stage2Value)
    elif displayedNumber == 3:
        press_button(stage4Value)
    elif displayedNumber == 4:
        press_button(stage3Value)


def Morse():
    morseMessage = input(
        "Input the Morse code from the start using / as a space: \n")
    morseLetters = morseMessage.split("/")
    morseTranslated = ''.join(
        morseTranslate[letter] for letter in morseLetters)
    frequency = morseFrequency.get(morseTranslated.lower())

    if frequency:
        print(f"Set the frequency to 3.{frequency}.")
    else:
        print("Invalid Morse code input.")


def ComplicatedWires(isOdd, batteries):
    wires = int(input("How many wires are in this module?\n"))
    for i in range(wires):
        print(
            f"Enter the {i + 1} position wire details using the notation below")
        print("Color (r, b, or w), Star (*), LED On (!) if both r+b -> use p\n")
        wire = input("")

        if wire in ["r", "b", "p", "p!"]:
            if not isOdd:
                print("Cut the wire")
            else:
                print("Do not cut")
        elif wire == "r*":
            print("Cut the wire")
        elif wire in ["r*!", "r!", "w*!"]:
            if batteries >= 2:
                print("Cut the wire")
            else:
                print("Do not cut")
        elif wire == "w":
            print("Cut the wire")
        elif wire == "w*":
            print("Cut the wire")
        elif wire == "w!":
            print("Do not cut")
        elif wire == "b*":
            print("Do not cut")
        elif wire in ["b*!", "b!", "p*"]:
            print("Cut the wire if there is a parallel port")
        elif wire == "p*!":
            if batteries >= 2:
                print("Do not cut")
            else:
                print("Cut the wire")


def WireSequence(wire_color, wire_occurrence):
    while True:
        wire_color = input(
            "Enter the wire color (red, blue, or black). You can exit the code by typing N/A at any time: \n")
        if wire_color == "N/A":
            break

        wire_occurrence = int(input("Enter the wire occurrence (1 to 9): "))

        def cut_wire(wire_color, wire_occurrence):
            if wire_color == "red":
                if wire_occurrence == 1:
                    return "C"
                elif wire_occurrence == 2:
                    return "B"
                elif wire_occurrence == 3:
                    return "A"
                elif wire_occurrence == 4:
                    return "A or C"
                elif wire_occurrence == 5:
                    return "B"
                elif wire_occurrence == 6:
                    return "A or C"
                elif wire_occurrence == 7:
                    return "A, B or C"
                elif wire_occurrence == 8:
                    return "A or B"
                elif wire_occurrence == 9:
                    return "B"

            elif wire_color == "blue":
                if wire_occurrence == 1:
                    return "B"
                elif wire_occurrence == 2:
                    return "A or C"
                elif wire_occurrence == 3:
                    return "B"
                elif wire_occurrence == 4:
                    return "A"
                elif wire_occurrence == 5:
                    return "B"
                elif wire_occurrence == 6:
                    return "B or C"
                elif wire_occurrence == 7:
                    return "C"
                elif wire_occurrence == 8:
                    return "A or C"
                elif wire_occurrence == 9:
                    return "A"

            elif wire_color == "black":
                if wire_occurrence == 1:
                    return "A, B or C"
                elif wire_occurrence == 2:
                    return "A or C"
                elif wire_occurrence == 3:
                    return "B"
                elif wire_occurrence == 4:
                    return "A or C"
                elif wire_occurrence == 5:
                    return "B"
                elif wire_occurrence == 6:
                    return "B or C"
                elif wire_occurrence == 7:
                    return "A or B"
                elif wire_occurrence == 8:
                    return "C"
                elif wire_occurrence == 9:
                    return "C"

        result = cut_wire(wire_color, wire_occurrence)
        print("Cut if connected to:", result)


# Maze requires too much visual information, not sure how to represent this in a text-based solver.
def Maze():
    print("Maze")


def Password():
    wordList = [
        "about", "after", "again", "below", "could",
        "every", "first", "found", "great", "house",
        "large", "learn", "never", "other", "place",
        "plant", "point", "right", "small", "sound",
        "spell", "still", "study", "their", "there",
        "these", "thing", "think", "three", "water",
        "where", "which", "world", "would", "write"
    ]

    column1 = input(
        "Enter the letters for the first column (separated by spaces): ").split()
    column2 = input(
        "Enter the letters for the second column (separated by spaces): ").split()
    column3 = input(
        "Enter the letters for the third column (separated by spaces): ").split()
    column4 = input(
        "Enter the letters for the fourth column (separated by spaces): ").split()

    matchingWord = None

    for word in wordList:
        if (
            word[0] in column1
            and word[1] in column2
            and word[2] in column3
            and word[3] in column4
        ):
            matchingWord = word
            break

    if matchingWord:
        print("Matching word:", matchingWord)
    else:
        print("No matching word found.")


def Knob():  # This function can technically be called as many times as the player wants, but for an 11 module bomb it can only be called once as the other 10 will have to be used for the vanillas.
    knobBinary = input(
        "Enter the pattern of lights shown from left to right, using 0 for off and 1 for on.\n")

    if knobBinary in ["001011111101", "101010011011"]:
        print("Put the knob in the up position")
    elif knobBinary in ["011001111101", "101010010001"]:
        print("Put the knob in the down position")
    elif knobBinary in ["000010100111", "000010000110"]:
        print("Put the knob in the left position")
    else:
        print("Put the knob in the right position")


def DefuseManager():
    serialNumber = input("\nWhat is the serial number of the bomb?\n")
    isOdd = int(serialNumber[-1]) % 2 == 1
    batteries = int(input("How many batteries are on the bomb?\n"))
    litCAR = input(
        "Does the bomb have a lit indicator with label CAR on the casing?\n")
    litFRK = input(
        "Does the bomb have a lit indicator with label FRK on the casing?\n")
    modules = int(input("How many modules are on the bomb?\n"))

    for _ in range(modules):
        moduleToSolve = input(
            "\nWhat module would you like to solve?\n").lower()

        if moduleToSolve in ("wires", "wire"):
            Wires(serialNumber, isOdd)
        elif moduleToSolve in ("button", "the button", "a button"):
            Button(batteries, litCAR, litFRK)
        elif moduleToSolve in ("keypad", "keypads", "a keypad"):
            Keypad()
        elif moduleToSolve in ("simon says", "simon", "simon say"):
            SimonSays()
        elif moduleToSolve in ("whos on first", "wof", "who's on first"):
            WhosOnFirst()
        elif moduleToSolve == "memory":
            Memory()
        elif moduleToSolve in ("morse", "morse code"):
            Morse()
        elif moduleToSolve in ("complicated wires", "complex wires", "complicated wire", "complex wire", "complicated", "complex"):
            ComplicatedWires(isOdd, batteries)
        elif moduleToSolve in ("wire sequence", "wires sequence", "sequence"):
            WireSequence()
        elif moduleToSolve in ("maze", "mazes"):
            Maze()
        elif moduleToSolve in ("passwords", "password"):
            Password()
        elif moduleToSolve in ("knob", "knobs"):
            Knob()


DefuseManager()
