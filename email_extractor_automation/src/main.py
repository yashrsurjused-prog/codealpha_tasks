from src.email_extractor import EmailExtractor
from src.logger_config import setup_logger


def main():
    logger = setup_logger()

    input_file = "data/input.txt"
    output_file = "data/extracted_emails.txt"

    try:
        logger.info("Starting Email Extraction Process...")

        extractor = EmailExtractor(input_file, output_file)

        extractor.validate_file()

        text = extractor.read_file()

        emails = extractor.extract_emails(text)

        extractor.save_emails(emails)

        stats = extractor.get_email_stats(emails)

        logger.info("Extraction completed successfully")

        print("\n" + "=" * 50)
        print(" EMAIL EXTRACTION REPORT")
        print("=" * 50)
        print(f"Total Emails Found   : {stats['total_emails']}")
        print(f"Unique Domains       : {stats['unique_domains']}")
        print(f"Output File          : {output_file}")
        print("=" * 50 + "\n")

    except FileNotFoundError as e:
        logger.error(str(e))
        print(f"Error: {e}")

    except Exception as e:
        logger.exception("Unexpected error occurred")
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
