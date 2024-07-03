
def ft_tqdm(lst: range) -> None:  # type: ignore
    """Function to display a progress bar"""
    total = len(lst)

    for idx, item in enumerate(lst):
        progress = (idx + 1) / total
        prcnt = int(progress * 100)
        bar = f"{prcnt}%|{'█' * prcnt}{' ' * (100 - prcnt)}| {idx + 1}/{total}"
        print(f"\r{bar}", end="")
        yield item
