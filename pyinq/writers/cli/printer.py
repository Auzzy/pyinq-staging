try:
	from _colorout import print_,to_str,to_plaintext
except ImportError as mess:
	def print_(text, fore=None, back=None, bright=True):
		print to_str(text, fore, back, bright)
	def to_str(text, fore=None, back=None, bright=True):
		return str(text)
	def to_plaintext(formatted_text):
		return formatted_text
