import csv
import datetime as dt

from scrapy import Item, Spider
from settings import (BASE_DIR, BASE_DIR_NAME,
                      TIME_FORMAT, CSV_TITLE, ENCODING, FILE_FORMAT)


class PepParsePipeline:
    status_count = {}
    total = 0

    def open_spider(self, spider: Spider) -> None:
        result_dir = BASE_DIR.parent / BASE_DIR_NAME
        result_dir.mkdir(exist_ok=True)

    def process_item(self, item: Item, spider: Spider) -> Item:
        if item.get('status'):
            self.total += 1
            self.status_count[
                item['status']] = self.status_count.get(
                item['status'], 0) + 1
        return item

    def close_spider(self, spider: Spider) -> None:
        results = [CSV_TITLE]
        for k, v in self.status_count.items():
            results.append((k, v))
        results.append(('Total ', self.total))
        fileformat = dt.datetime.now().strftime(TIME_FORMAT)
        filename = f'status_summary_{fileformat}.{FILE_FORMAT}'
        filepath = BASE_DIR / BASE_DIR_NAME / filename

        with open(filepath, 'w', encoding=ENCODING) as f:
            writer = csv.writer(f)
            writer.writerows(results)
