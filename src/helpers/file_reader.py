import xml.etree.ElementTree as element_tree

def read_xml(filename, tag):
	tree = element_tree.parse(filename)
	root = tree.getroot()

	tag_content = root.find(tag).text
	return tag_content.strip()

