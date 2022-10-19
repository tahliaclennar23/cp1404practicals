FILENAME = "wimbledon.csv"


def main():
    wimbledon_records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            wimbledon_records.append(line)
        print(wimbledon_records)


main()
