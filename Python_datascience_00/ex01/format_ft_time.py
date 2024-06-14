from datetime import date
import time

seconds = time.time()
sec = format(round(seconds, 4), ',')
sci = format(seconds, '.2e')
print(f"Seconds since January 1, 1970: {sec} or {sci} in scientific notation")
today = date.today()
print(today.strftime("%b-%d %Y"))

# python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in
# scientific notation$
# Oct 21 2022$
