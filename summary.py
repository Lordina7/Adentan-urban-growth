import csv
def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig")as f:
        return list(csv.DictReader(f))

def clean_values(rows, column):
    values = []
    for row in rows:
        text = row[column].strip().replace(",", "")
        if text  == "" or text.upper()in ("NA", "N/A", "NULL", "-"):
            continue
        try:
            values.append(float(text))
        except ValueError:
            pass
    return values

def summarise(values):
    return {"count": len(values), "smallest": min(values), "largest": max(values), "average": sum(values)/ len(values),}


def summarise_all(rows, columns):
    for column in columns:
        s = summarise(clean_values(rows, column))
        print(f"{column}: count={s['count']}, smallest={s['smallest']}, largest={s['largest']}, average={s['average']: .2f}")

rows = read_rows("Week 8/Adentan settlement.csv")
summarise_all(rows, ["AREA", "PERIMETER"]) 
