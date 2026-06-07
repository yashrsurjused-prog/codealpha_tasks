from portfolio import Portfolio
from file_handler import FileHandler
from logger import setup_logger


def main():
    logger = setup_logger()
    logger.info("Program started")

    print("=== STOCK PORTFOLIO TRACKER ===")

    portfolio = Portfolio()

    while True:
        try:
            symbol = input("Enter stock symbol (or DONE): ").upper()

            if symbol == "DONE":
                break

            quantity = int(input("Enter quantity: "))

            portfolio.add_stock(symbol, quantity)

        except ValueError as e:
            print("Error:", e)
        except KeyError as e:
            print("Error:", e)

    summary = portfolio.summary()
    total = portfolio.calculate_total()

    print("\n--- PORTFOLIO ---")
    for item in summary:
        print(item)

    print("\nTOTAL INVESTMENT:", total)

    FileHandler().save_csv("data/portfolio_output.csv", summary)

    logger.info(f"Total investment: {total}")
    logger.info("Data saved successfully")

    print("\nSaved successfully!")


if __name__ == "__main__":
    main()
