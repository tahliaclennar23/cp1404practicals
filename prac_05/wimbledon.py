"""
Tahlia Clennar
CP1404 Practical 05- Game, Set, Match
Program to read and process Wimbledon data.
Estimate:50 minutes
Actual time: 1 hour (with breaks)

"""

FILENAME = "wimbledon.csv"
CHAMPIONS_INDEX = 2
COUNTRY_INDEX = 1


def main():
    """Read wimbledon.csv data, process and display it"""
    wimbledon_records = get_wimbledon_records(FILENAME)
    countries, champions_to_count = get_champions(wimbledon_records)
    display_wimbledon_records(countries, champions_to_count)


def get_wimbledon_records(filename):
    """Get Wimbledon records"""
    wimbledon_records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            wimbledon_records.append(line.split(","))
        return wimbledon_records


def get_champions(wimbledon_records):
    """Get champions and how many times they won"""
    champions_to_count = {}
    countries = set()
    for record in wimbledon_records:
        countries.add(record[COUNTRY_INDEX])
        champions_to_count[record[CHAMPIONS_INDEX]] = champions_to_count.get(record[CHAMPIONS_INDEX], 0) + 1
    return countries, champions_to_count


def display_wimbledon_records(countries, champions_to_count):
    """Display champions, how many times they won and sort countries"""
    print("Wimbledon Champions: ")
    for champions in champions_to_count:
        print(f"{champions} {champions_to_count[champions]}")
    print(f"\nThese {len(countries)} have won Wimbledon: ")
    print(", ".join(sorted(countries)))


main()
