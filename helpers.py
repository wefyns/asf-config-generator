import tkinter as tk
import webbrowser
import os
from tkinter import filedialog
import json
import tkinter.messagebox as messagebox


def open_url_steam():
    webbrowser.open('https://steamcommunity.com')


def open_url_trade_token():
    webbrowser.open('http://steamcommunity.com/my/tradeoffers/privacy')


def select_file(file_entry):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(tk.END, file_path)


def generate(file_entry, steam_id_entry, trade_token_entry, auto_sale_event_var):
    file_path = file_entry.get()
    steam_id = steam_id_entry.get()
    trade_token = trade_token_entry.get()
    auto_sale_event = auto_sale_event_var.get()

    # Create the 'results' directory if it doesn't exist
    os.makedirs("results", exist_ok=True)

    try:
        # Modify the script to use the selected file and write results to the /results directory
        with open(file_path, "r") as file:
            for line in file:
                login, password = line.strip().split(":")
                account_data = {
                    "AutoSteamSaleEvent": auto_sale_event,
                    "Enabled": True,
                    "SteamLogin": login,
                    "SteamPassword": password,
                    "SteamTradeToken": trade_token,
                    "SteamUserPermissions": {
                        steam_id: 3
                    },
                    "IdleRefundableGames": "false"
                }
                # Write result to /results directory
                json_file_name = f"results/{login}.json"
                with open(json_file_name, "w") as json_file:
                    json.dump(account_data, json_file, indent=4)
                print(f"Generated {json_file_name} successfully.")

        messagebox.showinfo("Success", "Generation completed successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The selected file does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during generation: {str(e)}")
