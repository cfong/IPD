# Notes: Successfully identified my phone when it is visible to devices -- when not visible (but paired), does not identify

import bluetooth

print("performing inquiry...")

nearby_devices = bluetooth.discover_devices(lookup_names = True)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))
