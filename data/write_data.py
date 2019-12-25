import yaml

data = {
    "name": {"name1": 123, "name": {"nam": 111}, "name2": 234},
    "name1": {"name1": 123, "name": {"nam": 111, "name2": 234}},
    "values": {"001": [1, 2, 3]}
}
data1 = {
    "a,b,c": [(1, 2, 3), (2, 3, 5), (3, 4, 5)]
}
with open("./sun_data.yml", "w", encoding="utf-8") as f:
    yaml.safe_dump(data1, f, encoding="utf-8", allow_unicode=True)
