import numpy as np
from pychord import Chord
from tonegraph.graph import Node


def test_Node__constructor():
    bits_result = (1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0)

    # create using vector
    assert Node(
        vec=np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])
    ).to_bits(), bits_result

    # create using note names
    assert Node(note_names=["C", "E", "G"]).to_bits(), bits_result

    # create using ints
    assert Node(note_ints=[0, 5, 7]).to_bits(), bits_result

    # create using bits
    assert Node(bits=tuple([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])).to_bits(), bits_result

    # create using bit_str
    assert Node(bit_str="100010010000").to_bits(), bits_result


def test_Node__to_chord():
    n = Node(vec=np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))
    assert n.to_chord(), Chord("C")


def test_Node__to_note_names():
    n = Node(vec=np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))
    assert n.to_note_names(), ["C", "E", "G"]


def test_Node__to_note_ints():
    n = Node(vec=np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))
    assert n.to_note_ints(), [0, 5, 7]


def test_Node__to_binary():
    n = Node(vec=np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))
    assert n.to_binary(), [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]


def test_Node__to_bits():
    n = Node(vec=np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))
    assert n.to_bits(), (1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0)


def test_Node__to_bit_str():
    n = Node(vec=np.array([1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]))
    assert n.to_bit_str(), "100010010000"
