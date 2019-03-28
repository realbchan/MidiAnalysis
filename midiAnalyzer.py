from mido import MidiFile
from mido.midifiles.units import tempo2bpm, bpm2tempo, tick2second, second2tick
from midiUtils import Utils, Tone, Note, Chord, Song


util = Utils()

# mid = MidiFile('./aFriendLikeYou/aflu6.mid')
mid = MidiFile('./aFriendLikeYou/aflu6.mid')
print((mid.ticks_per_beat))
# print(mid.ticks_per_beat, 1000)
# print(mid.tracks)
# exit()
tempoPerMinute = 500000
totalNotes = list()
song = Song()
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    cumulative_time = 0
    currently_played_notes = dict()

    for msg in track:
    	if not msg.is_meta:
    		cumulative_time += tick2second(msg.time, mid.ticks_per_beat, tempoPerMinute)
    		message_note = util.note_number_to_letter(msg.note)

    		if message_note in currently_played_notes:
    			absoluteStart, velocityStart = currently_played_notes.pop(message_note)
    			note = Note(absoluteStart, cumulative_time, message_note, velocityStart, msg.velocity)
    			song.add_note(note)
    			# print(song)
    		else:
    			currently_played_notes[message_note] = (cumulative_time, msg.velocity)
    print(len(song.tones))
    # song.sort_by_start_of_tone()
    for tone in song.tones:
    	print(tone)




