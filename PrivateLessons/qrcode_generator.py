import qrcode
from qrcode.image.styledpil import StyledPilImage
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
        'qr_url': 'https://wa.me/3425016560?text=Ciao%20Tommaso,%20ho%20notato%20il%20tuo%20annuncio%20di%20lezioni%20e%20sarei%20interessato/a%20a%20provare.%20Possiamo%20accordarci?%20Buona%20giornata'
    }
]

for data in QR_data:
    logging.info(f"Starting: {data['name']}")

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        version=2,
        border=1,
        box_size=25,
    )

    qr.add_data(data['qr_url'])
    qr.make(fit=True)

    qr_img = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path=data['logo_url']
    )
    qr_img.save('./qr/' + data['name'] + '.png')

    logging.info(f"Done: {data['name']}")
