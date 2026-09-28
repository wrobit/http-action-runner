from runner import Runner

PATH = "https://dummyjson.com"


def main():
    runner = Runner(PATH)
    print(runner.get_path())


if __name__ == "__main__":
    main()
