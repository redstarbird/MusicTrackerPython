class MusicTracker:
    # User-facing properties:
    # self.tracks as a list containing the names of the tracks

    def __init__(self):
        self.tracks: list[str] = []

    def add_track(self, track: str) -> None:
        if track == "":
            raise Exception ("Track name cannot be empty!")

        if not isinstance(track, str):
            raise Exception ("Track name must be of type string!")

        self.tracks.append(track)

    def list_tracks(self) -> list[str]:
        # Parameters
        # None
        # Returns
        # List of stored track names
        # Side effects
        # None
        pass