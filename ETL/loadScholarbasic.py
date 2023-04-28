import psycopg2


def read_csv(path):
    with open(path, "r", encoding="UTF-8") as f:
        f.readline()  # Discard the header

        scholar_lt = []
        for line in f.readlines():
            line = line.strip()
            if len(line) > 0:
                if line[:2] == "by":
                    scholar_lt.append(line)
                else:
                    scholar_lt[-1] += line

    return [scholar.split(',') for scholar in scholar_lt]


def save_to_db(scholar_lt):
    sql_template = "insert into scholar_scholarbasicinfo values ({})".format(",".join(["%s"]*15))

    conn = psycopg2.connect(
        host='10.105.222.6',
        port='41466',
        password='qU9rgx!31^2n',
        dbname='smartcampus',
        user='acdev'
    )
    cursor = conn.cursor()

    for scholar in scholar_lt:
        scholar[0] = int(scholar[0][2:])
        cursor.execute(sql_template, scholar)

    conn.commit()
    conn.close()
    cursor.close()


def main():
    scholar_lt = read_csv("/home/data/SmartCampus/olddata/mag/beiyou.csv")
    save_to_db(scholar_lt)


if __name__ == "__main__":
    main()
