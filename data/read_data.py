import yaml, os


def read_yaml_data(yaml_name):
    with open(f"./data{os.sep}{yaml_name}","r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# def read_yaml_data(yaml_name):
#     with open(f"./{yaml_name}", "r", encoding="utf-8") as f:
#         return yaml.safe_load(f)


if __name__ == '__main__':
    print(read_yaml_data("mms_data.yaml"))
    # print(read_data().values())
    # data = [tuple(o) for i in read_data().values() for o in i]
    # print(data)
    # print(read_data().get("values3"))
    # print(read_data().get("values4"))
    # print(type(list(read_data().values())))
    # print(type(read_data().get("mmsa3")))
