#!/usr/bin/env python
# coding: utf-8

"""
   File Name: bitmap.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Thu May  1 15:26:18 2014 CST
"""
DESCRIPTION = """
BitMap class
"""

import array


class BitMap(object):
    """
    BitMap class
    """

    BITMASK = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
    BIT_CNT = [bin(i).count("1") for i in range(256)]

    def __init__(self, maxnum=0):
        """
        Create a BitMap
        """
        nbytes = (maxnum + 7) // 8
        self.bitmap = array.array('B', [0 for i in range(nbytes)])

    def __del__(self):
        """
        Destroy the BitMap
        """
        pass

    def set(self, pos):
        """
        Set the value of bit@pos to 1
        """
        self.bitmap[pos // 8] |= self.BITMASK[pos % 8]

    def reset(self, pos):
        """
        Reset the value of bit@pos to 0
        """
        self.bitmap[pos // 8] &= ~self.BITMASK[pos % 8]

    def flip(self, pos):
        """
        Flip the value of bit@pos
        """
        self.bitmap[pos // 8] ^= self.BITMASK[pos % 8]

    def count(self):
        """
        Count bits set
        """
        return sum([self.BIT_CNT[x] for x in self.bitmap])

    def size(self):
        """
        Return size
        """
        return len(self.bitmap) * 8

    def test(self, pos):
        """
        Return bit value
        """
#         print('pos:', pos, type(pos))
        return (self.bitmap[pos // 8] & self.BITMASK[pos % 8]) != 0

    def any(self):
        """
        Test if any bit is set
        """
        return self.count() > 0

    def none(self):
        """
        Test if no bit is set
        """
        return self.count() == 0

    def all(self):
        """
        Test if all bits are set
        """
        return (self.count() + 7) // 8 * 8 == self.size()

    def nonzero(self):
        """
        Get all non-zero bits
        """
        return [i for i in range(self.size()) if self.test(i)]

    def tostring(self):
        """
        Convert BitMap to string
        """
        return "".join([("%s" % bin(x)[2:]).zfill(8)
                        for x in self.bitmap[::-1]])

    def __str__(self):
        """
        Overloads string operator
        """
        return self.tostring()

    def __getitem__(self, item):
        """
        Return a bit when indexing like a array
        """
        return self.test(item)

    def __setitem__(self, key, value):
        """
        Sets a bit when indexing like a array
        """
        if value is True:
            self.set(key)
        elif value is False:
            self.reset(key)
        else:
            raise Exception("Use a boolean value to assign to a bitfield")

    def tohexstring(self):
        """
        Returns a hexadecimal string
        """
        val = self.tostring()
        st = "{0:0x}".format(int(val, 2))
        return st.zfill(len(self.bitmap)*2)

    @classmethod
    def fromhexstring(cls, hexstring):
        """
        Construct BitMap from hex string
        """
        bitstring = format(int(hexstring, 16), "0" + str(len(hexstring)/4) + "b")
        return cls.fromstring(bitstring)

    @classmethod
    def fromstring(cls, bitstring):
        """
        Construct BitMap from string
        """
        nbits = len(bitstring)
        bm = cls(nbits)
        for i in range(nbits):
            if bitstring[-i-1] == '1':
                bm.set(i)
            elif bitstring[-i-1] != '0':
                raise Exception("Invalid bit string!")
        return bm
