import unittest
from name_function import get_formatted_name


# 继承unittest.TestCase类，这样Python才知道如何运行你编写的测试
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    # 运行test_name_function.py时，所有以test_ 打头的方法都将自动运行
    def test_first_last_name(self):
        """能够正确的处理像Janis Joplin这样的姓名吗"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')   #断言 方法，将formatted_name 的值与字符串'Janis Joplin' 比较
    def test_first_last_middle_name(self):
        """能够正确处理像Janis A Joplin这样的姓名吗"""
        formatted_name = get_formatted_name('janis', 'joplin', 'a')
        self.assertEqual(formatted_name, 'Janis A Joplin')

if __name__ == '__main__':
    unittest.main()


