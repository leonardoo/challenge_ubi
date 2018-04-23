def find_peaks(array):
    peaks = 0
    valleys = 0
    i = 0
    while i < len(array):
        data = array[i]
        left = array[i - 1] if i > 0 else None
        rigth = array[i + 1] if i < len(array) - 1 else None
        if check_index_is_peak(data, left, rigth):
            peaks += 1
            if left:
                valleys += 1
            if rigth:
                valleys += 1
        i += 1
    return peaks, valleys


def check_index_is_peak(data, left, rigth):
    is_left = True
    if left:
        is_left = data > left
    is_rigth = True
    if rigth:
        is_rigth = data > rigth
    if not left and not rigth:
        return False
    return is_rigth and is_left

if __name__ == "__main__":
    data = input("add the array separated by comma: ")
    array = [int(i.strip()) for i in data.split(",")]
    if array > 0 and array < 500:
        peaks, valleys = find_peaks(array)
        print("the arrays has: {} peaks and {} valleys".format(peaks, valleys))
    else:
        print("not valid array")
