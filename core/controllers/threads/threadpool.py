'''
threadpool.py

Copyright 2006 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''

from multiprocessing.pool import ThreadPool
from multiprocessing.pool import RUN


__all__ = ['Pool']


class one_to_many(object):
    '''
    This is a simple wrapper that translates one argument to many in a function
    call. Useful for passing to the threadpool map function.
    '''
    def __init__(self, func):
        self.func = func
    
    def __call__(self, args):
        return self.func(*args)

    
class Pool(ThreadPool):
    def map_multi_args(self, func, iterable, chunksize=None):
        assert self._state == RUN
        return self.map_async(one_to_many(func), iterable, chunksize).get()
        