# -*- coding: utf-8 -*-
#
# Copyright 2017 Zuza Software Foundation
#
# This file is part of translate.
#
# translate is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# translate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""This module represents the Polish language.

.. seealso:: https://en.wikipedia.org/wiki/Polish_language
"""

from translate.lang import common


class pl(common.Common):
    """This class represents Polish."""

    validaccel = (u"abcdefghijklmnopqrstuvwxyz"
                  u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                  u"1234567890"
                  u"ąćęłńóśźż"
                  u"ĄĆĘŁŃÓŚŹŻ")
