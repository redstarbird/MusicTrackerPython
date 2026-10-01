class MusicTracker:
    # User-facing properties:
    # self.tracks as a list containing the names of the tracks

    def __init__(self):
        self.tracks: list[str] = []

    def add_track(self, track: str) -> None:
        self.tracks.append(track)

    def list_tracks(self) -> list[str]:
        # Parameters
        # None
        # Returns
        # List of stored track names
        # Side effects
        # None
        pass