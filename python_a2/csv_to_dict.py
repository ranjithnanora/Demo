
def csv_to_dict(filepath):
    with open(filepath,"rt") as file:
        dictionary=dict()
        for line in file:
            key,value=line.strip().split(",")
            dictionary[key]=value
        print(dictionary)

def test(filepath):
    csv_to_dict(filepath)
paths=["details.csv", "marks.csv"]
for path in paths:
    test(path)
