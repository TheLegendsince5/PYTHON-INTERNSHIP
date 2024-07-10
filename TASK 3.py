import tkinter as tk
from tkinter import messagebox
from lyricsgenius import Genius

class LyricsExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyrics Extractor")

        self.label1 = tk.Label(root, text="Song Title:")
        self.label1.pack()

        self.song_entry = tk.Entry(root, width=50)
        self.song_entry.pack()

        self.label2 = tk.Label(root, text="Artist:")
        self.label2.pack()

        self.artist_entry = tk.Entry(root, width=50)
        self.artist_entry.pack()

        self.extract_button = tk.Button(root, text="Extract Lyrics", command=self.extract_lyrics)
        self.extract_button.pack()

        self.lyrics_display = tk.Text(root, height=20, width=80)
        self.lyrics_display.pack()

    def extract_lyrics(self):
        song_title = self.song_entry.get().strip()
        artist_name = self.artist_entry.get().strip()

        if not song_title or not artist_name:
            messagebox.showerror("Error", "Please enter both song title and artist name.")
            return

        genius = Genius("LHrBJHyEUqxS83sADPFGGRApbGQ8sIZz_ok35eJanxRR1LKbZMEKq3m0nndvyef1bAGqLb4lCbDeVYwDBS4J-Q")  # Replace with your Genius API key
        try:
            song = genius.search_song(song_title, artist_name)
            if song:
                self.lyrics_display.delete(1.0, tk.END)
                self.lyrics_display.insert(tk.END, song.lyrics)
            else:
                messagebox.showerror("Error", "Lyrics not found for the specified song and artist.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LyricsExtractorApp(root)
    root.mainloop()
