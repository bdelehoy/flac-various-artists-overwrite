from mutagen.flac import FLAC
from pathlib import Path

MUSIC_FOLDER = Path("C:\\Users\\your_username\\Downloads\\extracted_music_folder")

# "Artist - Song"
#        ^^^
ARTIST_SONG_SEPARATOR_STRING = " - "

if __name__ == "__main__":
    for f in MUSIC_FOLDER.iterdir():
        if f.is_file() and len(f.suffix) > 1 and f.suffix[1:].upper() == "FLAC":
            print(f"Processing file: {f}")
            metadata = FLAC(f)
            title = metadata["title"]
            if isinstance(title, list) and len(title) > 0:
                title = title[0]

            if ARTIST_SONG_SEPARATOR_STRING in title:
                title_parts = title.split(ARTIST_SONG_SEPARATOR_STRING)

                new_artist = title_parts[0]

                # Get song title
                if len(title_parts) == 2:
                    # Cleanly split into artist and song title
                    new_song_title = title_parts[1]
                elif len(title_parts) > 2:
                    # Split into multiple tokens (uncommon)
                    new_song_title = ARTIST_SONG_SEPARATOR_STRING.join(title_parts[1:])
                else:
                    print(f"    Incompatible title (unexpected song title tokens): {title}")
                    continue

                metadata["artist"] = new_artist
                metadata["title"] = new_song_title
                metadata.save()
                print(f"    *** Changed metadata for {new_artist} - \"{new_song_title}\"")
            else:
                print(f"    Incompatible title (couldn't split; incorrect separator string?): {title}")
