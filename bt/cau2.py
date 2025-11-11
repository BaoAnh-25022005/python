class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id    # Mã sách
        self.title = title        # Tên sách
        self.author = author      # Tác giả
        self.price = price        # Giá bán

    # Phương thức hiển thị thông tin sách
    def display_info(self):
        print(f"Mã sách: {self.book_id}")
        print(f"Tên sách: {self.title}")
        print(f"Tác giả: {self.author}")
        print(f"Giá bán: {self.price:,} VNĐ")
        print("-" * 30)


# -----------------------------
# Lớp Library: quản lý danh sách các sách
# -----------------------------
class Library:
    def __init__(self):
        self.books = []   # Danh sách các đối tượng Book

    # Thêm một cuốn sách vào thư viện
    def add_book(self, book):
        self.books.append(book)

    # Tìm sách theo tên tác giả
    def search_by_author(self, author_name):
        result = []
        for book in self.books:
            if book.author.lower() == author_name.lower():  # So sánh không phân biệt hoa/thường
                result.append(book)
        return result

    # Tính tổng giá trị các sách trong thư viện
    def get_total_value(self):
        total = sum(book.price for book in self.books)
        return total

def main():
    # Tạo đối tượng thư viện
    library = Library()

    # Tạo ít nhất 3 cuốn sách
    book1 = Book("B001", "Cho tôi xin một vé đi tuổi thơ", "Nguyễn Nhật Ánh", 65000)
    book2 = Book("B002", "Tôi thấy hoa vàng trên cỏ xanh", "Nguyễn Nhật Ánh", 75000)
    book3 = Book("B003", "Dế Mèn phiêu lưu ký", "Tô Hoài", 55000)

    # Thêm sách vào thư viện
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # In ra toàn bộ thông tin sách trong thư viện
    print(" DANH SÁCH SÁCH TRONG THƯ VIỆN:")
    print("-" * 30)
    for book in library.books:
        book.display_info()

    # Tìm sách của tác giả "Nguyễn Nhật Ánh"
    print("\n CÁC SÁCH CỦA TÁC GIẢ 'Nguyễn Nhật Ánh':")
    found_books = library.search_by_author("Nguyễn Nhật Ánh")
    if found_books:
        for book in found_books:
            book.display_info()
    else:
        print("Không tìm thấy sách của tác giả này!")

    # In tổng giá trị sách trong thư viện
    total_value = library.get_total_value()
    print(f"\n Tổng giá trị các sách trong thư viện: {total_value:,} VNĐ")


main()