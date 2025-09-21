from typing import List

class LabelStore:
    def __init__(self):
        # Program başladığında hazır
        self.labels: List[str] = []

    def get(self) -> List[str]:
        return self.labels

    def set(self, labels: List[str]) -> None:
        self.labels.clear()
        self.labels.extend(labels)

# Tek instance olarak oluştur
label_store = LabelStore()
