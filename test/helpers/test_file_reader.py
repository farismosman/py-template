import unittest
import src.helpers.file_reader as reader

class TestFileReader(unittest.TestCase):
	
	def test_read_xml_by_tag_should_read_tag_content(self):
		filename = 'resources/test_file.xml'

		xml_content = reader.read_xml(filename, "content")

		self.assertEqual(xml_content, "here is the content")


if __name__ == '__main__':
	unittest.main()
