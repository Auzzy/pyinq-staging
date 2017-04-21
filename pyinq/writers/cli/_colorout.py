from StringIO import StringIO

import colorama
from colorama.ansitowin32 import AnsiToWin32
colorama.init()

from pyinq.writers.cli import colors

_FORE_MAP = {
	colors.RED: colorama.Fore.RED,
	colors.YELLOW: colorama.Fore.YELLOW,
	colors.GREEN: colorama.Fore.GREEN,
	colors.CYAN: colorama.Fore.CYAN,
	colors.BLUE: colorama.Fore.BLUE,
	colors.MAGENTA: colorama.Fore.MAGENTA,
	colors.WHITE: colorama.Fore.WHITE,
	colors.BLACK: colorama.Fore.BLACK
}
_BACK_MAP = {
	colors.RED: colorama.Back.RED,
	colors.YELLOW: colorama.Back.YELLOW,
	colors.GREEN: colorama.Back.GREEN,
	colors.CYAN: colorama.Back.CYAN,
	colors.BLUE: colorama.Back.BLUE,
	colors.MAGENTA: colorama.Back.MAGENTA,
	colors.WHITE: colorama.Back.WHITE,
	colors.BLACK: colorama.Back.BLACK
}

def _get_color(color, color_map, reset):
	if color:
		if color not in color_map:
			raise ValueError("Unsupported color provided.".format(label=label))
		return color_map[color]
	else:
		return reset

def print_(text, fore=None, back=None, bright=True):
	print to_str(text, fore, back, bright)

def to_str(text, fore=None, back=None, bright=True):
	fore_color = _get_color(fore, _FORE_MAP, colorama.Fore.RESET)
	back_color = _get_color(back, _BACK_MAP, colorama.Back.RESET)
	style = colorama.Style.BRIGHT if bright else colorama.Style.NORMAL

	return "{fore}{back}{style}{text}{reset}".format(fore=fore_color, back=back_color, style=style, text=text, reset=colorama.Style.RESET_ALL)

def to_plaintext(formatted_text):
	stringbuf = StringIO()
	strip_ansi = AnsiToWin32(stringbuf, strip=True, convert=False)
	strip_ansi.write_and_convert(formatted_text)
	return stringbuf.getvalue()
