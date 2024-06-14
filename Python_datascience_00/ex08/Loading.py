
def ft_tqdm(lst: range) -> None:
    """_summary_

    Args:
        lst (range): _description_
    """
    total = len(lst)

    for idx, item in enumerate(lst):
        progress = (idx + 1) / total
        progress_percent = int(progress * 100)
        progress_bar = f"{progress_percent}%|{'█' * progress_percent}{' ' * (100 - progress_percent)}| {idx + 1}/{total}"
        print(f"\r{progress_bar}", end="")
        yield item
