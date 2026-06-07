import re
from pathlib import Path
from typing import List, Dict


class EmailExtractor:
    """
    Professional email extraction service.
    """

    EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    def __init__(self, input_file: str, output_file: str):
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)

    def validate_file(self) -> None:
        if not self.input_file.exists():
            raise FileNotFoundError(
                f"Input file not found: {self.input_file}"
            )

    def read_file(self) -> str:
        with self.input_file.open("r", encoding="utf-8") as file:
            return file.read()

    def extract_emails(self, text: str) -> List[str]:
        emails = re.findall(self.EMAIL_PATTERN, text)
        return sorted(set(emails))

    def get_email_stats(self, emails: List[str]) -> Dict[str, int]:
        """
        Returns basic statistics about extracted emails.
        """
        domains = [email.split("@")[1] for email in emails]

        return {
            "total_emails": len(emails),
            "unique_domains": len(set(domains))
        }

    def save_emails(self, emails: List[str]) -> None:
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

        with self.output_file.open("w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
