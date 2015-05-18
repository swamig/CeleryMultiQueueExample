from logentries import LogentriesHandler
import logging
import celery
from django.conf import settings 

# log = logging.getLogger('logentries')
# log.setLevel(logging.INFO)
# # Note if you have set up the logentries handler in Django, the following line is not necessary
# log.addHandler(LogentriesHandler('1d18731d-53e4-41cd-b417-9ef4da1552c2'))


# log.info("test2 worker no worker")

@celery.task
def tryLogTest2Attempt1(inputInfo):
	print("test 2 worker attempt 1")
	print(inputInfo)

@celery.task
def tryLogTest2Attempt2(inputInfo):
	#log = logging.getLogger('logentries')
	#log.setLevel(logging.INFO)
	# Note if you have set up the logentries handler in Django, the following line is not necessary
	#log.addHandler(LogentriesHandler('1d18731d-53e4-41cd-b417-9ef4da1552c2'))
	print("test 2 worker attempt 2")
	print(inputInfo)
 