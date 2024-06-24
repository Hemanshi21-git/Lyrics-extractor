import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import lyricsgenius

def get_lyrics(apitoken, artist, song, language):
    genius = lyricsgenius.Genius(apitoken)
    
    try:
        lyrics = genius.search_song(song, artist)
        if lyrics:
            return lyrics.lyrics
        else:
            return "Lyrics not found."
    except Exception as e:
        return f"Error: {e}"

def extract_lyrics():
    apitoken = "dlqTo2-moMQmqwGYMwQTlxzQMOYj4S_Gi8GO8hI6qHkgpLoJ2agHVhNNEio46QLZ"  
    artist = artist_entry.get()    #take artist entry
    song = song_entry.get()        #take song name
    language = language_var.get()

    if not apitoken or not artist or not song:
        messagebox.showinfo("Error", "Please fill all field.")
        return

    lyrics = get_lyrics(apitoken, artist, song, language)

    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, lyrics)

# Create main root:
root = tk.Tk()
root.title("Lyrical")
# Set the root icon:
icon_path = r"C:/internship task/lyricsextractor/song.ico"
root.iconbitmap(icon_path)

# Set root size and position:
root_width = 500
root_height = 600
root.geometry(f"{root_width}x{root_height}")
root.eval('tk::PlaceWindow . center')

# Load the background image
background_image = Image.open("C:/internship task/lyricsextractor/background.jpg") 
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas and place the background image
canvas = tk.Canvas(root, width=root_width, height=root_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Create and place widgets on the canvas using `place`:(label,entry)
artist_label = tk.Label(root, text="Artist:", bd=1, relief="solid", bg="#F2F4F3", fg="#051923", font=("Helvetica", 12, "bold"))
song_label = tk.Label(root, text="Song:", bd=1, relief="solid", bg="#F2F4F3", fg="#051923", font=("Helvetica", 12, "bold"))
language_label = tk.Label(root, text="Language:", bd=1, relief="solid", bg="#F2F4F3", fg="#051923", font=("Helvetica", 12, "bold"))

artist_entry = tk.Entry(root, bd=1, relief="solid")
song_entry = tk.Entry(root, bd=1, relief="solid")

artist_label.place(x=590, y=120)
artist_entry.place(x=690, y=120, width=300)
song_label.place(x=590, y=160)
song_entry.place(x=690, y=160, width=300)
language_label.place(x=590, y=200)

# Add a option for language selection:
language_var = tk.StringVar()
language_options = ["English","Hindi", "Spanish", "French", "German", "Italian","Punjabi"]
language_menu = ttk.Combobox(root, textvariable=language_var, values=language_options, state="readonly")
language_menu.place(x=690, y=200, width=300)
language_menu.current(0)  # Set default selection to the first language

# Set button  and place it:
extract_button = tk.Button(root, text="Extract Lyrics", command=extract_lyrics, bg="#051923", fg="#ffffff",font=("Helvetica", 10, "bold"))
extract_button.place(x=750, y=240, width=100)

# Frame where result is shown:
result_text = tk.Text(root, height=20, width=40, bd=2, relief="solid",bg="#FBF7F4")
result_text.place(x=590, y=280, width=400, height=400)

# Start the GUI main loop
root.mainloop()
