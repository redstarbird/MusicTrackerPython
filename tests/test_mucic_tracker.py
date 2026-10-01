from lib.music_tracker import *
import pytest

"""
Given a track added to the tracker
The track name should be stored in the self.tracks list
"""
def test_add_one_track():
    tracker = MusicTracker()
    tracker.add_track("Track 1")
    assert tracker.tracks == ["Track 1"]

"""
Given a 2 tracks added to the tracker via add_track
The names of the tracks should be stored in the self.tracks list
"""
def test_add_two_track():
    tracker = MusicTracker()
    tracker.add_track("Track 1")
    tracker.add_track("Track 2")
    assert tracker.tracks == ["Track 1", "Track 2"]

"""
Given an empty track name to add_track
An expection should be raised
"""
def test_add_empty_track():
    tracker = MusicTracker()
    with pytest.raises(Exception) as error:
        tracker.add_track("")

    assert str(error.value) == "Track name cannot be empty!"

"""
Given an incorrect data type as name to add_track
An expection should be raised
"""
def test_add_incorrect_type():
    tracker = MusicTracker()
    with pytest.raises(Exception) as error:
        tracker.add_track(5.2)

    assert str(error.value) == "Track name must be of type string!"

"""
Given no tracks added to the tracker
list_tracks should return an empty list
"""
def test_list_empty_tracks():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []

"""
Given a track added to the tracker
list_tracks should return the name of the track within a list
"""

def test_list_one_track():
    tracker = MusicTracker()
    tracker.add_track("Track 1")
    assert tracker.list_tracks() == ["Track 1"]

"""
Given a 2 tracks added to the tracker via add_track
list_tracks should return the names of the two tracks within a list
"""

def test_list_two_tracks():
    tracker = MusicTracker()
    tracker.add_track("Track 1")
    tracker.add_track("Track 2")
    assert tracker.list_tracks() == ['Track 1', 'Track 2']