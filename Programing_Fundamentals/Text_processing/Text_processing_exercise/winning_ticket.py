def check_validation(tickets):
    winning_symbols = ['@', '#', '$', '^']
    if len(tickets) == 20:
        left_part = tickets[:10]
        right_part = tickets[10:]
        for symbol in winning_symbols:
            if symbol in left_part and symbol in right_part:
                for repetitions in range(10, 5, -1):
                    winning_repetition = repetitions * symbol
                    if winning_repetition in left_part and winning_repetition in right_part:
                        if len(winning_repetition) == 10:
                            return f'ticket "{tickets}" - {len(winning_repetition)}{symbol} Jackpot!'

                        return f'ticket "{tickets}" - {len(winning_repetition)}{symbol}'

        return f'ticket "{tickets}" - no match'
    return "invalid ticket"


collection = [s.strip() for s in input().split(", ")]
for current_ticket in collection:
    print(check_validation(current_ticket))

# def check_validation(tickets):
#     winning_symbols = ['@', '#', '$', '^']
#     if len(tickets) == 20:
#         left_part = tickets[:10]
#         right_part = tickets[10:]
#         for symbol in winning_symbols:
#             if symbol in left_part and symbol in right_part:
#                 is_won = False
#                 for repetitions in range(10, 5, -1):
#                     winning_repetition = repetitions * symbol
#                     if winning_repetition in left_part and winning_repetition in right_part:
#                         if len(winning_repetition) == 10:
#                             print(f'ticket "{tickets}" - {len(winning_repetition)}{symbol} Jackpot!')
#                             is_won = True
#                             break
#                         elif 6 <= len(winning_repetition) < 10:
#                             print(f'ticket "{tickets}" - {len(winning_repetition)}{symbol}')
#                             is_won = True
#                             break
#                 if is_won:
#                     break
#         else:
#             print(f'ticket "{tickets}" - no match')
#
#     else:
#         print("invalid ticket")
#
#
# collection = [s.strip() for s in input().split(", ")]
# for current_ticket in collection:
#     check_validation(current_ticket)

