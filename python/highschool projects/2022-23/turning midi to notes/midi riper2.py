import mido
from mido import MidiFile
from collections import defaultdict

class Note:
    def __init__(self, pitch, octave, duration, velocity=1):
        self.pitch = pitch
        self.octave = octave
        self.duration = duration
        self.velocity = velocity

class Sequencer:
    def __init__(self, notes_list):
        self.notes_list = notes_list

MIDI_NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def parse_midi_file(file_path):
    midi_file = MidiFile(file_path)
    sequencers = []

    for track in midi_file.tracks:
        current_time = 0
        notes_list = []

        for msg in track:
            current_time += msg.time

            if msg.type == 'note_on':
                if msg.velocity > 0:
                    pitch_name = MIDI_NOTE_NAMES[msg.note % 12]
                    octave = msg.note // 12
                    notes_list.append(Note(pitch_name, octave, msg.time, velocity=msg.velocity / 127))

        sequencer = Sequencer(notes_list)
        sequencers.append(sequencer)

    return sequencers

#if __name__ == "__main__":
midi_file_path = R"C:\Users\trevin\Music\Aqua_-_Barbie_Girl.mid"
sequencers = parse_midi_file(midi_file_path)
for seq in sequencers:
    print('[')
    for n in seq.notes_list:
        print(f"Note({n.pitch},{n.octave},{n.duration},{n.velocity}),")
    print(']')
print(sequencers)
    # Now you have a list of sequencers, each containing the notes from a different MIDI track or channel
    # You can use each sequencer to play the notes independently
