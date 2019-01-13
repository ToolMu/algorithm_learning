class KMP:
    def __init__(self, pattern):
        self._pattern_string = pattern
        self.failure_pointers = KMP._build_failure_pointer(pattern)

    def search(self, text):
        ret, pattern_index = [], 0

        for text_index, text_char in enumerate(text):
            while pattern_index > 0 and text_char != self._pattern_string[
                    pattern_index]:
                # 循环找到对应数据
                pattern_index = self.failure_pointers[pattern_index - 1]
            if text_char == self._pattern_string[pattern_index]:
                pattern_index += 1
            if pattern_index == len(self._pattern_string):
                ret.append(text_index - (pattern_index - 1))
                pattern_index = 0

        return ret

    @staticmethod
    def _build_failure_pointer(pattern):
        ret = [0]
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]

            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret


if __name__ == "__main__":
    pattern = "mumu"
    this_s = "this is mumu test"
    print(KMP(pattern).search(this_s))
