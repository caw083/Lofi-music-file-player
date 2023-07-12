
import os
import sys
import vlc

# Get the path to the music directory
music_dir = sys.argv[1]

# Get a list of all the files in the music directory
music_files = os.listdir(music_dir)

# Create a VLC instance
instance = vlc.Instance()

# Create a media player object
player = instance.media_player_new()

# Play the music files
while True:
    for music in music_files:
        media = instance.media_new(music_dir + "/" + music)
        player.set_media(media)
        player.play()
        
        # Wait for the playback to finish
        while player.get_state() != vlc.State.Ended:
            pass

    # Release the resources
    player.stop()
    player.release()
