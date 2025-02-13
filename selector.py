import numpy as np
import glob

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start) if mode == "encrypt" else chr((ord(char) - start - shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

def reverse_cipher(text):
    return text[::-1]

def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(ord('a') + ord('z') - ord(char))
            else:
                result += chr(ord('A') + ord('Z') - ord(char))
        else:
            result += char
    return result

def selector_menu():
    def process_input():
        selected_cipher = cipher_var.get()
        input_text = input_text_entry.get("1.0", tk.END).strip()  # Get text from Text widget
        shift_value = shift_entry.get()
        mode = mode_var.get()
        
        try:
            if selected_cipher == "Caesar Cipher":
                shift = int(shift_value)
                output_text = caesar_cipher(input_text, shift, mode)
            elif selected_cipher == "Reverse Cipher":
                output_text = reverse_cipher(input_text)
            elif selected_cipher == "Atbash Cipher":
                output_text = atbash_cipher(input_text)
            else:
                output_text = "No cipher selected."
            output_text_area.delete("1.0", tk.END)  # Clear previous output
            output_text_area.insert(tk.END, output_text)
        except ValueError:
            messagebox.showerror("Error", "Invalid shift value. Please enter an integer.")
        except Exception as e: # Catch any other exceptions
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    window = tk.Tk()
    window.title("Cipher Tool Selector")
    
    # Input Frame
    input_frame = ttk.LabelFrame(window, text="Input Text")
    input_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    input_text_entry = tk.Text(input_frame, wrap=tk.WORD, height=5) # Use Text widget
    input_text_entry.pack(fill=tk.BOTH, expand=True)
    
    # Cipher Selection
    cipher_label = ttk.Label(window, text="Select Cipher:")
    cipher_label.pack(pady=(0, 5))  # Add padding below the label
    
    ciphers = ["Caesar Cipher", "Reverse Cipher", "Atbash Cipher"]
    cipher_var = tk.StringVar(value=ciphers[0])  # Default selection
    cipher_dropdown = ttk.Combobox(window, textvariable=cipher_var, values=ciphers, state="readonly")
    cipher_dropdown.pack()
    
    # Shift Value (for Caesar Cipher)
    shift_label = ttk.Label(window, text="Shift Value (for Caesar):")
    shift_label.pack(pady=(5, 0))
    shift_entry = ttk.Entry(window)
    shift_entry.pack()
    shift_entry.insert(0, "3") # Default shift value
    
    # Mode Selection (for Caesar Cipher)
    mode_label = ttk.Label(window, text="Mode (for Caesar):")
    mode_label.pack(pady=(5, 0))
    modes = ["encrypt", "decrypt"]
    mode_var = tk.StringVar(value=modes[0])
    mode_dropdown = ttk.Combobox(window, textvariable=mode_var, values=modes, state="readonly")
    mode_dropdown.pack()
    
    # Process Button
    process_button = ttk.Button(window, text="Process", command=process_input)
    process_button.pack(pady=10)
    
    # Output Frame
    output_frame = ttk.LabelFrame(window, text="Output Text")
    output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    output_text_area = tk.Text(output_frame, wrap=tk.WORD, height=5)
    output_text_area.pack(fill=tk.BOTH, expand=True)
    
    window.mainloop()  # Start the Tkinter event loop

def minth():
    choice = selector_menu()
    return

if __name__ == "__main__":
    minth()