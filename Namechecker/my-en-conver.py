import preprocess as p
import mm_transpitor_module as mm

mapped_names = ''
input_text="မင်းသူ"

# Step 1: Preprocess
processed_text = p.preprocess(input_text)

word_list = mm.processed_text.split(' ')
mapped_names = ' '.join(p.get_map(word, word_dict) for word in word_list)

input_code_point = ''.join(hex(ord(char)) for char in processed_text)
output_text = mapped_names.p.capitalize()

print(output_text)


