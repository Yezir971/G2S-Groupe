from src.transform import get_paths, loading_file


def main():
    # loading and transforming data from Excel file in the data directory
    loading_file(get_paths("./data"))

if __name__ == "__main__":
    main()