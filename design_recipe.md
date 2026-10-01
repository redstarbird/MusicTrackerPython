# music Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicTracker:
    # User-facing properties:
    # self.tracks as a list containing the names of the tracks

    def __init__(self):
        # Parameters
        # None
        # Side effects
        # Initialise self.tracks as an empty list

    def add_track(self, track: str) -> None:
        # Parameters
        # track name as a string
        # Returns
        # Nothing
        # Side effects
        # Adds the track name to the list of tracks
        # Raise exception if the track name is not a string or if it is empty

    def list_tracks(self) -> list[str]:
        # Parameters
        # None
        # Returns
        # List of stored track names
        # Side effects
        # None
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

```python

"""
Given a track added to the tracker
The track name should be stored in the self.tracks list
"""
tracker = MusicTracker()
tracker.add_track("Track 1")
tracker.tracks # => ['Track 1']

"""
Given a 2 tracks added to the tracker via add_track
The names of the tracks should be stored in the self.tracks list
"""
tracker = MusicTracker()
tracker.add_track("Track 1")
tracker.add_track("Track 2")
tracker.tracks # => ['Track 1', 'Track 2']

"""
Given an empty track name to add_track
An expection should be raised
"""
tracker = MusicTracker()
tracker.add_track("")
tracker.tracks # => Exception("Track name cannot be empty!")

"""
Given an incorrect data type as name to add_track
An expection should be raised
"""
tracker = MusicTracker()
tracker.add_track(5.2)
tracker.tracks # => Exception("Track name must be of type string!")

"""
Given no tracks added to the tracker
list_tracks should return an empty list
"""
tracker = MusicTracker()
tracker.list_tracks() # => []

"""
Given a track added to the tracker
list_tracks should return the name of the track within a list
"""
tracker = MusicTracker()
tracker.add_track("Track 1")
tracker.list_tracks() # => ['Track 1']

"""
Given a 2 tracks added to the tracker via add_track
list_tracks should return the names of the two tracks within a list
"""
tracker = MusicTracker()
tracker.add_track("Track 1")
tracker.add_track("Track 2")
tracker.list_tracks() # => ['Track 1', 'Track 2']
```
