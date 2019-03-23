from mido import MidiFile

#note on my keyboard is from note=21 to note=108 == 88 keys

# mid = MidiFile('./aFriendLikeYou/aflu1.mid')
mid = MidiFile('test.mid')


for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)