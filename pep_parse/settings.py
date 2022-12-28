from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }

}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = Path(__file__).parent
BASE_DIR_NAME = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
CSV_TITLE = ('Статус', 'Количество')
ENCODING = 'utf-8'
FILE_FORMAT = 'csv'
