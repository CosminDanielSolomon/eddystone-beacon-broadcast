from scapy.layers import bluetooth
from scapy.contrib import eddystone
from scapy import compat

# open a HCI socket to device hci0
bt = bluetooth.BluetoothHCISocket(0)

# set the Eddystone frame
ns = compat.hex_bytes('aabbccddeeff11223344')
ins = compat.hex_bytes('112233445566')
edy_UID = eddystone.Eddystone_UID(tx_power=0, namespace=ns, instance=ins,)
edy_frame = eddystone.Eddystone_Frame() / edy_UID
bt.sr(edy_frame.build_set_advertising_data())

# start advertising
bt.sr(bluetooth.HCI_Hdr()/
      bluetooth.HCI_Command_Hdr()/
      bluetooth.HCI_Cmd_LE_Set_Advertise_Enable(enable=True))