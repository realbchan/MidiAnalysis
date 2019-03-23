number_to_letter_mappings = dict()

pattern = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

def build_number_letter_mapping():
	if len(number_to_letter_mappings) == 0:
		octave = 0
		for num_note in range(21, 109):
			letter = pattern[(num_note - 21) % len(pattern)]
			if letter == 'C':
				octave += 1
			number_to_letter_mappings[num_note] = pattern[(num_note - 21) % len(pattern)] + str(octave)


def note_number_to_letter(num_note):
	build_number_letter_mapping()
	return number_to_letter_mappings[num_note]

for i in range(21, 2019):
	print (note_number_to_letter(i))

