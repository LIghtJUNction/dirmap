#!/usr/bin/env python3

'''
@Author: xxlin
@LastEditors: xxlin
@Date: 2019-04-10 13:27:58
@LastEditTime: 2019-04-11 15:57:17
'''

"""
getTerminalSize()
 - get width and height of console
 - works on linux,os x,windows,cygwin(windows)
"""

import os

__all__ = ['getTerminalSize']


def getTerminalSize():
    import platform
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _getTerminalSize_windows()
        if tuple_xy is None:
            tuple_xy = _getTerminalSize_tput()
            # needed for window's python in cygwin's xterm!
    if current_os == 'Linux' or current_os == 'Darwin' or current_os.startswith('CYGWIN'):
        tuple_xy = _getTerminalSize_linux()
    if tuple_xy is None:
        tuple_xy = (80, 25)  # default value
    return tuple_xy


def _getTerminalSize_windows():
    res = None
    try:
        from ctypes import windll, create_string_buffer

        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12

        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
    except Exception:
        return None
    if res:
        import struct
        (bufx, bufy, curx, cury, wattr,
         left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        sizex = right - left + 1
        sizey = bottom - top + 1
        return sizex, sizey
    else:
        return None


def _getTerminalSize_tput():
    # get terminal width
    # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
    try:
        import subprocess
        proc = subprocess.Popen(["tput", "cols"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output = proc.communicate(input=None)
        cols = int(output[0])
        proc = subprocess.Popen(["tput", "lines"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output = proc.communicate(input=None)
        rows = int(output[0])
        return (cols, rows)
    except Exception:
        return None


def _getTerminalSize_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            import termios
            import struct
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        except Exception:
            return None
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except Exception:
            pass
    if not cr:
        try:
            cr = (env.get('LINES'), env.get('COLUMNS'))
        except Exception:
            return None
    return int(cr[1]), int(cr[0])

