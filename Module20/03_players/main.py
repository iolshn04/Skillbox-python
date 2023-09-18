def decode(player_list):
    decode_list = []
    for i_index, i_value in player_list.items():
        decode_list.append(i_index + i_value)
    return decode_list


players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

print(decode(players))

# зачтено
