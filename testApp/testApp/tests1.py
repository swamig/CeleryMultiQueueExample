from logentries import LogentriesHandler
import logging

log = logging.getLogger('logentries')
log.setLevel(logging.INFO)
# Note if you have set up the logentries handler in Django, the following line is not necessary
log.addHandler(LogentriesHandler('1d18731d-53e4-41cd-b417-9ef4da1552c2'))

log.info("test1 worker no worker")




def tryLogTest1Attempt1(inputInfo):
	log.info("test 1 worker attempt 1")
	log.info(inputInfo)


def tryLogTest1Attempt1(inputInfo):
	log.info("test 1 worker attempt 2")
	log.info(inputInfo)
