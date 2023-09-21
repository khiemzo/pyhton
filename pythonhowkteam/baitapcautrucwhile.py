def replace_words_before_Kteam(input_string, target_word, replacement):
    words = input_string.split()
    for i in range(1, len(words)):
        if words[i] == target_word:
            words[i - 1] = replacement
    return " ".join(words)

input_string = "an so dfn Kteam odsa in fasfna Kteam mlfjier as dfasod nf ofn asdfer fsan dfoans ldnfad Kteam asdfna asdofn sdf pzcvqp Kteam dfaojf kteam dfna Kteam dfaodf afdna Kteam adfoasdf ncxvo aern Kteam dfad"
result = replace_words_before_Kteam(input_string, "Kteam", "How")
print(result)
