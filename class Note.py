import json
import csv
from datetime import datetime

class Note:
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date