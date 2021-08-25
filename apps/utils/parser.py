from openpyxl import load_workbook

from apps.diary.models import Diary
from django.contrib.auth import get_user_model

def _get(data, index):
    try:
        return data[index].value

    except IndexError:
        return None


def load(path, worksheet):
    wb = load_workbook(path, read_only=True)
    ws = wb[worksheet]
    return ws


def parse():

    worksheets = ['시트1']

    for ws in worksheets:
        data = load('apps/utils/data.xlsx', ws)
        first_row = False

        for row in data.rows:

            if not first_row:
                first_row = True
                continue
            

            title = _get(row, 0)
            content = _get(row, 1)
            author = _get(row, 2)
            is_private = _get(row, 3)
            created_at = _get(row, 4)

            author_model, _ = get_user_model().objects.get_or_create(username=author, name=author, password='aassddff')

            diary = Diary.objects.create(title=title, content=content, author=author_model, is_private=is_private, created_at=created_at, score=0, magnitude=0)
            diary.update_score()

            print('{} - {}'.format(author, title))

