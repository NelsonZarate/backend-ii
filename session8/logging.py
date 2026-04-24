import logging

logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    filename="app.log",
	encoding="utf-8",
)
logging.error("Something went wrong!")
logging.warning("Warning logging")
logging.info("Logging info")

def main():
    print("Hello from session8!")


if __name__ == "__main__":
    main()
