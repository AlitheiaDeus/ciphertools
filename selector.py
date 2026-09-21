import numpy as np
import glob

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

import ciphers
import inspect

def selector_menu():
    cipher_functions = [
        (name, func) for name, func in inspect.getmembers(ciphers)
        if inspect.isfunction(func) and func.__module__ == 'ciphers' #check if it's in the ciphers module
    ]
    cipher_names = [name for name, func in cipher_functions]
    
    def process_input():
        selected_cipher_name = cipher_var.get()
        input_text = input_text_entry.get("1.0", tk.END).strip()
        # shift_value = shift_entry.get()
        mode = mode_var.get()

        try:
            selected_cipher_func = None
            for name, func in cipher_functions:
                if name == selected_cipher_name:
                    selected_cipher_func = func
                    output_text = selected_cipher_func(input_text)  # Call the selected function
                    break
                else:
                    output_text = "No cipher selected."

            output_text_area.delete("1.0", tk.END)
            output_text_area.insert(tk.END, output_text)

        except ValueError:
            messagebox.showerror("Error", "Invalid shift value. Please enter an integer.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    window = tk.Tk()
    window.title("Cipher Tool Selector")
    
    # Input Frame
    input_frame = ttk.LabelFrame(window, text="Input Text")
    input_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    input_text_entry = tk.Text(input_frame, wrap=tk.WORD, height=5) # Use Text widget
    input_text_entry.pack(fill=tk.BOTH, expand=True)
    
    # Cipher Selection (Dynamically populated)
    cipher_label = ttk.Label(window, text="Select Cipher:")
    cipher_label.pack(pady=(0, 5))
    
    cipher_var = tk.StringVar(value=cipher_names[0] if cipher_names else "")  # Default selection
    cipher_dropdown = ttk.Combobox(window, textvariable=cipher_var, values=cipher_names, state="readonly")
    cipher_dropdown.pack()
    
    mode_label = ttk.Label(window, text="Mode:")  # Now for all ciphers
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