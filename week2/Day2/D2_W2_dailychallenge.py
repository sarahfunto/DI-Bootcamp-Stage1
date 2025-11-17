import math

class Pagination:
    def init(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range.")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def display_all_pages(self):
        titles = ""
        pages = ""
        for i in range(self.total_pages):
            start = i * self.page_size
            end = start + self.page_size
            page_items = self.items[start:end]
            titles += f"Page {i+1}".ljust(12)
            pages += f"{page_items}".ljust(12)
        print(titles)
        print(pages)

data = list("abcdefghi")  # 9 éléments
p = Pagination(data, page_size=3)
p.display_all_pages()   