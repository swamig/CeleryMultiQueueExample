celery worker --config=testApp.settings -Q task2
celery worker --config=testApp.settings -Q default,celery
celery beat --cfig=testApp.settings 
