import numpy as np
from pychord import Chord, note_to_chord

from .constants import INT_TO_NOTE, NOTE_TO_INT

# For 12-tone music
TOTAL_NUM_TONES = 12

BIN_ARR = np.zeros(TOTAL_NUM_TONES, dtype=int)
NOTE_INTS_ARR = np.array(range(0, TOTAL_NUM_TONES))
NULL_CHORD_NOTE_DELIMITER = "_"


def bin_to_chord(bit_arr):
    notes = NOTE_INTS_ARR[bit_arr > 0]
    note_names = [INT_TO_NOTE[n] for n in notes]
    try:
        chrd = note_to_chord(note_names)
    except:
        return []
    return chrd


def chord_to_binary(chord_str):
    notes = Chord(chord_str).components()
    # print(notes)
    notes_ints = note_names_to_ints(notes)
    # print(notes_ints)
    bin_chrd = notes_to_bin(notes_ints)
    return bin_chrd


def note_names_to_ints(note_names):
    note_ints = [NOTE_TO_INT[n] for n in note_names]
    return note_ints


def notes_to_bin(notes_arr):
    mask = BIN_ARR.copy()
    mask[notes_arr] = 1
    return mask


def bin_to_note_ints(bin_notes_arr):
    return NOTE_INTS_ARR[bin_notes_arr > 0].tolist()


def note_ints_to_names(note_list):
    note_arr = np.array(note_list)
    notes = INT_TO_NOTE[note_arr % TOTAL_NUM_TONES]
    return list(notes)


def note_ints_to_vec(note_ints):
    bin_arr = BIN_ARR.copy()
    bin_arr[note_ints] = 1
    return bin_arr


class Node:
    def __init__(
        self, vec=[], note_ints=[], note_names=[], bits=[], bit_str="", chord=None
    ):
        """
        Create a node.
        """

        # bits is the canonical, immutable representation
        self.bits = []
        self.chord = None
        self.vec = []
        self.note_ints = []
        self.note_names = []

        # Generate bit tuple representation and others
        if len(bits):
            self.bits = bits
            self.vec = np.array(bits)
        elif len(vec):
            self.vec = vec
            self.bits = tuple(np.array(vec).astype(int))
        elif len(note_ints):
            self.note_ints = note_ints
            self.vec = note_ints_to_vec(note_ints)
            self.bin_arr = np.array(self.vec, dtype=int)
            self.bits = tuple(self.bin_arr)
        elif len(note_names):
            self.note_names = note_names
            self.note_ints = note_names_to_ints(note_names)
            self.vec = note_ints_to_vec(self.note_ints)
            self.bits = tuple(self.vec)
        elif len(bit_str):
            self.bits = [c for c in bit_str]
        elif chord:
            self.chord = chord
            self.note_names = chord.components()
            self.note_ints = note_names_to_ints(self.note_names)
            self.vec = note_ints_to_vec(self.note_ints)
            self.bits = tuple(self.vec)
        else:
            raise ValueError("Nodes must be initialized with a value!")

    def to_bits(self):
        return self.bits

    def to_binary(self):
        return list(np.array(self.bits, dtype=int))

    def to_note_ints(self):
        if not len(self.note_ints):
            self.note_ints = bin_to_note_ints(np.array(self.bits))
        return self.note_ints

    def to_note_names(self):
        if not len(self.note_names):
            note_ints = self.to_note_ints()
            self.note_names = note_ints_to_names(note_ints)
        return self.note_names

    def to_chord(self):
        if not self.chord:
            note_names = self.to_note_names()
            chords = note_to_chord(note_names)
            print(chords)
            if len(chords):
                self.chord = chords[0]
            else:
                self.chord = None
        return self.chord

    def to_str(self):
        chord = self.to_chord()
        if chord:
            return str(chord)
        else:
            return NULL_CHORD_NOTE_DELIMITER.join(self.to_note_names())

    def to_bit_str(self):
        return "".join([str(bit) for bit in self.bits])
