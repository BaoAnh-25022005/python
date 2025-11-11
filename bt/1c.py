def average(numbers):
    if len(numbers) == 0:       # Nếu danh sách rỗng, trả về 0 để tránh lỗi chia cho 0
        return 0
    return sum(numbers) / len(numbers)   # Trung bình = tổng / số phần tử

def main():
    numbers = [4, 7, 2, 9, 5]
    avg = average(numbers)
    print("Giá trị trung bình của {numbers} là:", avg)

main()