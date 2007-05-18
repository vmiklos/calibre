##    Copyright (C) 2006 Kovid Goyal kovid@kovidgoyal.net
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
Provides metadata editing support for PDF and RTF files. For LRF metadata, use 
the L{libprs500.lrf.meta} module.
"""
__docformat__ = "epytext"
__author__       = "Kovid Goyal <kovid@kovidgoyal.net>"


class MetaInformation(object):
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.comments = None
        self.category = None
        self.classification = None
        self.publisher = None
        
    def __str__(self):
        ans = ''
        ans += 'Title   : ' + str(self.title) + '\n'
        ans += 'Author  : ' + str(self.author) + '\n'
        ans += 'Category: ' + str(self.category) + '\n'
        ans += 'Comments: ' + str(self.comments) + '\n'
        return ans.strip()
    
    def __nonzero__(self):
        return self.title or self.author or self.comments or self.category