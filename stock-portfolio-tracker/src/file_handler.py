import csv
import os


class FileHandler:
    def save_csv(self, filepath, data):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["symbol", "quantity", "price", "value"]
            )
            writer.writeheader()
            writer.writerows(data)
