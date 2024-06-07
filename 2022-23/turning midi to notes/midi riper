import mido
from mido import MidiFile

# Define the BPM for the MIDI file
BPM = 126

# Open the MIDI file
midi_file = MidiFile(R"C:\Users\trevin\Music\cupid.mid")



# Initialize a list to store the sequences
tracks = []

#print(dir(midi_file))

# Process each track in the MIDI file
for track in midi_file.tracks:
    # [curent timestamp of sequence]
    sequences=[ [0] ]
    playing=[]
    time=0
    for msg in track:
    
        # print(msg.type)
        if msg.type == 'note_on'and msg.velocity!=0:
            for note in playing:
                note[2]+=msg.time
            time+=msg.time
            # Append the note to the sequences list
            # midi val, velocity,length,start time
            playing.append(  [msg.note,msg.velocity,0,time]  )
            #print(msg.time)
        
            #elif msg.type == 'note_on' and  msg.velocity==0:
        elif msg.type == 'note_off':

            # Find the corresponding note_on message and calculate the length
            #note_on_msg = next((m for m in reversed(track[:msg.index]) if m.type == 'note_on' and m.note == msg.note), None)
            #if note_on_msg:
            #note_length = (msg.time + note_on_msg.time) * (60 / BPM)
            #note_length=msg.time/480*(120/90)
            
            # Append the note to the sequences list
            # previous
            for note in playing:
                note[2]+=msg.time
            time+=msg.time
            
            for note in playing:
                if note[0]==msg.note:
                    
                    print("good note")
                    found=False
                    for sequence in sequences:
                        if sequence[0]<=note[3] and not found:
                            found=True
                            # midi val, velocity,length,

                            sequence.append(  (None, 0, note[3]-sequence[0] )) # type: ignore

                            sequence.append( (msg.note, note[1], note[2] ) ) # type: ignore

                            sequence[0]+=note[3]-sequence[0]
                            sequence[0]+=note[2]
                            print("rem",note)

                            playing.remove(note)
                            
                            
                    if not found:
                        sequences.append([time])
                        sequence=sequences[-1]
                        sequence.append(  (None, 0, time ))

                        sequence.append(  (None, 0, note[3]-sequence[0] )) # type: ignore

                        sequence.append( (msg.note, note[1], note[2] ) ) # type: ignore

                        sequence[0]+=note[3]-sequence[0]
                        sequence[0]+=note[2]
                        print("rem2",note)


                        playing.remove(note)

                # else:print("bad")
            # sequences.append(f"Note({msg.note}, 0, {note_length}),")
    print(playing,"\n\nplaying\n\ntracks\n\n")
    for sequence in sequences:
        tracks.append(sequence)



# Print the sequences
print(tracks)

print("\n\n\n\n\n",midi_file.ticks_per_beat)

with open('output.txt', 'a') as f:
    f.write(str(tracks))
    f.write('exit')
