"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    [+] 1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    [+] 2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    [+] 3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""
from dataclasses import dataclass


@dataclass(slots=True)
class TextProcessor:
    text: str

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self) -> str:
        output = super().summarize()
        words_count = len(self.text.strip().split())
        output += f', total number of words in the text: {words_count}'
        return output


if __name__ == '__main__':
    textprocessor = TextProcessor(text='Hello World')
    print(textprocessor)
    print(textprocessor.to_upper())
    print(textprocessor.summarize())

    advacedtextprocessor = AdvancedTextProcessor(text='Hello World')
    print(advacedtextprocessor)
    print(advacedtextprocessor.to_upper())
    print(advacedtextprocessor.summarize())
