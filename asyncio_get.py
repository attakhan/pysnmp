import asyncio
from pysnmp.hlapi.asyncio import *


@asyncio.coroutine
def run(varBinds):
    snmpEngine = SnmpEngine()
    while True:
        (errorIndication,
         errorStatus,
         errorIndex,
         varBindTable) = yield from bulkCmd(
           snmpEngine,
           CommunityData('public'),
           UdpTransportTarget(('localhost', 161)),
           ContextData(),
            0, 50,
            *varBinds)

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
            )
                  )
        else:
            for varBindRow in varBindTable:
                for varBind in varBindRow:
                    print(' = '.join([x.prettyPrint() for x in varBind]))

        varBinds = varBindTable[-1]
        if isEndOfMib(varBinds):
            break

    snmpEngine.transportDispatcher.closeDispatcher()


loop = asyncio.get_event_loop()
loop.run_until_complete(
    run([ObjectType(ObjectIdentity('MY-MIB', 'testCount'))])
)