"""
use segno library
https://segno.readthedocs.io/en/latest/index.html
"""
import segno
from segno import helpers

# Create a WIFI config with min. error level "L" or better
ssid="TBD"
password="TBD"
security_standard="WPA"
wifi_config = helpers.make_wifi_data(ssid=ssid, password=password, security=security_standard, hidden=False)
qrcode1 = qrcode2 = segno.make(wifi_config, error='m')

# send to artistic config engine
qrcode1.to_artistic(background='surfaceowl_logo_basic_bw.png',
                   target='guest_wifi_artistic_qr_v01.png',
                   border=0,
                   scale=10,
                   light=None,
                   dark='darkblue', data_dark='steelblue')

qrcode2.save(out='guest_wifi_artistic_qr_v02.png',
             border=0,
             scale=10,
             dark='darkblue', data_dark='steelblue')

qrcode1.to_artistic(background='surfaceowl_logo_basic_bw.png',
                   target='guest_wifi_artistic_qr_v03.png',
                   border=0,
                   scale=10,
                   light=None)

qrcode2.save(out='guest_wifi_artistic_qr_v04.png',
             border=0,
             scale=10)

# TBD qrcode.mask
