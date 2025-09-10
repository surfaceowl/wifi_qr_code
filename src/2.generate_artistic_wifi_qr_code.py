"""
use segno library
https://segno.readthedocs.io/en/latest/index.html
"""
import segno
from segno import helpers
from project_utils import get_output_path, resolve_input_art_path

# Create a WIFI config with min. error level "L" or better
ssid = "TBD"
password = "TBD"
security_standard = "WPA"
wifi_config = helpers.make_wifi_data(ssid=ssid, password=password, security=security_standard, hidden=False)
qrcode1 = qrcode2 = segno.make(wifi_config, error='m')

# send to artistic config engine
background = resolve_input_art_path('surfaceowl-logo-basic-bw.png')

target1 = get_output_path(None, 'guest-wifi-artistic-qr-v01')
qrcode1.to_artistic(background=str(background),
                   target=str(target1),
                   border=0,
                   scale=10,
                   light=None,
                   dark='darkblue', data_dark='steelblue')

out2 = get_output_path(None, 'guest-wifi-artistic-qr-v02')
qrcode2.save(out=str(out2),
             border=0,
             scale=10,
             dark='darkblue', data_dark='steelblue')

target3 = get_output_path(None, 'guest-wifi-artistic-qr-v03')
qrcode1.to_artistic(background=str(background),
                   target=str(target3),
                   border=0,
                   scale=10,
                   light=None)

out4 = get_output_path(None, 'guest-wifi-artistic-qr-v04')
qrcode2.save(out=str(out4),
             border=0,
             scale=10)

# TBD qrcode.mask
