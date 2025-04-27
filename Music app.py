import pygame
import os

pygame.init()

pygame.mixer.init()

def play_music(music_file):
    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
    except pygame.error as e:
        print("Error playing Music")

def main(song_index=None):
    music_library = input("Enter Full path of your music folder (example: C:\\\\Users\\\\YourName\\\\Music): ").strip()

    if not os.path.exists(music_library):
        print(f"Error: Music library directory '{music_library}' not found.")
        return
    music_files = [
        os.path.join(music_library, f)
        for f in os.listdir(music_library)
        if os.path.isfile(os.path.join(music_library, f)) and f.lower().endswith((".mp3", ".wav"))

    ]
    if not music_files:
        print("No files found in library directory.")
        return
    if not music_files:
        print("No music files found in the library.")
        return

        # Main application loop
    while True:
        print("\nAvailable music files:")
        for i, file in enumerate(music_files):
            print(f"{i + 1}. {os.path.basename(file)}")

        choice = input("Enter the number of the song to play (or 'q' to quit): ")

        if choice.lower() == "q":
            break
        try:
            song_index - int(choice) - 1
            if 0 <= song_index < len(music_files):
                play_music(music_files[song_index])
                print(f"Now playing: {os.path.basename(music_files[song_index])}")
                while pygame.mixer.music.get_busy():
                    pygame.time.clock().tick(10)
            else:
                print("Invalid Song number")
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")
pygame.quit()

if __name__ == "__main__":
    main()

