import sys

from settings import WORKERS_COUNT
from worker import CryptoHubWorker

if __name__ == "__main__":
    try:
        for i in range(WORKERS_COUNT):
            worker_tread = CryptoHubWorker()
            worker_tread.start()
    except Exception as exc:
        sys.stdout.write(f"Can't start API application: {str(exc)}")
