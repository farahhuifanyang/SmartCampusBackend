import os
import json
import psycopg2
from psycopg2.errors import UniqueViolation


paper_path = "/home/data/SmartCampus/olddata/mag/tea"


def get_all_keys():
    keys = set()
    for file_name in os.listdir(paper_path):
        with open(os.path.join(paper_path, file_name), "rb") as fp:
            for line in fp.readlines():
                d = json.loads(line)
                for key in d:
                    keys.add(key)
    return keys


order = ['url', 'volume', 'fos', 'issue', 'year', 'authors', 'lang', 'doc_type', 'page_end', 'publisher', 'n_citation', 'abstract', 'venue', 'page_start', 'doi', 'title', 'id', 'keywords']
paper_sql = "insert into scholar_papers values ({})".format(','.join(["%s"] * len(order)))
by_author_paper_sql = "insert into scholar_byauthorpaper values (%s, %s, %s)"
ref_sql = "insert into scholar_byauthorpaper values (%s, %s, %s)"


def maybe_join(arg):
    if arg is None or isinstance(arg, str) or isinstance(arg, int):
        return arg
    if len(arg) > 0 and isinstance(arg[0], dict):
        return ','.join([d['name'] for d in arg])
    if isinstance(arg, list):
        return ','.join(arg)
    raise TypeError("Encountered type {}".format(type(arg)))


ref_cnt, by_cnt = 0, 0
def upload_paper(cursor, conn, paper: dict):
    global ref_cnt, by_cnt
    paper_args = [maybe_join(paper.get(key)) for key in order]
    try:
        cursor.execute(paper_sql, paper_args)
    except UniqueViolation:
        conn.commit()

    if "id" in paper:
        by_author_paper_args = [by_cnt, paper['by_author'], paper['id']]
        by_cnt += 1
        cursor.execute(by_author_paper_sql, by_author_paper_args)

    if "id" in paper and "reference" in paper:
        this_id = paper["id"]
        for pid in paper['references']:
            cursor.execute(ref_sql, [ref_cnt, this_id, pid])
            ref_cnt += 1
    conn.commit()


def upload_all(cursor, conn):
    for file_name in os.listdir(paper_path):
        by_author = file_name.split('.')[0]
        with open(os.path.join(paper_path, file_name), "rb") as fp:
            for line in fp.readlines():
                d = json.loads(line)
                d["by_author"] = by_author
                upload_paper(cursor, conn, d)

def main():
    conn = psycopg2.connect(
        host='10.105.222.6',
        port='41466',
        password='qU9rgx!31^2n',
        dbname='smartcampus',
        user='acdev'
    )
    cursor = conn.cursor()

    upload_all(cursor, conn)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
