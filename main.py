from src.logs import logger
from src.settings import WORKERS_COUNT
from src.worker import CryptoHubWorker

if __name__ == "__main__":
    logger.info("Start workers")
    try:
        for worker_id in range(WORKERS_COUNT):
            worker_tread = CryptoHubWorker(worker_id)
            worker_tread.start()
    except Exception as exc:
        logger.error(f"Can't start workers: {str(exc)}")
