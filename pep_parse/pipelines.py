import csv
import datetime as dt
from pathlib import Path

from scrapy import Item, Spider

path = Path(__file__)

BASE_DIR = path.parent.parent
BASE_DIR_NAME = 'results'
TIME_FORMAT = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


class PepParsePipeline:
    status_count = {}
    total = 0

    def open_spider(self, spider: Spider) -> None:
        result_dir = BASE_DIR / BASE_DIR_NAME
        result_dir.mkdir(exist_ok=True)

    def process_item(self, item: Item, spider: Spider) -> Item:
        if item.get('status'):
            self.total += 1
            self.status_count[
                item['status']] = self.status_count.get(
                item['status'], 0) + 1
        return item

    def close_spider(self, spider: Spider) -> None:
        results = [('Статус', 'Количество')]
        for k, v in self.status_count.items():
            results.append((k, v))
        results.append(('Total ', self.total))

        filename = f'status_summary_{TIME_FORMAT}.csv'
        filepath = BASE_DIR / BASE_DIR_NAME / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(results)
