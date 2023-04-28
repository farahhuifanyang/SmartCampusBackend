import psycopg2


def read_csv(path):
    with open(path, "r", encoding="UTF-8") as f:
        f.readline()  # Discard the header

        lines = []
        for line in f.readlines():
            line = line.strip()
            if line[-1] == '|':
                line = line[:-1]  # Remove the tailing ","
            lines.append(line)

    return [line.split(',') for line in lines]


def save_to_db(scholar_lt):
    sql_template = "insert into scholar_teacherstudents values ({})".format(",".join(["%s"]*3))

    conn = psycopg2.connect(
        host='10.105.222.6',
        port='41466',
        password='qU9rgx!31^2n',
        dbname='smartcampus',
        user='acdev'
    )
    cursor = conn.cursor()

    for scholar in scholar_lt:
        cursor.execute(sql_template, scholar)

    cursor.close()
    conn.commit()
    conn.close()


def main():
    scholar_lt = read_csv("/home/data/SmartCampus/olddata/原有数据/teacher_students.csv")
    save_to_db(scholar_lt)


if __name__ == "__main__":
    main()
