text = input()
symbols_dict = {}
for ch in text:
    if ch not in symbols_dict.keys():
        symbols_dict[ch] = 0
    symbols_dict[ch] += 1
for ch, count in sorted(symbols_dict.items()):
    print(f"{ch}: {count} time/s")
