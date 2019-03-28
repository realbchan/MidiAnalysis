from midiUtils import Utils, Tone, Note, Chord, Song
from collections import defaultdict
import matplotlib.pyplot as plt

class ToneFrequency:
	def __init__(self, song):
		self.song = song
		self.frequency_of_all_notes = self.get_all_note_frequency()
		# self.frequency_of_only_chords = self.get_frequency_only_chords()

	def get_all_note_frequency(self):
		frequencies = defaultdict(int)
		for tone in self.song.tones:
			if tone.is_note():
				frequencies[tone.notePlayed] += 1
			else:
				for note in tone.notes_in_chord:
					frequencies[note.notePlayed] += 1
		return frequencies

	#notes_in_chord variable in Chord is a list, thus not hashable...

	# def get_frequency_only_chords(self):
	# 	frequencies = defaultdict(int)
	# 	for tone in self.song.tones:
	# 		if tone.is_chord():
	# 			for note in tone.notes_in_chord:
	# 				frequencies[note.notePlayed] += 1

	# 	return frequencies

