Python interface to obtain Bluetooth RSSI


To install the pyrssi module,

python setup.py install


For more information, contact
Maxin B. John <maxinbjohn@gmail.com>


/********* To generate RSSI wrapper (for more information)********/
Generating the swig wrapper for pyrssi.c

swig -python -module pyrssi pyrssi.c 

gcc -I /usr/include/python2.4 -c pyrssi.c pyrssi_wrap.c 

ld -shared -o _pyrssi.so pyrssi.o pyrssi_wrap.o -lbluetooth

This will create the _pyrssi.so in the present working directory. 
/************************************************************/


