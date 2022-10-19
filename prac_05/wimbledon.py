FILENAME = "wimbledon.csv"


def main():
    wimbledon_records = get_wimbledon_records(FILENAME)
    print(wimbledon_records)


def get_wimbledon_records(filename):
    wimbledon_records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            wimbledon_records.append(line.split(","))
        return wimbledon_records


main()
