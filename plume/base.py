
import logging
from plume.master import FlumeMaster

class PlumeMaster(object):
    def __init__(self, host="localhost", port=35873):
        self.master = FlumeMaster(host, port)
        self._cache = {}
        self.log = logging.getLogger("plume")

    @property
    def statuses(self):
        if self._cache.get('statuses') is None:
            self._cache['statuses'] = self.master.get_node_statuses()
        return self._cache['statuses']

    @property
    def configs(self):
        if self._cache.get('configs') is None:
            self._cache['configs'] = self.master.get_configs()
        return self._cache['configs']

    @property
    def physical_nodes(self):
        if self._cache.get('physical_nodes') is None:
            physical_nodes = set()
            for node, s in self.statuses.items():
                if s['state'] < self.master.STATE_LOST:
                    physical_nodes.add(s['physicalNode'])
            self._cache['physical_nodes'] = physical_nodes
        return self._cache['physical_nodes']

    @property
    def logical_nodes(self):
        if self._cache.get('logical_nodes') is None:
            logical_nodes = set()
            for node, s in self.statuses.items():
                if s['state'] < self.master.STATE_LOST:
                    logical_nodes.add(node)
            self._cache['logical_nodes'] = logical_nodes - self.physical_nodes
        return self._cache['logical_nodes']        

    def configure_node(self, pname, source, sink, flow=None):
        lname = "%s:%s" % (pname, flow)
        if lname not in self.logical_nodes or self.statuses[lname]['physicalNode'] != pname:
            self.log.info("Spawned {logical} on {physical}".format(logical=lname, physical=pname))
            self.master.spawn(pname, lname)
        config = self.configs.get(lname)
        if not config or config['sourceConfig'] != source or config['sinkConfig'] != sink or config['flowID'] != flow:
            self.log.info("Configuring {logical}".format(logical=lname))
            self.master.config(lname, source, sink, flow)

    def reset(self):
        statuses = self.statuses
        configs = self.configs
        # self.unmap_all()
        for name, status in statuses.items():
            if name != status['physicalNode']:
                self.master.unmap(status['physicalNode'], name)
        for name in configs:
            self.master.decommission(name)
        self.master.refresh_all()
