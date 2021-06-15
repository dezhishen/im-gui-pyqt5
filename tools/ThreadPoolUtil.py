from concurrent.futures import ThreadPoolExecutor
from concurrent.futures._base import Future


class _ThreadPool:
    _pool: ThreadPoolExecutor = None

    def __init__(self) -> None:
        self._pool = ThreadPoolExecutor(20)
        pass

    def submit(self, fn, /, *args, **kwargs) -> Future:
        """Submits a callable to be executed with the given arguments.

        Schedules the callable to be executed as fn(*args, **kwargs)\
            and returns
        a Future instance representing the execution of the callable.

        Returns:
            A Future representing the given call.
        """
        f = self._pool.submit(fn,  *args, **kwargs)
        return f


THREAD_POOL = _ThreadPool()
