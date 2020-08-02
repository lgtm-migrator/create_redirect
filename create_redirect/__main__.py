#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __main__.py
"""
Generate HTML Redirect File
"""
#
#  Copyright (c) 2015, 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

# stdlib
import argparse
import os
import sys


def main():
	parser = argparse.ArgumentParser(description='Generate HTML Redirect File.')
	parser.add_argument('redirect_url', help='The URL to redirect to')
	parser.add_argument('output', nargs='?', default="redirect.html", help='Path of the file to create')

	args = parser.parse_args()
	if not args.redirect_url.startswith('http'):
		url = f"http://{args.redirect_url}"
	else:
		url = args.redirect_url

	output_file = os.path.join(os.getcwd(), args.output)

	with open(output_file, 'w') as f:
		f.write(
				"""<!DOCTYPE HTML>
	<html lang="en-GB">
		<head>
			<meta charset="UTF-8">
			<meta http-equiv="refresh" content="1";url='{0}'>
			<script type="text/javascript">
				window.location.href = '{0}'
			</script>
			<title>Page Redirection</title>
		</head>
		<body>
			<!-- Note: don't tell people to `click` the link, just tell them that it is a link. -->
			If you are not redirected automatically, follow the <a href='{0}'>link</a>
		</body>
	</html>""".format(url)
				)

	print(f"Successfully written file '{output_file}' with url '{url}'")

	return 0


if __name__ == "__main__":
	sys.exit(main())
