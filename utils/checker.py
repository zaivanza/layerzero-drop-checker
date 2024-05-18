from termcolor import cprint
import json
from pathlib import Path
import csv

def load_json(filepath: Path | str):
    with open(filepath, "r") as file:
        return json.load(file)
    
def read_txt(filepath: Path | str):
    with open(filepath, "r") as file:
        return [row.strip() for row in file]
    
def call_json(result: list | dict, filepath: Path | str):
    with open(f"{filepath}.json", "w") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

def get_layerzero_wallets():
    wallets = []
    cprint(f"Start checking ineligible wallets...", "white")
    with open("layerzero_wallets/wallets.csv", newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for i, row in enumerate(data):
            if "ADDRESS" in row:
                address = row["ADDRESS"].lower()
                wallets.append(address)
    cprint(f"Found {len(wallets)} ineligible wallets", "white")
    return wallets

class Checker:
    def __init__(self) -> None:
        self.wallets = [wallet.lower() for wallet in read_txt("wallets.txt")]
        self.layerzero_wallets = get_layerzero_wallets()

    def get_checked_wallets(self):
        ineligible_wallets = []
        eligible_wallets = []
        for wallet in self.wallets:
            if wallet in self.layerzero_wallets:
                ineligible_wallets.append(wallet)
            else:
                eligible_wallets.append(wallet)
        return eligible_wallets, ineligible_wallets
    
    def main(self):
        eligible_wallets, ineligible_wallets = self.get_checked_wallets()

        with open("results/eligible_wallets.txt", 'w') as file:
            for wallet in eligible_wallets:
                file.write(wallet + '\n')

        with open("results/ineligible_wallets.txt", 'w') as file:
            for wallet in ineligible_wallets:
                file.write(wallet + '\n')

        cprint("\n\nResults are recorded in results", "white")
        cprint(f"Eligible wallets: {len(eligible_wallets)} / {len(self.wallets)}\n", "green")
