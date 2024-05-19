from analyzer import analyze_text
from writer import save_result
from archiver import archive_result

def main():
    source_filename = "Task 2/text.txt"
    result_filename = "Task 2/analysis_results.txt"
    archive_filename = "Task 2/analysis_results.zip"

    with open(source_filename, 'r', encoding='utf-8') as file:
        text = file.read()

    analysis_results = analyze_text(text)
    
    print_results(analysis_results)
                
    save_result(analysis_results, result_filename)

    archive_result(result_filename, result_filename, archive_filename)

    print("Analysis completed and results saved.")


def print_results(results: dict):
    """
    This function prints analyzing text results
    """
    for key, value in results.items():
        if type(value) == list:
            print(f"{key}: ")
            for item in value:
                print(item)
        elif type(value) == dict:
            print(f"{key}: ", end='')
            for k,v in value.items():
                print(f"{k}: {v}")
        else:
            print(f"{key}: {value}")
        print()

if __name__ == "__main__":
    main()