from circus.plugins.statsd import BaseObserver
from multiprocessing import cpu_count


class Catcher(BaseObserver):
    name = "Catcher"

    def __init__(self, *args, **config):
        super(Catcher, self).__init__(*args, **config)
        self.watcher = config.get("watcher", None)
        self.procesess_count = int(cpu_count() * float(config.get("multiplier", 1)))

        if self.watcher is None:
            self.statsd.stop()
            self.loop.close()
            raise NotImplementedError('watcher is mandatory for now.')

    def look_after(self):
        info = self.call("stats", name=self.watcher)
        if info["status"] == "error":
            self.statsd.increment("_resource_watcher.%s.error" % self.watcher)
            return

        current_count = len(info['info'].keys())
        if current_count < self.procesess_count:
            for i in range(self.procesess_count - current_count):
                self.call("incr", name=self.watcher)
        elif self.procesess_count < current_count:
            for i in range(current_count - self.procesess_count):
                self.call("decr", name=self.watcher)

    def stop(self):
        self.statsd.stop()
        super(Catcher, self).stop()