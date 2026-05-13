import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")]
    )
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def convert_file():
    input_path = entry.get()
    if not input_path:
        messagebox.showerror("Error", "Please select an MP3 file first.")
        return

    try:
        audio = AudioSegment.from_mp3(input_path)
        output_path = input_path.rsplit(".", 1)[0] + ".wav"
        audio.export(output_path, format="wav")
        messagebox.showinfo("Success", f"Converted to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed:\n{e}")

root = tk.Tk()
root.title("MP3 to WAV Converter")

label = tk.Label(root, text="Select an MP3 file:")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

browse_btn = tk.Button(root, text="Browse", command=select_file)
browse_btn.pack(pady=5)

convert_btn = tk.Button(root, text="Convert to WAV", command=convert_file)
convert_btn.pack(pady=10)

root.mainloop()
