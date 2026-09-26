import ctypes

class CommonList:
    def __init__(self):
        self._length = 0
        self._capacity = 1
        self._array = self.make_array(self._capacity)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if not 0 <= index < self._length:
            raise IndexError("Out of range")
        return self._array[index]

    def append_to_common_list(self,item):
        if self._length == self._capacity:
            self._resize(2*self._capacity)

        self._array[self._length] = item
        self._length += 1

    def _resize(self,new_capacity):
        #создание нового списка
        new_array = self.make_array(new_capacity)
        #Копирование старых элементов в новый список
        for i in range(self._length):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity

    def _make_array(self, capacity):

