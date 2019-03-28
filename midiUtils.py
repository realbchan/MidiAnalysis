class Utils:
	# initialize, build mapping from a note number to a note letter
	def __init__(self):
		self.number_to_letter_mappings = dict()
		self.pattern = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
		self.build_number_letter_mapping()

	# this method maps a number to a note letter and it's octave
	# notes on my keyboard is from note=21 to note=108 == 88 keys
	# I dont think the piano can represent anything out of this range
	def build_number_letter_mapping(self):
		octave = 0
		for num_note in range(21, 109):
			letter = self.pattern[(num_note - 21) % len(self.pattern)]
			if letter == 'C':
				octave += 1
			self.number_to_letter_mappings[num_note] = self.pattern[(num_note - 21) % len(self.pattern)] + str(octave)

	# get method, retrieve note letter from note number
	def note_number_to_letter(self, num_note):
		return self.number_to_letter_mappings[num_note]

# each note or chord is considered a "Tone"
# This is the parent class for Note and Chord
class Tone:
	def __init__(self):
		# this threshold limit determines how "close"
		# a note is to another note in seconds, this can be tuned
		self.threshold_limit = .25

	def is_note(self):
		return False
	def is_chord(self):
		return False
	# must be implemented in Note and Chord
	def is_close(self, other_note):
		raise NotImplementedError("To be implemented")

# I define a Note to be a single musical note played
# If there are 1 or 2 notes "close" by, it is considered a Chord
class Note(Tone):
	# takes in parameters from message, calculates duration
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
	# uses self.threshold to determine if a note is close
	def is_close(self, other_note):
		start_difference = abs(self.absoluteStart - other_note.absoluteStart)
		stop_difference = abs(self.absoluteStop - other_note.absoluteStop)

		if start_difference <= self.threshold_limit and stop_difference <= self.threshold_limit:
			return True
		return False

# a chord is considered 1 or 2 notes that are close by
class Chord(Tone):
	# we need to keep track of the average parameters of a chord
	def __init__(self):
		super().__init__()
		self.notes_in_chord = list()
		self.num_chords = 0
		self.average_duration = 0
		self.average_start_time = 0
		self.average_stop_time = 0


	def is_chord(self):
		return True

	# on adding a note, recalculate averages
	def add_note(self, note):
		self.average_duration = self.get_new_average(self.average_duration, note.duration)
		self.average_start_time = self.get_new_average(self.average_start_time, note.absoluteStart)
		self.average_stop_time = self.get_new_average(self.average_stop_time, note.absoluteStop)

		self.num_chords += 1

		self.notes_in_chord.append(note)

	# calculate new arbitrary average
	def get_new_average(self, previous_cumulation, next_number):
		previous_sum = previous_cumulation * self.num_chords
		current_sum = previous_sum + next_number
		return current_sum / (self.num_chords + 1)

	# similar to is_close for Note
	def is_close(self, other_note):
		start_difference = abs(self.average_start_time - other_note.absoluteStart)
		stop_difference = abs(self.average_stop_time - other_note.absoluteStop)
		

		if start_difference <= self.threshold_limit and stop_difference <= self.threshold_limit:
			return True
		return False

# a Song is a list of Tones
# it represents a midi track as a whole
class Song:
	def __init__(self):
		self.tones = list()
	# sorts tones by start
	def sort_by_start_of_tone(self):
		# sorting comparator, probably could refactor
		def get_start(tone):
			if tone.is_note():
				return tone.absoluteStart
			else:
				return tone.average_start_time

		self.tones.sort(key=get_start)
	# add note to song, will detect if needs to make a chord
	def add_note(self, note):
		if len(self.tones) == 0:
			self.tones.append(note)
		else:
			last_tone = self.tones[len(self.tones) - 1]
			# print(self.tones[-10:])
			# last_ten_tones = self.tones[-10:]
			# found_neighbor = False
			# for previous_tone in last_ten_tones:

			if last_tone.is_close(note):
				# found_neighbor = True

				if last_tone.is_note():
					chord = Chord()
					chord.add_note(last_tone)
					chord.add_note(note)
					self.tones.pop()
					self.tones.append(chord)
				else:
					last_tone.add_note(note)
			# 		# break
			# if not found_neighbor:
			else:
				self.tones.append(note)




