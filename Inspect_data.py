import csv

def read_rows(path):
 with open(path,newline="", encoding="utf-8-sig")as f:
   return list(csv.DictReader(f))

def to_number(text):
    text = text.strip().replace(",","")
    if text == "" or text.upper() in ("NA", "N/A", "NULL","-"):
        return None
    try:
      return float(text)
    except ValueError:
      return None
def summarise_column(rows, column):
    values = []
    for row in rows:
        n = to_number(row[column])
        if n is not None:
           values.append(n)
    return {"count": len(values),"smallest": min(values),"largest": max(values),"average": sum(values) / len(values),}
rows = read_rows("Week 8/Adentan settlement.csv")
print(summarise_column(rows, "AREA"))
print(summarise_column(rows, "PERIMETER"))
            
