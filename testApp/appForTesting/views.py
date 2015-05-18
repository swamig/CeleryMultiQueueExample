from django.shortcuts import render

# Create your views here.


def assignToWorkerDefault(request):
	from appForTesting import tasks1 
	tasks1.tryLogTest1Attempt1.delay("request")
	tasks1.tryLogTest1Attempt2.delay("request")

def assignToWorkerOther(request):
	from appForTesting import tasks2	
	tasks2.tryLogTest2Attempt1.apply_async(args=["request"], queue="task2")
	tasks2.tryLogTest2Attempt2.apply_async(args=["request"], queue="task2")