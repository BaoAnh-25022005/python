def count_vowels(s):
    vowels = "aeiouAEIOU"  # Danh sách các nguyên âm (cả chữ hoa và chữ thường)
    count = 0               # Biến đếm số nguyên âm

    for ch in s:            # Duyệt từng ký tự trong chuỗi
        if ch in vowels:    # Nếu ký tự là nguyên âm
            count += 1      # Tăng biến đếm lên 1

    return count            # Trả về tổng số nguyên âm

def main():
    s = "Artificial Intelligence"
    result = count_vowels(s)
    print(f"Số nguyên âm trong chuỗi '{s}' là:", result)

main()