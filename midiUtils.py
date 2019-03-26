class Utils:
	def __init__(self):
		self.number_to_letter_mappings = dict()
		self.pattern = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

	def build_number_letter_mapping(self):
		if len(self.number_to_letter_mappings) == 0:
			octave = 0
			for num_note in range(21, 109):
				letter = self.pattern[(num_note - 21) % len(self.pattern)]
				if letter == 'C':
					octave += 1
				self.number_to_letter_mappings[num_note] = self.pattern[(num_note - 21) % len(self.pattern)] + str(octave)

	def note_number_to_letter(self, num_note):
		self.build_number_letter_mapping()
		return self.number_to_letter_mappings[num_note]



class Tone:
	def __init__(self):
		self.threshold_limit = .25

	def is_Note(self):
		return False
	def is_Chord(self):
		return False
	def is_close(self, other_note):
		raise NotImplementedError("To be implemented")

class Note(Tone):

	def __init__(self, absoluteStart, absoluteStop, notePlayed, velocityStart, velocityStop):
		super().__init__()
		self.absoluteStart = absoluteStart
		self.absoluteStop = absoluteStop
		self.duration = self.absoluteStop - self.absoluteStart
		self.notePlayed = notePlayed
		self.velocityStart = velocityStart
		self.velocityStop = velocityStop

	def is_note(self):
		return True

	def is_close(self, other_note):
		start_difference = abs(self.absoluteStart - other_note.absoluteStart)
		stop_difference = abs(self.absoluteStop - other_note.absoluteStop)
		

		if start_difference <= threshold_limit and stop_difference <= threshold_limit:
			return True
		return False

class Chord(Tone):

	def __init__(self):
		super().__init__()
		self.notes_in_chord = list()
		self.num_chords = 0
		self.average_duration = 0
		self.average_start_time = 0
		self.average_stop_time = 0


	def is_chord(self):
		return True

	def add_note(self, note):
		self.average_duration = self.get_new_average(self.average_duration, note.duration)
		self.average_start_time = self.get_new_average(self.average_start_time, note.absoluteStart)
		self.average_stop_time = self.get_new_average(self.average_stop_time, note.absoluteStop)

		self.num_chords += 1

		self.notes_in_chord.append(note)


	def get_new_average(self, previous_cumulation, next_number):
		previous_sum = previous_cumulation * self.num_chords
		current_sum = previous_sum + next_number
		return current_sum / (self.num_chords + 1)

	def is_close(self, other_note):
		start_difference = abs(self.average_start_time - other_note.absoluteStart)
		stop_difference = abs(self.average_stop_time - other_note.absoluteStop)
		

		if start_difference <= threshold_limit and stop_difference <= threshold_limit:
			return True
		return False
