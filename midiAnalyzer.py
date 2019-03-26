from mido import MidiFile
from mido.midifiles.units import tempo2bpm, bpm2tempo, tick2second, second2tick
from midiUtils import Utils, Tone, Note, Chord







util = Utils()
#note on my keyboard is from note=21 to note=108 == 88 keys

# mid = MidiFile('./aFriendLikeYou/aflu6.mid')
mid = MidiFile('legato.mid')
print((mid.ticks_per_beat))
# print(mid.ticks_per_beat, 1000)
# print(mid.tracks)
# exit()
tempoPerMinute = 500000
totalNotes = list()
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    # print(dir(track))
    cumulative_time = 0
    currently_played_notes = dict()

    for msg in track:
    	if not msg.is_meta:
    		# print(msg, tick2second(msg.time, mid.ticks_per_beat, tempoPerMinute), util.note_number_to_letter(msg.note))
    		cumulative_time += tick2second(msg.time, mid.ticks_per_beat, tempoPerMinute)
    		message_note = util.note_number_to_letter(msg.note)
    		if message_note in currently_played_notes:
    			absoluteStart, velocityStart = currently_played_notes.pop(message_note)
    			note = Note(absoluteStart, cumulative_time, message_note, velocityStart, msg.velocity)
    			totalNotes.append(note)
    		else:
    			currently_played_notes[message_note] = (cumulative_time, msg.velocity)


    for note in totalNotes:
    	print(note.notePlayed, note.absoluteStart, note.absoluteStop)

    		# print(util.note_number_to_letter(msg.note), cumulative_time)
    		# print(msg)

    	# print(dir(msg))
    	# print(msg.is_realtime)
    	# exit()
    	# if not msg.is_meta:
        	# print(util.note_number_to_letter(msg.note))
        	# print(msg, util.note_number_to_letter(msg.note))



