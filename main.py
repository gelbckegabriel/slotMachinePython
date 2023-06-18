import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#  ROWS AND COLUMNS OF THE SLOT MACHINE.
ROWS = 3
COLS = 3

#  SYMBOLS OF OUR SLOT MACHINE AND AMOUNT OF SYMBOL ON EACH REEL. 'A' IS THE MOST VALUABLE ON THIS CASE.
symbol_count = {
    'A': 2,  # 2 'A' on each reel.
    'B': 4,  # 4 'B' on each reel.
    'C': 6,  # 6 'C' on each reel.
    'D': 8   # 8 'D' on each reel.
}

symbol_value = {
    'A': 5,  # THIS SYMBOL HAS THE MULTIPLIER OF '5' BECAUSE OF RARITY.
    'B': 4,  # THIS SYMBOL HAS THE MULTIPLIER OF '4' BECAUSE OF RARITY.
    'C': 3,  # THIS SYMBOL HAS THE MULTIPLIER OF '3' BECAUSE OF RARITY.
    'D': 2   # THIS SYMBOL HAS THE MULTIPLIER OF '2' BECAUSE OF RARITY.
}


# THIS WILL VERIFY IF A COLUMN HAS ALL THE THREE CHARACTERS MATCHING.
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

        return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    #  LOOP TO GENERATE A COLUMN FOR EVERY SINGLE COLUMN THAT WE HAVE.
    #  (IF WE HAVE THREE COLUMNS, DO THIS LOOP THREE TIMES).
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        #  THIS LOOP PICKS A RANDOM VALUE TO EACH ROW THAT WE HAVE.
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # THIS REMOVES THE VALUE SO THAT IT DOESN'T PICK IT AGAIN.
            column.append(value)  # THIS ADDS THE VALUE TO THE COLUMN.

        columns.append(column)

    return columns


# WE GOT DEFINE A FUNCTION THAT WILL PRINT CORRECTLY AS COLUMNS AND ROWS.
def print_slot_machine(columns):
    print("-MACHINE-")
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:  # TO VERIFY IF IT SHOULD HAVE A '|' AFTER THE VARIABLE.
                print(column[row], "| ", end="")
            else:
                print(column[row])
    print("- - - - -\n")


def deposit():
    while True:
        amount = input("Value of deposit: U$ ")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0 !\n")
        else:
            print("Please enter a valid number.\n")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines !\n")
        else:
            print("Please enter a number.\n")

    return lines


def get_bet():
    while True:
        amount = input("Value of bet on each line: U$ ")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between 'U$ {MIN_BET}' and 'U$ {MAX_BET}' !")
        else:
            print("Please enter a valid number.\n")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet_value = get_bet()
        total_bet = bet_value * lines

        if total_bet > balance:
            print(f"Not enough balance for this bet (U${total_bet})! CURRENT BALANCE: U$ {balance}\n")
        else:
            break

    print(f"You're betting U${bet_value} on {lines} lines. TOTAL BET: U$ {total_bet}\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet_value, symbol_value)
    print(f"You've won U$ {winnings}. ", end="")
    print("You won on lines:", *winning_lines)  # THE '*' IS THE SPLAT/UNPACK OPERATOR.
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f'CURRENT BALANCE: U$ {balance}')
        answer = input("Press 'ENTER' to play! ('Q' and 'ENTER' to QUIT) \n")
        if answer == 'q' or answer == 'Q':
            break
        balance += spin(balance)

    print(f"FINAL BALANCE: U$ {balance}.")


main()
