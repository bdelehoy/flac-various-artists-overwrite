from mutagen.flac import FLAC
from pathlib import Path

MUSIC_FOLDER = Path("")

if __name__ == "__main__":
    for f in MUSIC_FOLDER.iterdir():
        if len(f.suffix) > 1 and f.suffix[1:].upper() == "FLAC":
            print(f"Processing file: {f}")
            metadata = FLAC(f)
            title = metadata["title"]
            if type(title) == list and len(title) > 0:
                title = title[0]

            # Find title tags that follow the format "{artist} - {song}"
            # Will not work with artists or songs that contain the string " - "
            if " - " in title:
                title_parts = title.split(" - ")
                if len(title_parts) == 2:
                    new_song_title = title_parts[1]
                    new_artist = title_parts[0]

                    metadata["title"] = new_song_title
                    metadata["artist"] = new_artist
                    metadata.save()
                    print(f"    *** Changed metadata for {new_artist} - \"{new_song_title}\"")
                else:
                    print(f"    Incompatible title (unexpected split): {title}")
            else:
                print(f"    Incompatible title (nothing to split): {title}")
