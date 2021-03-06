import math

music_section_names = [ 
                        'ADV', 'NUM', 'ADJ', 'NOUN', 'VERB', 'ADP',
                        'AUX', 'PROPN', 'DET', 'PUNCT', 'PRON', 'CCONJ',
                        'X', 'PART', 'INTJ', 'SYM'
                    ]

number_of_section = len(music_section_names)
highest_connect = 70001
pnt_array = []

with open('test_data', 'r') as original_data:
    for pnt in original_data:
        numbers = pnt.split()

        # Skip if there's not exactly 3 items
        if len(numbers) != 3:
            continue

        # Scale points
        scale_factor = 1.6
        for i in range(len(numbers)):
            numbers[i] = str(eval(numbers[i]) * scale_factor)

        pnt_array.append(numbers[0]  + ' ' + numbers[1] + ' ' + numbers[2])


number_of_pnt = len(pnt_array)

with open('full_data', 'w+') as full_data:
    with open('meta-main.txt', 'w+') as meta_main:
        with open('0.txt', 'w+') as main_data:
            for enum_pnt in enumerate(pnt_array):
                section_index = math.floor(enum_pnt[0] * number_of_section / number_of_pnt)
                section = music_section_names[section_index]

                full_data.write('section' + str(section_index+1) + '/' + str(number_of_section) + '_' + section + '\n')
                full_data.write(enum_pnt[1] + ' ')

                if enum_pnt[0] == 0:
                    full_data.write('1\n')

                    # writing to meta-main
                    meta_main.write('0\n')
                    meta_main.write('0 ' + 'section' + str(section_index+1) + '/' + str(number_of_section) + '_' + section + '\n')
                else:
                    full_data.write('0\n')
                
                # writing to main data
                main_data.write(str(enum_pnt[0]) + ', ' + \
                    str(math.ceil(\
                        highest_connect * (number_of_pnt - enum_pnt[0]) / number_of_pnt
                    )) + '\n')