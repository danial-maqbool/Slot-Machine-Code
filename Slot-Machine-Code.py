import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = {
    "A": (2, 5),
    "B": (4, 4),
    "C": (6, 3),
    "D": (8, 2)
}


def calculate_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            winnings += symbols[symbol][1] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def generate_spin(rows, cols):
    all_symbols = []
    for symbol, (count, _) in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)
    return columns


def display_machine(columns):
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))


def get_deposit():
    while True:
        try:
            amount = int(input("Deposit amount: $"))
            if amount > 0:
                return amount
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_line_count():
    while True:
        try:
            lines = int(input(f"Lines to bet on (1-{MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Invalid number of lines.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_bet_amount():
    while True:
        try:
            amount = int(input("Bet per line: $"))
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_round(balance):
    lines = get_line_count()
    bet = get_bet_amount()
    total_bet = bet * lines

    if total_bet > balance:
        print(f"Insufficient balance. You have ${balance}.")
        return 0

    print(f"Betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    result = generate_spin(ROWS, COLS)
    display_machine(result)

    winnings, winning_lines = calculate_winnings(result, lines, bet)
    print(f"You won ${winnings} on lines: {', '.join(map(str, winning_lines))}")

    return winnings - total_bet


balance = get_deposit()
while True:
    print(f"Current balance: ${balance}")
    if input("Press Enter to spin (q to quit): ").lower() == 'q':
        break
    balance += play_round(balance)

print(f"Final balance: ${balance}")
