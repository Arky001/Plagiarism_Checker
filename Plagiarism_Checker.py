import tkinter as tk
from fuzzywuzzy import fuzz

def calculate_similarity():
    # Retrieve the texts from the input fields
    text1 = entry1.get("1.0", "end-1c")
    text2 = entry2.get("1.0", "end-1c")

    # Calculate the similarity ratio using fuzzywuzzy's ratio function
    similarity = fuzz.ratio(text1, text2)

    # Update the similarity label with the result
    similarity_label.config(text=f"Similarity: {similarity}%")

# Create the main window
window = tk.Tk()
window.title("Plagiarism Checker")

# Create labels
label1 = tk.Label(window, text="Text 1:")
label1.pack()
entry1 = tk.Text(window, height=10, width=50)
entry1.pack(pady=5)

label2 = tk.Label(window, text="Text 2:")
label2.pack()
entry2 = tk.Text(window, height=10, width=50)
entry2.pack(pady=5)

# Create button
button = tk.Button(window, text="Check Similarity", command=calculate_similarity)
button.pack(pady=10)

# Create label to display similarity result
similarity_label = tk.Label(window, text="")
similarity_label.pack()

# Start the main event loop
window.mainloop()
