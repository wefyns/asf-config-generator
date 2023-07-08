import tkinter as tk
from helpers import open_url_trade_token, open_url_steam, select_file, generate
import styles

# Create the main window
window = tk.Tk()
window.title("ASF Config Generator")
window.geometry("600x400")
window.configure(bg=styles.WINDOW_BG_COLOR)

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Create the label and entry field for file selection
file_label = tk.Label(window, text="Select text file:", **styles.LABEL_STYLE)
file_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

file_entry = tk.Entry(window, **styles.ENTRY_STYLE)
file_entry.grid(row=0, column=1, padx=(0, 20), pady=(20, 0), sticky="we")

file_button = tk.Button(window, text="Browse", command=lambda: select_file(
    file_entry), **styles.BUTTON_STYLE)
file_button.grid(row=0, column=2, padx=(0, 20), pady=(20, 0), sticky="e")

# Create the label and entry field for Steam ID
steam_id_label = tk.Label(window, text="Your Steam ID:", **styles.LABEL_STYLE)
steam_id_label.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="w")

steam_id_entry = tk.Entry(window, **styles.ENTRY_STYLE)
steam_id_entry.grid(row=1, column=1, padx=(0, 20), pady=(20, 0), sticky="we")

# Create a button for the trade token URL
token_url_button = tk.Button(
    window, text="Open steam URL", command=lambda: open_url_steam(), **styles.BUTTON_STYLE)
token_url_button.grid(row=2, column=1, padx=(0, 20), pady=(20, 0), sticky="we")

# Create the label and entry field for Steam Trade Token
trade_token_label = tk.Label(
    window, text="Your Steam Trade Token:", **styles.LABEL_STYLE)
trade_token_label.grid(row=3, column=0, padx=20, pady=(20, 0), sticky="w")

trade_token_entry = tk.Entry(window, **styles.ENTRY_STYLE)
trade_token_entry.grid(row=3, column=1, padx=(0, 20),
                       pady=(20, 0), sticky="we")

# Create a button for the trade token URL
token_url_button = tk.Button(
    window, text="Open trade token URL", command=lambda: open_url_trade_token(), **styles.BUTTON_STYLE)
token_url_button.grid(row=4, column=1, padx=(0, 20), pady=(20, 0), sticky="we")

# Create the checkbox for AutoSteamSaleEvent
auto_sale_event_var = tk.BooleanVar()
auto_sale_event_check = tk.Checkbutton(
    window, text="AutoSteamSaleEvent", variable=auto_sale_event_var, **styles.CHECKBOX_STYLE)
auto_sale_event_check.grid(
    row=5, columnspan=2, padx=20, pady=(20, 0), sticky="w")

# Create the Generate button
generate_button = tk.Button(window, text="Generate", command=lambda: generate(
    file_entry, steam_id_entry, trade_token_entry, auto_sale_event_var), **styles.BUTTON_MAIN_STYLE)
generate_button.grid(row=6, columnspan=1, pady=(20, 0),
                     padx=(20, 0), sticky="w")


# Start the GUI event loop
window.mainloop()
