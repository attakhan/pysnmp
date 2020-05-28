#
# PySNMP MIB module MY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/dev/Downloads/MY-MIB
# Produced by pysmi-0.3.4 at Fri May 22 00:45:56 2020
# On host v6-DevBox platform Linux version 3.10.0-862.14.4.el7.x86_64 by user dev
# Using Python version 2.7.5 (default, Jul 13 2018, 13:06:57) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
myMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42))
myMIB.setRevisions(('2020-05-10 00:00',))
if mibBuilder.loadTexts: myMIB.setLastUpdated('202005100000Z')
if mibBuilder.loadTexts: myMIB.setOrganization('AFINITI')
myCompany = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 1))
testCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: testCount.setStatus('current')
testDescription = MibScalar((1, 3, 6, 1, 4, 1, 42, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: testDescription.setStatus('current')
testTrap = NotificationType((1, 3, 6, 1, 4, 1, 42, 1, 3))
if mibBuilder.loadTexts: testTrap.setStatus('current')
mibBuilder.exportSymbols("MY-MIB", testCount=testCount, testDescription=testDescription, testTrap=testTrap, PYSNMP_MODULE_ID=myMIB, myMIB=myMIB, myCompany=myCompany)
