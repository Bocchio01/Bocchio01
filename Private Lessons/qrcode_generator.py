import qrcode
from qrcode.image.styledpil import StyledPilImage
import urllib.parse
import logging

logging.basicConfig(level=logging.INFO)

QR_data = [
    {
        'name': 'Bocchio',
        'logo_url': './assets/img/LogoBocchio.png',
        'qr_url': 'https://bocchio.dev/it/mix/private-lessons'
    },
    {
        'name': 'WhatsApp',
        'logo_url': './assets/img/LogoWhatsApp.png',
        'qr_url': 'https://wa.me/3425016560?text=' + urllib.parse.quote('Ciao Tommaso, ho notato il tuo annuncio di lezioni e sarei interessato/a a provare. Possiamo accordarci? Buona giornata')
    }
]

for data in QR_data:
    logging.info(f"Starting: {data['name']}")

    qr = qrcode.QRCode(
        error_correction=qrcode.ERROR_CORRECT_H,
        version=2,
        border=1,
        box_size=25,
        image_factory=StyledPilImage,
    )

    qr.add_data(data['qr_url'])
    qr.make(fit=True)

    qr_img = qr.make_image(
        embeded_image_path=data['logo_url']
    )
    qr_img.save('./qr/' + data['name'] + '.png')

    logging.info(f"Done: {data['name']}")
