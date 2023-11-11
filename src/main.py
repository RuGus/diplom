import sys
from loguru import logger

from settings import WORKERS_COUNT
from worker import CryptoHubWorker

if __name__ == "__main__":
    # logging.getLogger("pika").propagate = False
    # logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    logger.info("Start workers")
    try:
        for worker_id in range(WORKERS_COUNT):
            worker_tread = CryptoHubWorker(worker_id)
            worker_tread.start()
    except Exception as exc:
        sys.stdout.write(f"Can't start API application: {str(exc)}")
