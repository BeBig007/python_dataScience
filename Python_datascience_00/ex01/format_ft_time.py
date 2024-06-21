import time
from datetime import date


def main():
    seconds = time.time()
    sec = format(round(seconds, 4), ',')
    sci = format(seconds, '.2e')
    print(
        f"Seconds since January 1, 1970: {sec} or {sci} in scientific notation"
    )
    today = date.today()
    print(today.strftime("%b-%d %Y"))


if __name__ == "__main__":
    main()
