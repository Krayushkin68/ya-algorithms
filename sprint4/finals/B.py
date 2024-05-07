"""
https://contest.yandex.ru/contest/24414/run-report/114205358/

Реализация хэш таблицы с разрешением коллизий методом цепочек.
По условию задачи, ключи - целые числа. Сам ключ используется как хэш значение.
Индекс корзины вычисляется мультипликативным способом с использованием константы 1/Φ, что предоставляет равномерное распределение ключей по корзинам.
Также согласно условию количество ключей в таблице не превышает 10^5, поэтому используется количество корзин - 133_013 (простое число, примерно на треть большее чем 10^5).
Это позволит иметь среднюю длину цепочки равной 1.

Для оптимизации операции удаления используется маркерный элемент вместо удаления элемента из списка, так как удаление элемента из списка выполняется O(n), где n - длина списка.
(Хотя при средней длине цепочки равной 1 это не окажет особого влияния, все-таки может помочь в некоторых крайних ситуациях)

Сложность по времени (средняя): O(1), так как ключи распределены равномерно и средняя длина цепочки равна 1;
Сложность по памяти: O(N), где N - количество внесенных ключей в таблицу;
"""

from typing import Union


class HashTable:
    def __init__(self, num_buckets: int = 133_013):
        self._num_buckets = num_buckets
        self._buckets = [[] for _ in range(num_buckets)]
        self._skip_marker = object()

    def get(self, key: int) -> Union[int, None]:
        bucket_idx = self._get_bucket_idx(key)
        bucket = self._buckets[bucket_idx]

        for i, (bucket_key, bucket_value) in enumerate(bucket):
            if bucket_key == key:
                return bucket_value

        return None

    def put(self, key: int, value: int):
        bucket_idx = self._get_bucket_idx(key)
        bucket = self._buckets[bucket_idx]

        for i, (bucket_key, bucket_value) in enumerate(bucket):
            if bucket_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def delete(self, key: int):
        bucket_idx = self._get_bucket_idx(key)
        bucket = self._buckets[bucket_idx]

        for i, (bucket_key, bucket_value) in enumerate(bucket):
            if bucket_key == key:
                bucket[i] = (self._skip_marker, None)
                return bucket_value

    def _get_bucket_idx(self, key: int) -> int:
        return int(self._num_buckets * ((abs(key) * 0.6180339887) % 1))


def main():
    n = int(input())

    hash_map = HashTable()

    outputs = []
    for _ in range(n):
        command = input()

        if command.startswith('get'):
            key = int(command.split()[-1])
            value = hash_map.get(key)
            outputs.append(str(value))
        elif command.startswith('put'):
            key, value = map(int, command.split()[1:])
            hash_map.put(key, value)
        elif command.startswith('delete'):
            key = int(command.split()[-1])
            value = hash_map.delete(key)
            outputs.append(str(value))

    print('\n'.join(map(str, outputs)))


if __name__ == '__main__':
    main()
