import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a dataset from a CSV file and print its content.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Dataset as a pandas DataFrame.
    """
    try:
        assert isinstance(path, str), "the input must be string"
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as e:
        print(f"Error: {e}")
    return None
