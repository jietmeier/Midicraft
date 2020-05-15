from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))
# track.append(Message('note_on', note=64, velocity=64, time=32))
# track.append(Message('note_off', note=64, velocity=127, time=32))

i=0
while i<128:
    track.append(Message('note_on', note=i, velocity=96, time=0))
    track.append(Message('note_off', note=i, velocity=96, time=3840))
    print(i)
    i+=1


mid.save('0-127.mid')