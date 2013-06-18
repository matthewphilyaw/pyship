import ship_power
import ship_system
import env_constants as env

if __name__ == '__main__':
    pm = ship_power.BreakablePowerModule()
    pm.status()

    cm = ship_system.SystemUnit(env.SystemUnitType.CHARGE)
    cm.value = 20

    pm.queue_unit(cm)
    pm.queue_unit(cm)
    pm.queue_unit(cm)
    pm.queue_unit(cm)
    pm.queue_unit(cm)
    pm.queue_unit(cm)
    pm.queue_unit(cm)
    pm.queue_unit(cm)
    pm.cycle()

    pm.status()
    
    dm = ship_system.SystemUnit(env.SystemUnitType.DISCHARGE)
    dm.value = 10

    pm.queue_unit(dm)
    pm.queue_unit(dm)
    pm.cycle()


    pm.queue_unit(dm)
    pm.cycle()

    pm.status() 

    ccm = ship_system.SystemUnit(env.SystemUnitType.COOLING)
    ccm.value = 50

    pm.queue_unit(ccm)
    pm.cycle()

    pm.status()