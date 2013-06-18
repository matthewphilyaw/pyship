import env_constants as env

class UnitQueue:
    def __init__(self, queue, apply_func):
        self.queue = queue
        self.apply_func = apply_func
            
class PowerModule(object):
    def __init__(self):
        self._power = 0
        self._heat = 0
        self._uqs = {
            env.SystemUnitType.DISCHARGE : UnitQueue([], self._apply_discharge),
            env.SystemUnitType.COOLING   : UnitQueue([], self._apply_cooling),
            env.SystemUnitType.CHARGE    : UnitQueue([], self._apply_charge) }

    def _apply_discharge(self, unit):
        p = self._power - unit.value 
        if p < 0:
            unit.applied(False, env.PowerActionStatus.OVERLOADED)
        self._power = p 
        self._heat = self._heat + unit.value ** 2
        unit.applied(True, env.PowerActionStatus.COMPLETED)

    def _apply_charge(self, unit):
        self._power = self._power + unit.value
        unit.applied(True, env.PowerActionStatus.COMPLETED)

    def _apply_cooling(self, unit):
        c = self._heat - unit.value
        if c < 0:
            c = 0
        self._heat = c
        unit.applied(True, env.PowerActionStatus.COMPLETED)

#----------

    def queue_unit(self, unit):
        self._uqs[unit.unit_type].queue.append(unit)

    def cycle(self):
        for t, uq in self._uqs.iteritems():
            while 0 < len(uq.queue):
                u = uq.queue.pop(0)
                uq.apply_func(u)
                
    def status(self):
        print 'power: ' + str(self._power)
        print 'heat:  ' + str(self._heat)


class BreakablePowerModule(PowerModule):
    def __init__(self):
        super(BreakablePowerModule, self).__init__()

    def queue_unit(self, unit):
        super(BreakablePowerModule, self).queue_unit(unit)
