import subprocess

from circus import logger
from circus.plugins.statsd import BaseObserver


class DbRestarter(BaseObserver):
    ''' This circus plugin restarts couchdb database when it has more then 500
    CLOSE_WAIT connections'''
    name = 'DbRestarter'

    def __init__(self, *args, **config):
        super(DbRestarter, self).__init__(*args, **config)
        self.db_port = config.get('db_port')

    def look_after(self):
        command = "/usr/bin/netstat -n | grep {} | grep CLOSE_WAIT | wc -l".format(self.db_port)
        output = subprocess.check_output(['bash', '-c', command]).rstrip()
        if int(output) > 500:
            self.cast('restart', name='db')
            self.statsd.increment("high_number_close_wait__sockets_restart")
            logger.info("DB was restarted because of {} CLOSE_WAIT sockets on {} port".format(output, self.db_port))
