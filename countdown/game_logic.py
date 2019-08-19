""" File can be deleted once completed """

player_answer_given = 'STAR'.lower()
player_answer_length = get_answer_length(player_answer_given)
print(f'{"Player Answer Length: "}{player_answer_length}')

comp_answer_given = get_longest_possible_word(words_list)
comp_answer_length = len(comp_answer_given)
print(f'{"Comp Answer Length: "}{comp_answer_length}')

print("Oh dear, I'm afraid I only managed to get " +
      '"' + player_answer_given + '"')
time.sleep(1)

print("""Ha ha ha, you will never deafeat me. I am the original lexicographer!
I got """ + '"' + comp_answer_given + '"')
