from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


class ToneFrequency:
	def __init__(self, song):
		self.song = song
		self.frequency_of_all_notes = self.get_all_note_frequency()
		self.frequency_of_only_chords = self.get_frequency_only_chords()
		self.plot_get_frequency_only_chords()

	def get_all_note_frequency(self):
		frequencies = defaultdict(int)
		for tone in self.song.tones:
			if tone.is_note():
				frequencies[tone.notePlayed] += 1
			else:
				for note in tone.notes_in_chord:
					frequencies[note.notePlayed] += 1
		return frequencies


	def get_frequency_only_chords(self):
		frequencies = defaultdict(int)
		for tone in self.song.tones:
			if tone.is_chord():
				notes = tuple(note.notePlayed for note in tone.notes_in_chord)
				frequencies[notes] += 1

		return frequencies


	def plot_get_frequency_only_chords(self):
		D = self.frequency_of_only_chords

		plt.bar(range(len(D)), list(D.values()), align='center')
		plt.xticks(range(len(D)), list(D.keys()))
		# # for python 2.x:
		# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
		# plt.xticks(range(len(D)), D.keys())  # in python 2.x

		plt.show()

