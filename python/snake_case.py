def get_snake_case(input_val):
    re_val = ""

    for i, idx in enumerate(input_val):
        if i == 0 and not idx.islower():
            re_val = idx.lower()
        else:
            if not idx.islower():
                rep = input_val[i]
                re_val = re_val + "_" + rep.lower()
            else:
                re_val += idx
    print(re_val)


if __name__ == "__main__":
    get_snake_case("ohYeonjoo")
    get_snake_case("OhYeonJoo")
    get_snake_case("OhYeonJooA")
    get_snake_case("AAAAAAAAAAAAAA")
    get_snake_case("A")

