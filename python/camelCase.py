def getCamelCase(inputValue):
    # if first, end index is '_', let delete
    inputValue = inputValue.strip("_")

    # push arrList base on splited '_'
    arr = inputValue.split("_")
    reVal = ""

    for i, idx in enumerate(arr):
        arr[i] = arr[i].lower()
        if i == 0:
            reval += str(arr[i])
        else:
            reval += str(arr[i].capitalize())
            
    print(reVal)  # return value

    
if __name__ == "__main__":
    getCamelCase("_test_case_yeon_joo")
    getCamelCase("_test_case_yeon_joo_")
    getCamelCase("teEt_case__________yeon_joo")
    getCamelCase("TEST_case_yeon_jOo")
    getCamelCase("________TEST_case_yeon_jOo")
    getCamelCase("________TEST_case_yeon_jOo_______________")
