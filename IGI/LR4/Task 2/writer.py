def save_result(results: dict, filename: str):
    """
    Saves the analysis results to a file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")